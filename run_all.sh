#!/bin/bashg


filename="geometry_with_material_tags.h5m"
post_zip_filename="geometry_with_material_tags_zip.h5m"

python3 make_materials.py

python2 make_solid_for_reflecting_surfaces.py --radius=50 --height=40 --start_angle=33.75 --end_angle=348.75 --angle=315 --output_filename='reflecting_wedge.stp'
python2 make_solid_for_reflecting_surfaces.py --radius=50 --height=40 --start_angle=348.75 --end_angle=33.75 --angle=45 --output_filename='common_wedge.stp'


trelis make_dagmc_geometry_with_material_tags.py

make_watertight $filename

check_watertight $post_zip_filename

uwuw_preproc $post_zip_filename -l materials.h5 -s -v

if [ $? -ne 0 ] ; then
  uwuw_preproc $post_zip_filename -l materials.h5
fi

rm runtp*
rm out*


mcnp6.mpi i=dagmc_demo.inp g=$post_zip_filename


mbconvert tetmesh.cub tetmesh.h5m
mbconvert tetmesh.h5m tetmesh.vtk