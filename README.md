# Baby card 

 a simple python program for create fake driver licence,
 use OpenCV for face detect.

## How to use:
press [1] for shot a picture from the webcam, then press [q] to quit.


## set the environment for Ubuntu 16.04 

### update the system
sudo apt-get update
sudo apt-get upgrade

### install git
sudo apt-get install git

### install developer tools
sudo apt-get install build-essential cmake git pkg-config

### install pre-requisite for OpenCV
sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libatlas-base-dev gfortran

### install pip (Pip Installs Packages)
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

### install virtual environment
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip

### update the bash file ~/.bashrc appending this line
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

### reload the bashrc using 
source ~/.bashrc

### create the virtual environment cv
mkvirtualenv cv

### PLEASE note that you now are in (cv) environment
### look on your prompt to find (cv) that means you still working into a virtual env

### install python2.7 on Ubuntu
sudo apt-get install python2.7-dev

### install numpy
pip install numpy

### download OpenCV
cd ~
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout -b 3.1.0

### download OpenCV contrib
cd ~
git clone https://github.com/Itseez/opencv_contrib.git
cd opencv_contrib
git checkout -b 3.1.0

### setup the build
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..
	
### compile
make -j4

### install
sudo make install
sudo ldconfig

### symlink site-packages
cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so


## copy the repository

### create a folder for reporitory
mkdir ~/Desktop/patente_bimbi

### move to the working folder
cd ~/Desktop/patente_bimbi

### clone the repositories
git clone https://github.com/davidecaminati/Baby_card.git .

### launch the program
python patente.py


