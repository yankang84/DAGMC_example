

# This script adds commands to your $HOME/.bashrc

echo 'export PATH=$PATH:$HOME/dagmc_bld/HDF5/bin' >> ~/.bashrc 

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/dagmc_bld/HDF5/lib' >> ~/.bashrc 

echo 'export PATH=$PATH:$HOME/dagmc_bld/MOAB/bin' >> ~/.bashrc 

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/dagmc_bld/MOAB/lib' >> ~/.bashrc 

echo 'export DATAPATH=$HOME/xdata' >> ~/.bashrc 

echo 'export PATH=$PATH:$INSTALL_PATH/bin' >> ~/.bashrc 

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$INSTALL_PATH/lib' >> ~/.bashrc 

echo 'export PATH=$PATH:/opt/Trelis-16.5/bin/' >> ~/.bashrc 

echo 'export PATH=$PATH:$HOME/opt/visit2_13_2.linux-x86_64/bin/' >> ~/.bashrc 

DAGMC_PATH=$HOME/dagmc_bld' >> ~/.bashrc 

echo 'export PATH=$DAGMC_PATH/HDF5/bin:$PATH' >> ~/.bashrc 

echo 'export PATH=$DAGMC_PATH/MOAB/bin:$PATH' >> ~/.bashrc 

export LD_LIBRARY_PATH=$DAGMC_PATH/MOAB/lib:$LD_LIBRARY_PATH' >> ~/.bashrc 
