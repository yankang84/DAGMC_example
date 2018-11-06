#################################################################
#!/bin/bash

#PBS -V
               #export all environment variables
##PBS -l select=4:ncpus=8:mem=40gb
               #chunks, cpus per chunk, mem per chunk
#PBS -l nodes=5:ppn=32
#PBS -k oe
    # stdout and err real time in home dir rather than copied back at the end

#PBS -N dagmc_DEMO_NBI
cd $PBS_O_WORKDIR
   #uses the CWD as the home for the job
module load ifort/2017.0.098
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/mcnp/DAGMCV3/moab/lib64:
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/mcnp/mcnpexecs/dag-mcnp611/lib/
export DATAPATH=/home/mcnp/xs/

post_zip_filename="geometry_with_tags_zip.h5m"

mpirun -np 160 /home/mcnp/mcnpexecs/dag-mcnp611/bin/mcnp6.mpi i=dagmc_demo.inp g=geometry_with_tags_zip.h5m xsdir="xsdir_mcnp_jeff33_fendl31d"

#################################################################
