

DAGMC_PATH=$HOME/dagmc_bld

export PATH=$DAGMC_PATH/HDF5/bin:$PATH

export PATH=$DAGMC_PATH/MOAB/bin:$PATH

export LD_LIBRARY_PATH=$DAGMC_PATH/MOAB/lib:$LD_LIBRARY_PATH

pip3 install tables --user

git clone https://github.com/pyne/pyne

cd pyne

python3 setup.py install --user -- -DHDF5_ROOT=$HOME/dagmc_bld/HDF5 -DMOAB_ROOT=$HOME/dagmc_bld/MOAB

nuc_data_make --fetch-prebuilt=no -m atomic_mass,scattering_lengths,decay,materials,q_values,dose_factors
