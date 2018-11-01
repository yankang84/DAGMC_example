#!/usr/env/python3
import os
import json


def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


os.system('rm *.log')
os.system('rm *.jou')

cubit.cmd('reset')

cubit.cmd('open "geometry_with_tags_without_extra_vols.trelis"')

cubit.cmd('set attribute on')
#cubit.cmd('export dagmc "geometry_with_material_tags.h5m" faceting_tolerance 1.0e-4')

#cubit.cmd('export dagmc "geometry_with_material_tags.h5m" faceting_tolerance 1.0e-2')

#os.system('mbconvert geometry_with_material_tags.h5m geometry_with_material_tags.stl')

#cubit.cmd('save as "geometry_with_material_tags.cub" overwrite')

cubit.cmd('delete mesh')
current_vols =cubit.parse_cubit_list("volume", "all")

cubit.cmd('Trimesher volume gradation 1.3')
cubit.cmd('volume all size auto factor 5')

with open('geometry_details.json') as f:
    geometry_details = byteify(json.load(f))

for entry in geometry_details:
  for volume in entry['volumes']:
    cubit.cmd('volume '+str(volume)+' size auto factor 6')
    cubit.cmd('volume all scheme tetmesh proximity layers off geometric sizing on')
    if 'mesh_size' in entry.keys():
      cubit.cmd('volume '+str(volume)+' size 0.5')
    cubit.cmd('mesh volume '+str(volume))

# for volume in current_vols:
#   cubit.cmd('volume '+str(volume)+' size auto factor 4')
#   cubit.cmd('volume all scheme tetmesh proximity layers off geometric sizing on')
#   cubit.cmd('mesh volume '+str(volume))

for volume in current_vols:
  print('volume id ', volume, ' is meshed = ', cubit.is_meshed('vol',volume))

cubit.cmd('save as "tetmesh.cub" overwrite')

# additional steps needed for unstructured mesh https://svalinn.github.io/DAGMC/usersguide/tally.html
# os.system('rm *.jou')
# os.system('rm *.log')

# os.system('mbconvert tetmesh.cub tetmesh.h5m')
# os.system('mbconvert tetmesh.h5m tetmesh.vtk')
