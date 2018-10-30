

export PATH=$PATH:$HOME/dagmc_bld/HDF5/bin

export PATH=$PATH:$HOME/visit/visit2_13_2.linux-x86_64/bin

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/dagmc_bld/HDF5/lib

export PATH=$PATH:$HOME/dagmc_bld/MOAB/bin

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/dagmc_bld/MOAB/lib

#export DATAPATH=$HOME/xdata this is for local installation
export DATAPATH=/home/mcnp/xs

INSTALL_PATH=$HOME/dagmc_bld/DAGMC
INSTALL_PATH=/home/mcnp/mcnpexecs/dagmc_mcnp611




export HDF5_LIBRARIES=/home/jshim/dagmc_bld/HDF5/lib
export HDF5_ROOT=/home/jshim/dagmc_bld/HDF5
export PATH=/home/jshim/dagmc_bld/HDF5/bin:$PATH

export PATH=$PATH:/home/jshim/visit/visit2_13_2.linux-x86_64/bin

export LD_LIBRARY_PATH=/home/jshim/dagmc_bld/HDF5/lib/:$LD_LIBRARY_PATH

export PATH=$PATH:/home/jshim/dagmc_bld/MOAB/bin

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/jshim/dagmc_bld/MOAB/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/jshim/dagmc_bld/HDF5/lib

#export DATAPATH=$HOME/xdata this is for local installation
export DATAPATH=/home/mcnp/xs

#INSTALL_PATH=/home/mcnp/mcnpsource/DAGMC_MCNP611
INSTALL_PATH=/home/mcnp/mcnpexecs/DAGMC_MCNP611

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

#autoreconf -fi

sudo apt-get install devscripts

sudo apt-get install gawk

sudo apt-get install gfortran

cd $HOME/dagmc_bld/MOAB

ln -s moab src

cd bld

#autotools
#../src/configure --enable-optimize --enable-shared --disable-debug --with-hdf5=$HOME/dagmc_bld/HDF5 --prefix=$HOME/dagmc_bld/MOAB

#ifort requires change to moab/util.h
CC=icc CXX=icpc FC=ifort CFLAGS='-fPIC' CXXFLAGS='-fPIC' cmake .. -DENABLE_HDF5=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=.. 

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

cp /home/mcnp/mcnpsource/MCNP6v1/Source/CCFE_MCNP_mods/source.F90                          /home/mcnp/mcnpsource/DAGMC_MCNP611/DAGMC/src/mcnp/mcnp6/Source/src/
cp /home/mcnp/mcnpsource/MCNP6v1/Source/CCFE_MCNP_mods/cR2S_source/cR2S_modules.F90        /home/mcnp/mcnpsource/DAGMC_MCNP611/DAGMC/src/mcnp/mcnp6/Source/src/
cp /home/mcnp/mcnpsource/MCNP6v1/Source/CCFE_MCNP_mods/cR2S_source/cR2S_source.F90         /home/mcnp/mcnpsource/DAGMC_MCNP611/DAGMC/src/mcnp/mcnp6/Source/src/
cp /home/mcnp/mcnpsource/MCNP6v1/Source/CCFE_MCNP_mods/parametric_plasma_source/plasma.F90 /home/mcnp/mcnpsource/DAGMC_MCNP611/DAGMC/src/mcnp/mcnp6/Source/src/

# documentation refers to patch -p0 < patch/dagmc.6.1.1beta.patch which is not in the patch folder
patch -p0 < patch/mcnp611.patch

cd /home/mcnp/mcnpsource/DAGMC_MCNP611/DAGMC/bld

module load ifort/2017.0.098
module load cmake

mkdir $HOME/dagmc_bld/DAGMC/DAGMC/bld

cd /home/mcnp/mcnpsource/DAGMC_MCNP611/DAGMC/bld


rm -rf *

#cmake .. -DCMAKE_INSTALL_PREFIX=$INSTALL_PATH -DMOAB_ROOT=/home/jshim/dagmc_bld/MOAB/lib -DBUILD_MCNP6=on -DMCNP6_DATAPATH=$DATAPATH -DMPI_BUILD=on -DBUILD_STATIC=ON 

CC=icc CXX=icpc FC=ifort cmake .. -DMOAB_ROOT=$HOME/DAGMCV3/moab/lib64/ -DBUILD_MCNP6=ON -DMPI_BUILD=ON -DMCNP6_DATAPATH=/home/mcnp/xs -DCMAKE_INSTALL_PREFIX=$HOME/mcnpexec/dag-mcnp611/

make -j

make install

cd ..
cd lib
export LD_LIBRARY_PATH=/home/mcnp/DAGMCV3/moab/lib64:/home/mcnp/mcnpexecs/dag-mcnp611/lib/:$LD_LIBRARY_PATH

cd ../test
for i in `ls test_*` ; do ./$i ; done
cd ..

chmod o-rx /home/mcnp/mcnpexecs/dagmc_mcnp611/bin/*
chmod g+rx /home/mcnp/mcnpexecs/dagmc_mcnp611/bin/*




cd $HOME

mkdir visit

cd $HOME/visit

wget http://portal.nersc.gov/project/visit/releases/2.13.2/visit2_13_2.linux-x86_64-ubuntu14.tar.gz

tar -zxf visit2_13_2.linux-x86_64-ubuntu14.tar.gz 

cd $HOME/visit/visit2_13_2.linux-x86_64/

cd bin/

rm $HOME/visit2_13_2.linux-x86_64-ubuntu14.tar.gz 

rm $HOME/dagmc_bld/HDF5/hdf5-1.8.13.tar.gz

