


python3 make_material.py

python2 make_solid_for_reflecting_surfaces.py

trelis make_dagmc_geometry_with_material_tags.py

make_wateright geometry_with_material_tags.h5m

uwuw_preproc geometry_with_material_tags.h5m -l materials.h5 -s -v

uwuw_preproc geometry_with_material_tags.h5m -l materials.h5



mcnp6.mpi i=dagmc_demo.inp g=geometry_and_materials.h5m

