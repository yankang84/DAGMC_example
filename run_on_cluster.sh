

post_zip_filename="geometry_with_tags_zip.h5m"
mcnp_filename="dagmc_demo.inp"
mesh_filename_stub="tetmesh"

submit_script="submit_script_cumulus.sh"

python3 make_dagmcnp_input_file.py -nps=1e7 --output_filename=$mcnp_filename 
python3 make_submit_script.py -nodes=4 -ppn=32 -ncpu=40 --output_filename=$submit_script
#each mpi task needs 23Gb of RAM so we can't use all 32 cpus , each node has 512GB of RAM available

#copy files to cluster
scp $submit_script jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/
scp $post_zip_filename jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/
scp $mcnp_filename jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/
scp $mesh_filename_stub.h5m jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/

ssh -X jshim@login1.cumulus.hpc.l

cd /home/jshim/dagmc_example/

rm out*
rm runt*
rm mctal
rm meshtal
rm tally_tbr.h5m
rm tally_neutron_spectra.h5m

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

/home/jshim/dagmc_bld/MOAB/bin/mbconvert tally_tbr.h5m tally_tbr.vtk
/home/jshim/dagmc_bld/MOAB/bin/mbconvert tally_neutron_spectra.h5m tally_neutron_spectra.vtk
/home/jshim/dagmc_bld/MOAB/bin/mbconvert tally_neutron_heat.h5m tally_neutron_heat.vtk
/home/jshim/dagmc_bld/MOAB/bin/mbconvert tally_photon_heat.h5m tally_photon_heat.vtk

exit

scp jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/tally_neutron_spectra.h5m tally_neutron_spectra.h5m
scp jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/tally_tbr.h5m tally_tbr.h5m
scp jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/tally_neutron_heat.h5m tally_neutron_heat.h5m
scp jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/tally_photon_heat.h5m tally_photon_heat.h5m

scp jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/tally_neutron_spectra.h5m tally_neutron_spectra.vtk
scp jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/tally_tbr.h5m tally_tbr.vtk
scp jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/tally_neutron_heat.h5m tally_neutron_heat.vtk
scp jshim@login1.cumulus.hpc.l:/home/jshim/dagmc_example/tally_photon_heat.h5m tally_photon_heat.vtk
