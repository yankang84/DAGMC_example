#!/usr/env/python3
import os

cubit.cmd('reset')

def create_graveyard():
  cubit.cmd('brick x 110')
  cubit.cmd('brick x 111')
  cubit.cmd('subtract volume 1 from volume 2')
  cubit.cmd('group "mat:Graveyard" add volume 3')

def create_wedge():
  os.system('python make_solid_for_reflecting_surfaces.py')
  # input_location_wedge = "/home/jshim/Desktop/cylinder_slice_start_0_end_22.5_angle_22.5.stp"
  input_location_wedge = "cylinder_slice_start_22.5_end_0_angle_337.5.stp"
  cubit.cmd('import step "' + input_location_wedge + '" heal')
  surfaces_in_volume = cubit.parse_cubit_list("surface", " in volume 4")
  print(surfaces_in_volume)
  surface_info_dict = {}
  for surface_id in surfaces_in_volume:
    surface = cubit.surface(surface_id)
    #area = surface.area()
    vertex_in_surface = cubit.parse_cubit_list("vertex", " in surface " + str(surface_id))
    if surface.is_planar()==True and len(vertex_in_surface) == 4 :
      surface_info_dict[surface_id] = {'reflector':True}
    else:
      surface_info_dict[surface_id] = {'reflector':False}
    print()
  print('surface_info_dict',surface_info_dict)
  cubit.cmd('group "mat:Vacuum" add volume 4')
  return surface_info_dict

def find_reflecting_surfaces(surface_info_dict):
    surfaces_in_wedge_volume = cubit.parse_cubit_list("surface", " in volume 4")
    for surface_id in surface_info_dict.keys():
        if surface_info_dict[surface_id]['reflector']==True:
            print(surface_id, 'surface originally reflecting but does it still exist')
            if surface_id not in surfaces_in_wedge_volume:
                del surface_info_dict[surface_id]
    for surface_id in surfaces_in_wedge_volume:
        if surface_id not in surface_info_dict.keys():
            surface_info_dict[surface_id]= {'reflector':True}
    return surface_info_dict

# os.system('python3 make_materials.py')
create_graveyard()
wedge_surface_info_dict = create_wedge()




geometry_details=[]
geometry_details.append({"filename":"CAD_segmented_by_material/blanket_blanket.stp","material":"eurofer"})
geometry_details.append({"filename":"CAD_segmented_by_material/central_sol.stp","material":"eurofer"}) #change to .sat files
geometry_details.append({"filename":"CAD_segmented_by_material/divertor.stp","material":"tungsten"})
geometry_details.append({"filename":"CAD_segmented_by_material/magnets.stp","material":"tungsten"})
geometry_details.append({"filename":"CAD_segmented_by_material/plasma.stp","material":"tungsten"})
geometry_details.append({"filename":"CAD_segmented_by_material/port_plugs.stp","material":"tungsten"})
geometry_details.append({"filename":"CAD_segmented_by_material/vaccuum_vessel.stp","material":"tungsten"})

for entry in geometry_details:
  cubit.cmd('import step "' + entry['filename'] + '" separate_bodies heal group "mat:'+entry['material']+'"') #step
 # cubit.cmd('import step "' + entry['filename'] + '" group "mat:'+entry['material']+'"') #.sat files

cubit.cmd('vol all scale 100')
cubit.cmd('imprint body all')
#cubit.cmd('merge tolerance 1.e-4')
cubit.cmd('merge all')
cubit.cmd('graphics tol angle 3')

updated_wedge_surface_info_dict = find_reflecting_surfaces(wedge_surface_info_dict)
print('wedge_surface_info_dict',wedge_surface_info_dict)

for surface_id in updated_wedge_surface_info_dict.keys():
  if updated_wedge_surface_info_dict[surface_id]['reflector'] == True:
    cubit.cmd('group "boundary:Reflecting" add surf ' +str(surface_id))


#cubit.cmd('export dagmc "geometry_and_materials.h5m" faceting_tolerance 1.0e-4')
cubit.cmd('set attribute on')
#cubit.cmd('export dagmc "geometry_with_material_tags.h5m"')
os.system('rm *.jou')
