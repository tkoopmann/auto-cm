sudo apt update && sudo apt upgrade -y
sudo apt install make autoconf libtool-bin libgmp-dev libmpfr-dev libmpc-dev libpari-dev zlib1g zlib1g-dev -y
wget https://www.multiprecision.org/downloads/mpfrcx-0.6.3.tar.gz
tar xvzf mpfrcx-0.6.3.tar.gz
rm mpfrcx-0.6.3.tar.gz
cd mpfrcx-0.6.3
./configure
make
sudo make install
cd ..
git clone https://github.com/flintlib/flint.git
cd flint
./bootstrap.sh
./configure
make
sudo make install
cd ..
wget https://www.multiprecision.org/downloads/cm-0.4.4.tar.gz
tar xvzf cm-0.4.4.tar.gz
rm cm-0.4.4.tar.gz
cd cm-0.4.4
./configure
make
sudo make install
make check
