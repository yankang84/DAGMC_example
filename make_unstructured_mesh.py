#!/usr/env/python3
import os
import json

# aprepro_vars = cubit.get_aprepro_vars()

# print("Found the following aprepro variables:")
# print(aprepro_vars)
# for var_name in aprepro_vars:
#   val = cubit.get_aprepro_value_as_string(var_name)
#   print("{0} = {1}".format(var_name, val))


# if "output_filename_stub" in aprepro_vars:
#     output_filename_stub = str(cubit.get_aprepro_value_as_string("output_filename_stub"))
# elif "ofs" in aprepro_vars:
#     output_filename_stub = str(cubit.get_aprepro_value_as_string("ofs"))
# else:
#     output_filename_stub = "geometry_with_tags"
#
#print('output_filename_stub',output_filename_stub)

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




cubit.cmd('reset')



with open('filename_details.json') as f:
    filename_details = byteify(json.load(f))
  
faceted_filename_stub = filename_details['faceted_filename_stub']
output_filename_stub = filename_details['mesh_filename_stub']


cubit.cmd('open "'+faceted_filename_stub+'.trelis"')

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
    if 'mesh' in entry.keys():
      if entry['mesh'].lower() != "false":
        cubit.cmd('volume '+str(volume)+' '+entry['mesh']) #' size 0.5'
        cubit.cmd('mesh volume '+str(volume))
    else:
        cubit.cmd('mesh volume '+str(volume))

# for volume in current_vols:
#   cubit.cmd('volume '+str(volume)+' size auto factor 4')
#   cubit.cmd('volume all scheme tetmesh proximity layers off geometric sizing on')
#   cubit.cmd('mesh volume '+str(volume))

for volume in current_vols:
  print('volume id ', volume, ' is meshed = ', cubit.is_meshed('vol',volume))

cubit.cmd('save as "'+output_filename_stub+'.cub" overwrite')

print('unstrutured mesh saved as ',output_filename_stub+'.cub')

# additional steps needed for unstructured mesh https://svalinn.github.io/DAGMC/usersguide/tally.html
# os.system('rm *.jou')
# os.system('rm *.log')

os.system('mbconvert '+output_filename_stub+'.cub '+output_filename_stub+'.h5m')
os.system('mbconvert '+output_filename_stub+'.h5m '+output_filename_stub+'.vtk')

#for each element in the mesh
# find all material names
# allocate material numbers based on these names ('alpha')
# write mcr2s material card using

# find material name
# alocate materials using their name
