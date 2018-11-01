#!/usr/env/python3
import os
import json

# os.system('rm *.log')
# os.system('rm *.jou')

cubit.cmd('reset')


def find_number_of_volumes_in_each_step_file(input_locations):
    body_ids=''
    volumes_in_each_step_file=[]
    #all_groups=cubit.parse_cubit_list("group","all")
    #starting_group_id = len(all_groups)
    for entry in input_locations:
      #starting_group_id = starting_group_id +1
      current_vols =cubit.parse_cubit_list("volume", "all")
      print(entry['filename'])
      if entry['filename'].endswith('.sat'):
        import_type = 'acis'
      if entry['filename'].endswith('.stp') or entry['filename'].endswith('.step'):
        import_type = 'step'
      short_file_name = os.path.split(entry['filename'])[-1]
      #print('short_file_name',short_file_name)
      #cubit.cmd('import '+import_type+' "' + entry['filename'] + '" separate_bodies no_surfaces no_curves no_vertices group "'+str(short_file_name)+'"')
      cubit.cmd('import '+import_type+' "' + entry['filename'] + '" separate_bodies no_surfaces no_curves no_vertices ')
      all_vols = cubit.parse_cubit_list("volume", "all")
      new_vols = set(current_vols).symmetric_difference(set(all_vols))
      new_vols = map(str, new_vols)
      print('new_vols',new_vols,type(new_vols))
      current_bodies = cubit.parse_cubit_list("body","all")
      print('current_bodies',current_bodies)
      #volumes_in_group = cubit.cmd('volume in group '+str(starting_group_id))
      #print('volumes_in_group',volumes_in_group,type(volumes_in_group))
      if len(new_vols) > 1:
        cubit.cmd('unite vol '+ ' '.join(new_vols)+ ' with vol '+' '.join(new_vols))
      all_vols = cubit.parse_cubit_list("volume", "all")
      new_vols_after_unite = set(current_vols).symmetric_difference(set(all_vols))
      new_vols_after_unite = map(str, new_vols_after_unite)      
      #cubit.cmd('group '+str(starting_group_id)+' copy rotate 45 about z repeat 7')
      entry['volumes']=new_vols_after_unite
      cubit.cmd('group "'+short_file_name+'" add volume ' +' '.join(entry['volumes']))
      if 'surface_reflectivity' in entry.keys():
        entry['surface_reflectivity'] = find_all_surfaces_of_reflecting_wedge(new_vols_after_unite)
        print("entry['surface_reflectivity']",entry['surface_reflectivity'])
      #cubit.cmd('volume in group '+str(starting_group_id)+' copy rotate 45 about z repeat 7')
    cubit.cmd('separate body all')
    return input_locations


def create_graveyard():
  current_vols =cubit.parse_cubit_list("volume", "all")
  #makes smaller bounding box
  cubit.cmd('create brick bounding box Volume all extended absolute 100') 
  vols_after_small_box = cubit.parse_cubit_list("volume", "all")
  small_box_vols = set(current_vols).symmetric_difference(set(vols_after_small_box))
  small_bound_box = map(str, small_box_vols)[0]  
  current_vols =cubit.parse_cubit_list("volume", "all")
  cubit.cmd('create brick bounding box Volume all extended absolute 200')
  vols_after_big_box = cubit.parse_cubit_list("volume", "all")
  big_box_vols = set(current_vols).symmetric_difference(set(vols_after_big_box))
  big_bound_box = map(str, big_box_vols)[0]  
  current_vols =cubit.parse_cubit_list("volume", "all")
  cubit.cmd('subtract volume '+small_bound_box+' from volume '+big_bound_box)
  vols_after_substraction = cubit.parse_cubit_list("volume", "all")
  print('vols_after_substraction',vols_after_substraction)
  new_vols = set(current_vols).symmetric_difference(set(vols_after_substraction))
  for vol in new_vols:
    if vol not in small_box_vols and vol not in big_box_vols:
        graveyard_vol = str(vol)
  #graveyard = map(str, new_vols)
  print('graveyard vols =',graveyard_vol)
  cubit.cmd('group "mat:Graveyard" add volume '+graveyard_vol)
  cubit.cmd('volume '+graveyard_vol+' visibility off')
  return graveyard_vol


def find_all_surfaces_of_reflecting_wedge(new_vols):
  surfaces_in_volume = cubit.parse_cubit_list("surface", " in volume "+' '.join(new_vols))
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
  print('surface_info_dict',surface_info_dict)
  return surface_info_dict


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


def find_reflecting_surfaces_of_reflecting_wedge(geometry_details):
    for entry in geometry_details:
        if 'surface_reflectivity' in entry.keys():
            surface_info_dict = entry['surface_reflectivity']
            wedge_volume = ' '.join(entry['volumes'])
            surfaces_in_wedge_volume = cubit.parse_cubit_list("surface", " in volume "+str(wedge_volume))
            for surface_id in surface_info_dict.keys():
                if surface_info_dict[surface_id]['reflector']==True:
                    print(surface_id, 'surface originally reflecting but does it still exist')
                    if surface_id not in surfaces_in_wedge_volume:
                        del surface_info_dict[surface_id]
            for surface_id in surfaces_in_wedge_volume:
                if surface_id not in surface_info_dict.keys():
                    surface_info_dict[surface_id]= {'reflector':True}
                    cubit.cmd('group "boundary:Reflecting" add surf ' +str(surface_id))
                    cubit.cmd('surface ' +str(surface_id)+' visibility on')            
            entry['surface_reflectivity'] = surface_info_dict
            return geometry_details, wedge_volume


def scale_geometry(geometry_details):
  for entry in geometry_details:
    if 'scale' in entry.keys():
      cubit.cmd('volume ' +' '.join(entry['volumes'] + ' scale ' + str(entry['scale'])))

def color_geometry(geometry_details):
    for entry in geometry_details:
       #cubit.cmd('group "'+os.path.split(entry['filename'])[-1]+'" add volume ' +' '.join(entry['volumes'])) # can be performed here or in the file loading
       cubit.cmd('group "mat:'+entry['material']+'" add volume ' +' '.join(entry['volumes']))
       print(entry)
       if "color" in entry.keys():
        print('color in keys')
        # Available Colors https://www.csimsoft.com/help/appendix/available_colors.htm
        cubit.cmd('Color volume '+' '.join(entry['volumes'])+ ' '+ entry['color'])    
       if "tallies" in entry.keys():
        for tally in entry['tallies']:
          print('adding tally group',tally)
          cubit.cmd('group "tally:'+tally+'" add volume ' +' '.join(entry['volumes']))


with open('model_description.json') as f:
    geometry_details = byteify(json.load(f))

geometry_details = find_number_of_volumes_in_each_step_file(geometry_details)

scale_geometry(geometry_details)

graveyard_vol = create_graveyard()

color_geometry(geometry_details)

cubit.cmd('imprint body all')
#cubit.cmd('merge tolerance 1.e-4') #optional as there is a default
cubit.cmd('merge vol all group_results')
cubit.cmd('graphics tol angle 3')


updated_wedge_surface_info_dict,wedge_volume = find_reflecting_surfaces_of_reflecting_wedge(geometry_details)

cubit.cmd('set attribute on')

cubit.cmd('export dagmc "geometry_with_tags.h5m" faceting_tolerance 1.0e-2') # change to 1.0e-4 for accurate simulations

#os.system('mbconvert geometry_with_material_and_tally_tags.h5m geometry_with_material_and_tally_tags.stl')
# now peformed by run_all.sh

cubit.cmd('save as "geometry_with_tags.cub" overwrite')

#cubit.cmd('delete Group "mat:Graveyard"')
#cubit.cmd('delete Group "mat:Vacuum"')
cubit.cmd('delete volume '+wedge_volume)
cubit.cmd('delete volume '+graveyard_vol)
cubit.cmd('save as "geometry_with_tags_without_extra_vols.trelis" overwrite')
with open('geometry_details.json', 'w') as outfile:
    json.dump(geometry_details, outfile, indent =4)
