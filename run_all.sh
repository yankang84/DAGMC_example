#!/bin/bashg

rm *.jou
rm *.log
#tidies up the directory


filename="geometry_with_material_tags.h5m"
post_zip_filename="geometry_with_material_tags_zip.h5m"

python make_solid_for_reflecting_surfaces.py --output_filename "CAD_segmented_by_material/reflecting_wedge.stp" \
                                             --radius 5000 \
                                             --height 4000 \
                                             --start_angle 33.75 \
                                             --end_angle 348.75 \
                                             --angle 315 


python3 make_materials_from_file.py
#outputs materials.h5m for transport

#trelis make_dagmc_faceted_geometry_with_material_tags.py
trelis -batch -nographics make_dagmc_faceted_geometry_with_material_tags.py
#outputs geometry_with_material_tags_without_extra_vols.trelis for meshing later

mbconvert geometry_with_material_tags.h5m geometry_with_material_tags.stl
#outputs stl file for visulisation

#paraview geometry_with_material_tags.stl

trelis -batch -nographics make_dagmc_unstructured_mesh.py
#outputs tetmesh.cub for conversion

mbconvert tetmesh.cub tetmesh.h5m

mbconvert tetmesh.h5m tetmesh.vtk
#outputs vtk file for visulisation


make_watertight $filename

check_watertight $post_zip_filename

uwuw_preproc $post_zip_filename -l materials.h5 -s -v

if [ $? -ne 0 ] ; then
  uwuw_preproc $post_zip_filename -l materials.h5
else
    echo "Failed to perform uwuw_preproc"
    exit
fi

rm runtp*
rm out*
rm meshta*


mcnp6.mpi i=dagmc_demo.inp g=$post_zip_filename xsdir='jeff33_fendl31d_xsdir'


#mbconvert tetmesh.cub tetmesh.h5m
#mbconvert tetmesh.h5m tetmesh.vtk