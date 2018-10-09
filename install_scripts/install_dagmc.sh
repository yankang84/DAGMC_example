

export PATH=$PATH:$HOME/dagmc_bld/HDF5/bin

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/dagmc_bld/HDF5/lib

export PATH=$PATH:$HOME/dagmc_bld/MOAB/bin

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/dagmc_bld/MOAB/lib

export DATAPATH=$HOME/xdata

INSTALL_PATH=$HOME/dagmc_bld/DAGMC

cd $HOME

mkdir dagmc_bld

cd dagmc_bld

mkdir -p $HOME/dagmc_bld/HDF5/bld

cd $HOME/dagmc_bld/HDF5

wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.13/src/hdf5-1.8.13.tar.gz

tar -xzvf hdf5-1.8.13.tar.gz

ln -s hdf5-1.8.13 src

cd $HOME/dagmc_bld/HDF5/bld

../src/configure --enable-shared --prefix=$HOME/dagmc_bld/HDF5

make

make check

make install

cd $HOME/dagmc_bld

mkdir -p MOAB/bld

cd $HOME/dagmc_bld/MOAB

git clone https://bitbucket.org/fathomteam/moab

cd $HOME/dagmc_bld/MOAB/moab

git checkout Version5.0

sudo apt-get install -y libtool

sudo apt install -y autoconf

autoreconf -fi

sudo apt-get install devscripts

sudo apt-get install gawk

sudo apt-get install gfortran

cd $HOME/dagmc_bld/MOAB

ln -s moab src

cd bld

../src/configure --enable-optimize --enable-shared --disable-debug --with-hdf5=$HOME/dagmc_bld/HDF5 --prefix=$HOME/dagmc_bld/MOAB

apt-get install libblas-dev libatlas-dev liblapack-dev

sudo apt-get install -y libblas-dev 

sudo apt-get install -y liblapack-dev

make

make check

make install

sudo apt install -y cmake

cd $HOME/dagmc_bld

mkdir DAGMC

cd $HOME/dagmc_bld/DAGMC

#git clone https://github.com/svalinn/DAGMC
git clone git@github.com:Shimwell/DAGMC.git
# the shimwell fork has a small change that is needed to avoid this issue https://github.com/svalinn/DAGMC/issues/562

cd $HOME/dagmc_bld/DAGMC/DAGMC

git checkout develop

cd src/mcnp/mcnp6

#copy the source folder from mcnp6 dvd
cp -r $HOME/MCNP6/Source .

# documentation refers to patch -p0 < patch/dagmc.6.1.1beta.patch which is not in the patch folder
patch -p0 < patch/mcnp611.patch

cd $HOME/dagmc_bld/DAGMC

mkdir $HOME/dagmc_bld/DAGMC/DAGMC/bld

cd $HOME/dagmc_bld/DAGMC/DAGMC/bld

rm -rf *

cmake .. -DCMAKE_INSTALL_PREFIX=$INSTALL_PATH -DMOAB_ROOT=$HOME/dagmc_bld/MOAB/lib -DBUILD_MCNP6=on -DMCNP6_DATAPATH=$DATAPATH -DMPI_BUILD=on

make -j

make install

cd $HOME

mkdir visit

cd visit


wget http://portal.nersc.gov/project/visit/releases/2.13.2/visit2_13_2.linux-x86_64-ubuntu14.tar.gz

tar -zxf visit2_13_2.linux-x86_64-ubuntu14.tar.gz 

cd visit2_13_2.linux-x86_64/

cd bin/

# ./visit to run visit

