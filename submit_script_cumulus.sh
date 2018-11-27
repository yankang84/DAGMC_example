#################################################################
#!/bin/bash

#PBS -V
               #export all environment variables
#PBS -l nodes=4:ppn=32
#PBS -k oe
    # stdout and err real time in home dir rather than copied back at the end

#PBS -N dagmc_DEMO_NBI
cd $PBS_O_WORKDIR
   #uses the CWD as the home for the job
module unload ifort/12.0.1.107 openmpi/1.10.2
module load ifort/2017.0.098
export LD_LIBRARY_PATH=/home/mcnp/DAGMCV3/moab/lib64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/mcnp/mcnpexecs/dag-mcnp611/lib/:$LD_LIBRARY_PATH
export DATAPATH=/home/mcnp/xs/

mpirun -np 40 /home/mcnp/mcnpexecs/dag-mcnp611/bin/mcnp6.mpi i=dagmc_demo.inp g=geometry_with_tags_zip.h5m xsdir="xsdir_mcnp_jeff33_fendl31d"

#################################################################
