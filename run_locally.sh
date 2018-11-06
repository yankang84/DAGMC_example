#!/bin/bashg


faceted_filename_stub="geometry_with_tags"
post_zip_filename="geometry_with_tags_zip.h5m"
mcnp_filename="dagmc_demo.inp"
mesh_filename_stub="tetmesh"
materials_filename="materials.h5m"
#model_description="model_description.json"
model_description="model_description_full.json"

#tidies up the directory
rm *.jou
rm *.log
rm out*
rm dump
rm runtp*
rm lcad
rm fcad
rm $faceted_filename_stub*
rm post_zip_filename
rm mcnp_filename
rm $mesh_filename_stub*
rm materials_filename

python3 make_filenames_to_json.py --faceted_filename_stub=$faceted_filename_stub \
                                   --mesh_filename_stub=$mesh_filename_stub \
                                   --model_description=$model_description \
                                   --materials_filename=$materials_filename \
                                   --mcnp_filename=$mcnp_filename \
                                   --post_zip_filename=$post_zip_filename
#outputs filename_details.json which is used by the trelis scripts                       



python make_solid_for_reflecting_surfaces.py --output_filename "CAD_segmented_by_material/reflecting_wedge.stp" \
                                             --radius 5000 \
                                             --height 4000 \
                                             --start_angle 33.75 \
                                             --end_angle 348.75 \
                                             --angle 315 


python3 make_materials_from_file.py --output_filename=$materials_filename
#outputs materials.h5m for particle transport

trelis -batch -nographics make_faceted_geometry_with_material_and_tally_tags.py 
#trelis make_faceted_geometry_with_material_and_tally_tags.py
#outputs:
# geometry_with_tags.trelis for meshing later
# geometry_with_tags.h5m for particle transport
# geometry_with_tags.stl for paraview or visit visulisation

trelis -batch -nographics make_unstructured_mesh.py 
#trelis make_unstructured_mesh.py
#outputs tetmesh.cub for conversion
#outputs tetmesh.h5m for particle tallies
#outputs tetmesh.vtk for visulisation



make_watertight $faceted_filename_stub.h5m

check_watertight $post_zip_filename

uwuw_preproc $post_zip_filename -l $materials_filename -s -v

#if [ $? -ne 0 ] ; then
  uwuw_preproc $post_zip_filename -l $materials_filename
#else
#    echo "Failed to perform uwuw_preproc"
#    exit
#fi

python3 make_dagmcnp_input_file.py -nps=1e4 --output_filename=$mcnp_filename 

mcnp6.mpi i=dagmc_demo.inp g=geometry_with_tags_zip.h5m xsdir='xsdir_mcnp_jeff33_fendl31d'

