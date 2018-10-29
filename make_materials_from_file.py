#!/usr/env/python3

from pyne.material import Material,MaterialLibrary,MultiMaterial
from pyne.mcnp import mats_from_inp
from pprint import pprint

import os

def check_materials_are_the_same(mat1,mat2):
    if mat1.__class__.__name__ == 'MultiMaterial' or mat2.__class__.__name__ == 'MultiMaterial':
        print('MultiMaterial detechted')
        return False 
    identical= True
    if mat1 == mat2:
        print('mat1==mat2')
    else:
        for entry1, entry2 in zip(mat1.items(),mat2.items()):
            if entry1[0] != entry2[0]:
                print('mismatch in name ',entry1[0], '!=' ,entry2[0])
                identical=False
            if entry1[1] != entry2[1]:
                print('mismatch in quantity',entry1[1], '!=' ,entry2[1])            
                identical=False
    return identical

def split_multimaterial_into_materials(multimat):
    if multimat.__class__.__name__ == 'Material':
        print('Material')
        return multimat
    if multimat.__class__.__name__ == 'MultiMaterial':
        print('MultiMaterial')
        materials=[]
        for item in multimat._mats.items():
            materials.append(item[0])
        return materials


mcnp_lib_nbi_2017 = mats_from_inp("mcnp_models/DEMO_NBI_.i")
mcnp_lib = mats_from_inp("mcnp_models/demo.inp")
mcnp_lib_generic = mats_from_inp("mcnp_models/2017_Generic_DEMO_MCNP_22_5deg_v1_1.txt")

my_material_library = MaterialLibrary()

#check_materials_are_the_same(mat1=mcnp_lib_generic[25],mat2=mcnp_lib_nbi_2017[25])

my_material_library['homogenised_magnet'] = mcnp_lib_generic[25].expand_elements()
#my_material_library['homogenised_magnet'].metadata='homogenised_magnet used in the central sol, poloidal and toroidal magnets'


my_material_library['SS-316L(N)-IG'] = mcnp_lib_generic[50].expand_elements()
# my_material_library['SS-316L(N)-IG'].metadata='SS-316L(N)-IG used in the magnet casing and vacuum vessel skin and cyrostat'



my_material_library['SS316_vol_0.6_and_H2O_vol_0.4'] = mcnp_lib_generic[60].expand_elements()
# my_material_library['SS316_vol_0.6_and_H2O_vol_0.4'].metadata='SS316 - 60%, H2O - 40% vacuum vessel middle section'


materials=split_multimaterial_into_materials(mcnp_lib_generic[15])
for material in materials:
    if material.density == 19.244032325601673:
       my_material_library['tungsten']  = material.expand_elements()
       #my_material_library['tungsten'].metadata='used in divertor layer 1 regular tungsten'
    if material.density == 11.542145657217626:
       my_material_library['tungsten_reduced_density']  = material.expand_elements()
       #my_material_library['tungsten_reduced_density'].metadata='reduced density tungsten used in divertor layer 3'


my_material_library['tungsten_water_cucrzr_copper'] = mcnp_lib_generic[74].expand_elements()
# my_material_library['tungsten_water_cucrzr_copper'].metadata='used in the divertor layer 2, 32.8% water, 18.4% CuCrZr, 9.38% copper, remainder tungsten'
# #mistake in previous nbi model : use of wrong material for divertor layer 2


my_material_library['steel_vol_54_water_vol_46'] = mcnp_lib_generic[75].expand_elements()
# my_material_library['steel_vol_54_water_vol_46'].metadata='used in the divertor layer 4, 46% water, remainder Fe based'

my_material_library['homogenised_blanket'] = mcnp_lib_nbi_2017[6].expand_elements()
# my_material_library['homogenised_blanket'].metadata='used in the blankets 80% Pb-15.7Li (9.5g/cc)  20% EUROFER (7.87g/cc)'

my_material_library['concrete_with_rebar'] = mcnp_lib_nbi_2017[100].expand_elements()
# my_material_library['concrete_with_rebar'].metadata='used in the bioshield 0.5% Steel, 99.5% Concrete'

my_material_library['steel_vol_60_water_vol_40'] = mcnp_lib_nbi_2017[160].expand_elements()
# my_material_library['steel_vol_60_water_vol_40'].metadata='used in lower port plug SS316L(N) - 60%, water (31 bar, 200 C) - 40%'


my_material_library['steel_vol_45_copper_vol_40_alumina_vol_10_water_vol_5'] = mcnp_lib_nbi_2017[77].expand_elements()
# my_material_library['steel_vol_60_water_vol_40'].metadata='used in the ion source case 45% SS 316 40% Cu 10% Alumina 5% Water'

my_material_library['steel_vol_45_copper_vol_40_alumina_vol_10_water_vol_5'] = mcnp_lib_nbi_2017[73].expand_elements()
# my_material_library['steel_vol_60_water_vol_40'].metadata='used in the ion source case 45% SS 316 40% Cu 10% Alumina 5% Water'

# nbi body m73
# nbi other parts m71 m72 m74 m75 m76 m77 m78

try:
    os.system('rm materials.h5')
except:
    pass

my_material_library.write_hdf5("materials.h5")
print('Finished creating Pyne materials, materials saved as "materials.h5"')



#sometimes the string version of the int causes an error
# for item in mat_lib.keys():
#     print(item)
#     trunk = mat_lib[item]
#     trunk.metadata["mat_number"] = int(trunk.metadata["mat_number"])
#     print(trunk)
#     print(trunk.mcnp())

