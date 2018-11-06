#!/usr/env/python3
import os
import json

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-of', '--output_filename', type=str, default='submit_script_cumulus.sh')
parser.add_argument('-nodes', type=str, default='4')
parser.add_argument('-ppn', type=str, default='32')
args = parser.parse_args()


with open('filename_details.json') as f:
    filename_details = json.load(f)

mcnp_filename= filename_details['mcnp_filename']
post_zip_filename=filename_details['post_zip_filename']


submit_commands = ['#################################################################',
                   '#!/bin/bash',
                   '',
                   '#PBS -V',
                   '               #export all environment variables',
                   '##PBS -l select=4:ncpus=8:mem=40gb',
                   '               #chunks, cpus per chunk, mem per chunk',
                   '#PBS -l nodes='+args.nodes+':ppn='+args.ppn,
                   '#PBS -k oe',
                   '    # stdout and err real time in home dir rather than copied back at the end',
                   '',
                   '#PBS -N dagmc_DEMO_NBI',
                   ''
                   'cd $PBS_O_WORKDIR',
                   '   #uses the CWD as the home for the job',
                   'module load ifort/2017.0.098',
                   'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/mcnp/DAGMCV3/moab/lib64:',
                   'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/mcnp/mcnpexecs/dag-mcnp611/lib/',
                   'export DATAPATH=/home/mcnp/xs/',
                   '',
                   'post_zip_filename="geometry_with_tags_zip.h5m"',
                   '',
                   'mpirun -np '+str(int(args.nodes)*int(args.ppn))+' /home/mcnp/mcnpexecs/dag-mcnp611/bin/mcnp6.mpi i='+mcnp_filename+' g='+post_zip_filename+' xsdir="xsdir_mcnp_jeff33_fendl31d"',
                   '',
                   '#################################################################',
                   ]
   

print('creating '+str(args.output_filename))
f = open(args.output_filename, "w")
for line in submit_commands:
    print(line)
    f.write(line+'\n')
f.close()

print('file written '+args.output_filename)