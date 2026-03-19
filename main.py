import zipfile
import subprocess
import requests
from pathlib import Path


def get_new_probable_prime(amt, min_digits, offset):
    response = requests.get(f"https://factordb.com/listtype.php?t=1&mindig={min_digits}&perpage={amt}&start={offset}&download=1")
    return response.text.splitlines()

def prove_primality(batch_size, min_digits, offset):
    with zipfile.ZipFile("results.zip", "w") as archive:
        count = 1
        for probable_prime in get_new_probable_prime(amt=batch_size, min_digits=min_digits, offset=offset):
            subprocess.run(["ecpp", "-n", probable_prime, "-p", "-f", str(count)])
            archive.write(f"{count}.primo")
            for file in Path(".").glob(f"{count}*"):
                file.unlink()
            count += 1

    with open("results.zip", "rb") as f:
        files = {
            "cert": ("results.zip", f, "application/zip")
        }
        cookies = {
            "fdbuser": "76c3e48414df81bfb14c0793e21ddca8"
        }
        response = requests.post(
            "https://factordb.com/uploadcert.php",
            data={"zip": "on"},
            cookies=cookies,
            files=files
        )
        if response.status_code != 200:
            raise Exception(f"Failed to upload cert: {response.text}")
        print("Successfully uploaded certificates!")

    Path("results.zip").unlink()


def main():
    total_amount = 100 # Total amount of probable primes to be checked
    batch_size = 10 # Amount of probable primes to be checked per request to factordb
    min_digits = 500 # The minimum number of digits in the probable prime to be considered
    offset = 0 # Increase this if you are worried that small numbers could be done by someone else
    number_of_batches = total_amount // batch_size # Number of requests to be made

    for i in range(number_of_batches):
        prove_primality(batch_size=batch_size, min_digits=min_digits, offset=offset)


if __name__ == "__main__":
    main()
