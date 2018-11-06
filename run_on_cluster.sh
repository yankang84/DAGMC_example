

post_zip_filename="geometry_with_tags_zip.h5m"
mcnp_filename="dagmc_demo.inp"
mesh_filename_stub="tetmesh"

submit_script="submit_script_cumulus.sh"

python3 make_dagmcnp_input_file.py -nps=1e7 --output_filename=$mcnp_filename 
python3 make_submit_script.py -nodes=4 -ppn=32 --output_filename=$submit_script


#copy files to cluster
scp $submit_script jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/
scp $post_zip_filename jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/
scp $mcnp_filename jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/
scp $mesh_filename_stub.h5m jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/

ssh -X jshim@login1.cumulus.hpc.l

module load ifort/2017.0.098
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/mcnp/DAGMCV3/moab/lib64:
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/mcnp/mcnpexecs/dag-mcnp611/lib/
export DATAPATH=/home/mcnp/xs/

cd /home/jshim/dagmc_example/

qsub submit_script_cumulus.sh

export PATH=$PATH:/home/jshim/visit/visit2_13_2.linux-x86_64/bin/

# output files include

#fcad
#lcad
#meshtal
#outp
#runtpe
#tally_neutron_spectra.h5m
#tally_tbr.h5m