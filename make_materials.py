
import os

from pyne.material import Material,MaterialLibrary,MultiMaterial

from pyne.mcnp import Xsdir

from pyne.nucname import name,id,iselement,isnuclide


myxsdir = Xsdir('/home/jshim/xdata/xsdir')



# def remove_isotopes_not_in_xsdir_and_collapse_particular_elements(mat):
#     to_del = []
#     to_keep = set()
#     for nuc in mat.comp.keys():
#         if nuc not in myxsdir.nucs():
#             to_del.append(nuc)
#         else:
#             to_keep.add(nuc)
            
#     for nuc in to_del:
#         del mat.comp[nuc]
#         print('deleting nuc from material', nuc)

#     to_keep.remove(id('C13'))

#     mat = mat.collapse_elements(to_keep)



eurofer_2016 = Material({'Fe' : 0.88821,
                    'B' : 1e-05,
                    'C' : 0.00105,
                    'N' : 0.0004,
                    'O' : 1e-05,
                    'Al' : 4e-05,
                    'Si' : 0.00026,
                    'P' : 2e-05,
                    'S' : 3e-05,
                    'Ti' : 1e-05,
                    'V' : 0.002,
                    'Cr' : 0.09,
                    'Mn' : 0.0055,
                    'Co' : 5e-05,
                    'Ni' : 0.0001,
                    'Cu' : 3e-05,
                    'Nb' : 5e-05,
                    'Mo' : 3e-05,
                    'Ta' : 0.0012,
                    'W' : 0.011,
                    })
eurofer_2016.density = 7.87 
eurofer_2016 = eurofer.expand_elements()

#this needs changing to be the 2017 version
eurofer = Material({'Fe' : 0.88821,
                    'B' : 1e-05,
                    'C' : 0.00105,
                    'N' : 0.0004,
                    'O' : 1e-05,
                    'Al' : 4e-05,
                    'Si' : 0.00026,
                    'P' : 2e-05,
                    'S' : 3e-05,
                    'Ti' : 1e-05,
                    'V' : 0.002,
                    'Cr' : 0.09,
                    'Mn' : 0.0055,
                    'Co' : 5e-05,
                    'Ni' : 0.0001,
                    'Cu' : 3e-05,
                    'Nb' : 5e-05,
                    'Mo' : 3e-05,
                    'Ta' : 0.0012,
                    'W' : 0.011,
                    })
eurofer.density = 7.87 
eurofer = eurofer.expand_elements()

#warning reference table is in units of 10E-2
Austenitic_steel_316L_N_IG = Material({'Fe' : 0.63684,
                                        'C' : 0.0003,
                                        'Mn' : 0.02,
                                        'Si' : 0.005,
                                        'P' : 0.00025,
                                        'S' : 0.0001,
                                        'Cr' : 0.18,
                                        'Ni' : 0.125,
                                        'Mo' : 0.027,
                                        'N' : 0.0008,
                                        'B' : 1e-05,
                                        'Cu' : 0.003,
                                        'Co' : 0.0005,
                                        'Nb' : 0.0001,
                                        'Ti' : 0.001,
                                        'Ta' : 0.0001,
})
Austenitic_steel_316L_N_IG.density = 7.93                            
Austenitic_steel_316L_N_IG = Austenitic_steel_316L_N_IG.expand_elements()                            
                               
#warning reference table is in units of 10E-2
Pb_15_8_Li = Material({'Li' : 0.062,
                        'Ag' : 0.0001,
                        'Cu' : 0.0001,
                        'Nb' : 0.0001,
                        'Pd' : 0.0001,
                        'Zn' : 0.0001,
                        'Fe' : 0.0005,
                        'Cr' : 0.0005,
                        'Mn' : 0.0005,
                        'Mo' : 0.0005,
                        'Ni' : 0.0005,
                        'V' : 0.0005,
                        'Si' : 0.001,
                        'Al' : 0.001,
                        'Bi' : 0.002,
                        'Sn' : 0.002,
                        'W' : 0.002,
                        'Pb' : 0.99265,
              })
Pb_15_8_Li.density = 10.0
Pb_15_8_Li = Pb_15_8_Li.expand_elements() 
                               
Li4SiO4 = Material({'Li' : 0.22415,
                    'Si' : 0.24077,
                    'O' : 0.5339,
                    'Al' : 3e-05,
                    'C' : 0.001,
                    'Ca' : 3e-05,
                    'Co' : 2e-06,
                    'Cr' : 1e-06,
                    'Cu' : 1e-06,
                    'Fe' : 5e-06,
                    'K' : 1e-05,
                    'Mg' : 5e-06,
                    'Mn' : 1e-06,
                    'Pt' : 9e-05,
                    'Na' : 2e-05,
                    'Ni' : 2e-06,
                    'Ti' : 5e-06,
                    'Zn' : 2e-06,
                    'Zr' : 1e-05,

           })
Li4SiO4.density =2.40
Li4SiO4 = Li4SiO4.expand_elements() 
                               
beryllium = Material({'Be' : 0.98749,
                        'O' : 0.009,
                        'Al' : 0.0009,
                        'Fe' : 0.001,
                        'Mg' : 0.0008,
                        'Si' : 0.0006,
                        'Mn' : 0.0001,
                        'U' : 0.0001,
                        'Co' : 1e-05,
                })
beryllium.densty = 1.85
beryllium = beryllium.expand_elements() 
                               
tungsten = Material({'W' : 0.999595,
                    'Ag' : 1e-05,
                    'Al' : 1.5e-05,
                    'As' : 5e-06,
                    'Ba' : 5e-06,
                    'Ca' : 5e-06,
                    'Cd' : 5e-06,
                    'Co' : 1e-05,
                    'Cr' : 2e-05,
                    'Cu' : 1e-05,
                    'Fe' : 3e-05,
                    'K' : 1e-05,
                    'Mg' : 5e-06,
                    'Mn' : 5e-06,
                    'Na' : 1e-05,
                    'Nb' : 1e-05,
                    'Ni' : 5e-06,
                    'Pb' : 5e-06,
                    'Ta' : 2e-05,
                    'Ti' : 5e-06,
                    'Zn' : 5e-06,
                    'Zr' : 5e-06,
                    'Mo' : 1e-04,
                    'C' : 3e-05,
                    'H' : 5e-06,
                    'N' : 5e-06,
                    'O' : 2e-05,
                    'P' : 2e-05,
                    'S' : 5e-06,
                    'Si' : 2e-05,
                })         
tungsten.density = 19.0
tungsten = tungsten.expand_elements()

# check you are happy with the isotope impuries for Cu_Cr_Zr as the table is ambiguous
CuCrZr = Material({'Cu' :0.9871,
                        'Cr' :0.0075,
                        'Zr' :0.0011,
                        'Co' :0.0005,
                        'Ta' :0.0001,
                        'Nb' :0.001,
                        'B' :1e-05,
                        'O' :0.00032,
                        'Mg' :0.0004,
                        'Al' :3e-05,
                        'Si' :0.0004,
                        'P' :0.00014,
                        'S' :4e-05,
                        'Mn' :2e-05,
                        'Fe' :0.0002,
                        'Ni' :0.0006,
                        'Zn' :0.0001,
                        'As' :0.0001,
                        'Sn' :0.0001,
                        'Sb' :0.00011,
                        'Pb' :0.0001,
                        'Bi' :3e-05,
                    })
CuCrZr.density = 8.9
CuCrZr = CuCrZr.expand_elements()

concrete_ordinary = Material({'H' : 0.00555,
                                'O' : 0.4975,
                                'Si' : 0.3147,
                                'Ca' : 0.0828,
                                'Mg' : 0.0026,
                                'Al' : 0.0469,
                                'S' : 0.0013,
                                'Fe' : 0.0124,
                                'Na' : 0.0171,
                                'K' : 0.0192,
                             })
concrete_ordinary.density = 2.2
concrete_ordinary = concrete_ordinary.expand_elements()

concrete_heavy = Material({'H' : 0.0052,
                            'O' : 0.3273,
                            'C' : 0.004,
                            'Si' : 0.0224,
                            'Ca' : 0.0657,
                            'Mg' : 0.0021,
                            'Al' : 0.0038,
                            'Fe' : 0.568,
                            'P' : 0.0015,
                          })
concrete_heavy.density = 3.6
concrete_heavy = concrete_heavy.expand_elements()

concrete_boronated_heavy = Material({'H' :0.0052,
                                    'O' :0.3258,
                                    'B' :0.003,
                                    'C' :0.004,
                                    'Si' :0.0223,
                                    'Ca' :0.0655,
                                    'Mg' :0.0021,
                                    'Al' :0.0038,
                                    'Fe' :0.5667,
                                    'P' :0.0015,
                                    })
concrete_boronated_heavy.density = 3.6
concrete_boronated_heavy= concrete_boronated_heavy.expand_elements()


mat_lib = MaterialLibrary()
mat_lib["eurofer"] = eurofer
mat_lib["Austenitic_steel_316L_N_IG"] = Austenitic_steel_316L_N_IG
mat_lib["Pb15.8Li"] = Pb_15_8_Li
mat_lib["Li4SiO4"] = Li4SiO4
mat_lib["beryllium"] = beryllium
mat_lib["tungsten"] = tungsten
mat_lib["CuCrZr"] = CuCrZr
mat_lib["concrete_ordinary"] = concrete_ordinary
mat_lib["concrete_heavy"] = concrete_heavy
mat_lib["concrete_boronated_heavy"] = concrete_boronated_heavy


os.system('rm materials.h5')
mat_lib.write_hdf5("materials.h5")
print('Finished creating Pyne materials, materials saved as "materials.h5"')