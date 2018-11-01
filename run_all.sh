#!/bin/bashg

#filename_stub = "geometry_"

rm *.jou
rm *.log
rm geometry_with_tags.h5m 
rm geometry_with_tags.stl
rm geometry_with_material_and_tally_tags_without_extra_vols.trelis
rm tetmesh.cub tetmesh.h5m
rm tetmesh.h5m tetmesh.vtk
rm runtp*
rm out*
rm meshta*
rm dagmc_demo.inp
rm materials.h5
rm make_faceted_geometry_with_material_and_tally_tags
rm lcad
rm fcad
rm *.h5m
#tidies up the directory


filename="geometry_with_tags.h5m"
post_zip_filename="geometry_with_tags_zip.h5m"

python make_solid_for_reflecting_surfaces.py --output_filename "CAD_segmented_by_material/reflecting_wedge.stp" \
                                             --radius 5000 \
                                             --height 4000 \
                                             --start_angle 33.75 \
                                             --end_angle 348.75 \
                                             --angle 315 


python3 make_materials_from_file.py
#outputs materials.h5m for transport

#trelis make_faceted_geometry_with_material_and_tally_tags.py
trelis -batch -nographics make_faceted_geometry_with_material_and_tally_tags.py
#outputs:
# geometry_with_material_and_tally_tags_without_extra_vols.trelis for meshing later
# geometry_with_material_and_tally_tags.h5m for particle transport

mbconvert geometry_with_material_and_tally_tags.h5m geometry_with_material_and_tally_tags.stl
#outputs stl file for visulisation

#paraview geometry_with_material_and_tally_tags.stl

#trelis make_unstructured_mesh.py
trelis -batch -nographics make_unstructured_mesh.py
#outputs tetmesh.cub for conversion

mbconvert tetmesh.cub tetmesh.h5m

mbconvert tetmesh.h5m tetmesh.vtk
#outputs vtk file for visulisation


make_watertight $filename

check_watertight $post_zip_filename

uwuw_preproc $post_zip_filename -l materials.h5 -s -v

#if [ $? -ne 0 ] ; then
  uwuw_preproc $post_zip_filename -l materials.h5
#else
#    echo "Failed to perform uwuw_preproc"
#    exit
#fi

python3 make_dagmcnp_input_file.py

mcnp6.mpi i=dagmc_demo.inp g=$post_zip_filename xsdir='jeff33_fendl31d_xsdir'

#alias ssh_cumulus_jshim="ssh -X jshim@login1.cumulus.hpc.l"

