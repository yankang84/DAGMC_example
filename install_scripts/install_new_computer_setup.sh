sudo apt-get update
sudo apt-get upgrade

sudo apt-get dist-upgrade

sudo apt -y install gcc
sudo apt -y install make

sudo apt-get install -y devscripts build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev
sudo apt install -y curl

#python3
sudo apt install -y python3-dev python3-setuptools python3-pip ipython3 python3-tk
sudo python3 -m pip install jupyterlab
sudo jupyter labextension install @jupyter-widgets/jupyterlab-manager


sudo apt-get install -y libncursesw5-dev libgdbm-dev libc6-dev
sudo apt-get install -y zlib1g-dev libsqlite3-dev tk-dev
sudo apt-get install -y libssl-dev openssl
sudo apt-get install -y libffi-dev

#build python3 from source
# https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
#     ./configure
#     make
#     make test
#     sudo make install


#sublime
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-add-repository "deb https://download.sublimetext.com/ apt/stable/"
sudo apt -y install sublime-text

# add python 3 build system (Ctrl +b) to sublime
#Tools -> Build System -> New Build System 
# {
#     "cmd": ["python3", "-i", "-u", "$file"],
#     "file_regex": "^[ ]File \"(...?)\", line ([0-9]*)",
#     "selector": "source.python"
# }

#atom
curl -sL https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
sudo apt-get update
sudo apt-get install -y atom

# mongodb
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
python3 -m pip install pymongo --user
sudo mkdir /data
sudo mkdir /data/db

#react
sudo apt-get -y install nodejs
sudo apt -y install npm
# npm install -g create-react-app
# create-react-app my-app
npm install --save reactstrap react react-dom
npm install --save react react-dom 
npm install --save react-bootstrap
npm install react-select
npm install react-table
npm install react-plotly.js plotly.js
# create-react-app my-app
# npm start

# allows usb drives with exfat format to be accessed
sudo apt install exfat-fuse exfat-utils





pip3 install ipywidgets --user
pip3 install pandas --user
pip3 install matplotlib --user
pip3 install plotly --user
pip3 install dash==0.26.3 --user
pip3 install dash-html-components==0.12.0 --user
pip3 install dash-core-components==0.28.0 --user

wget https://download.jetbrains.com/python/pycharm-community-2018.2.3.tar.gz




#DAGMC
cd $HOME
mkdir dagmc_bld
cd dagmc_bld
mkdir -p $HOME/dagmc_bld/HDF5/bld
cd $HOME/dagmc_bld/HDF5
wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.13/src/hdf5-1.8.13.tar.gz
tar -xzvf hdf5-1.8.13.tar.gz
ln -s hdf5-1.8.13 src
cd $HOME/dagmc_bld/HDF5/bld
../src/configure --enable-shared                    --prefix=$HOME/dagmc_bld/HDF5
make
make check
make install
cd $HOME/dagmc_bld
mkdir -p MOAB/bld
cd $HOME/dagmc_bld/MOAB
git clone https://bitbucket.org/fathomteam/moab
cd $HOME/dagmc_bld/MOAB/moab
git checkout Version5.0

#missing from instructions
sudo apt-get install -y libtool
#missing from instructions
sudo apt install -y autoconf

autoreconf -fi

#missing from instructions
sudo apt-get install devscripts
#missing from instructions
sudo apt-get install gawk
#missing from instructions
#sudo apt-get install gfortran-6

cd $HOME/dagmc_bld/MOAB
ln -s moab src
cd bld
../src/configure --enable-optimize --enable-shared --disable-debug --with-hdf5=$HOME/dagmc_bld/HDF5 --prefix=$HOME/dagmc_bld/MOAB
apt-get install libblas-dev libatlas-dev liblapack-dev


#missing from instructions, not found in ubuntu 8.04
sudo apt-get install -y libblas-dev 
sudo apt-get install -y liblapack-dev


make
make check
make install

#add to path
export PATH=$PATH:$HOME/dagmc_bld/HDF5/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/dagmc_bld/HDF5/lib

export PATH=$PATH:$HOME/dagmc_bld/MOAB/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/dagmc_bld/MOAB/lib





  

 sudo add-apt-repository ppa:alexlarsson/flatpak
    

 sudo apt update
      
 sudo apt install flatpak

 sudo apt install gnome-software-plugin-flatpak

 flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    
 flatpak install https://flathub.org/repo/appstream/org.gimp.GIMP.flatpakref


sudo apt install python3-pytest


pip3 install pytest


sudo apt-get update

sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg 
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce
apt-cache madison docker-ce
sudo apt-get install docker-ce=18.04.0~ce-0~ubuntu .
sudo docker run hello-world




sudo apt -y install git
# ssh-keygen -t rsa -b 4096 -C "mail@jshimwell.com"
# eval "$(ssh-agent -s)"
# ssh-add ~/.ssh/id_rsa
# sudo apt-get install xclip
# xclip -sel clip < ~/.ssh/id_rsa.pub


# freecad
sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
sudo apt-get update 
sudo apt-get install freecad freecad-doc && sudo apt-get upgrade 


#multi screen work spaces
sudo apt install gnome-tweak-tool
