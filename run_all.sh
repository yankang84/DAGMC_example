#!/bin/bashg


filename="geometry_with_material_tags.h5m"
post_zip_filename="geometry_with_material_tags_zip.h5m"

python3 make_materials.py

trelis make_dagmc_geometry_with_material_tags.py

mbconvert tetmesh.cub tetmesh.h5m
mbconvert tetmesh.h5m tetmesh.vtk


make_watertight $filename

check_watertight $post_zip_filename

uwuw_preproc $post_zip_filename -l materials.h5 -s -v

if [ $? -ne 0 ] ; then
  uwuw_preproc $post_zip_filename -l materials.h5
fi

rm runtp*
rm out*



mcnp6.mpi i=dagmc_demo.inp g=$post_zip_filename xsdir='jeff33_mod.xsdir'


#mbconvert tetmesh.cub tetmesh.h5m
#mbconvert tetmesh.h5m tetmesh.vtk