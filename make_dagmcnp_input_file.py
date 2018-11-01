#!/usr/env/python3
import os
import json




with open('geometry_details.json') as f:
    geometry_details = json.load(f)

for entry in geometry_details:
    if 'tally' in entry.keys():
        print(entry)


number_of_tallies = 70

# print(geometry_details)

header = ['c This dag-mcnp6 file was made used DAGMC_example',
          'c https://github.com/Shimwell/DAGMC_example ',
          'c',
          ]

physics_card = ['sdef x=600 y=0 z=0 erg=14.1',
                'print',
                'mode n p',
                'nps 1e7',
                'cut:n    j 1e-11  0.2  0.1  j',
                'cut:p 1e+7 1e-3  -0.5 -0.25 j',
                'c',
                ]

mesh_spectra = ['c neutron spectra on mesh',
                'fmesh$tally_number$4:n geom=dag',
                '       EMESH=1.0000E-07  4.1399E-07  5.3158E-07  6.8256E-07  8.7643E-07 ',
                '       1.1254E-06  1.4450E-06  1.8554E-06  2.3824E-06  3.0590E-06 ',
                '       3.9279E-06  5.0435E-06  6.4760E-06  8.3153E-06  1.0677E-05 ',
                '       1.3710E-05  1.7604E-05  2.2603E-05  2.9023E-05  3.7267E-05 ',
                '       4.7851E-05  6.1442E-05  7.8893E-05  1.0130E-04  1.3007E-04 ',
                '       1.6702E-04  2.1445E-04  2.7536E-04  3.5358E-04  4.5400E-04 ',
                '       5.8295E-04  7.4852E-04  9.6112E-04  1.2341E-03  1.5846E-03 ',
                '       2.0347E-03  2.2487E-03  2.4852E-03  2.6126E-03  2.7465E-03 ',
                '       3.0354E-03  3.3546E-03  3.7074E-03  4.3074E-03  5.5308E-03 ',
                '       7.1017E-03  9.1188E-03  1.0595E-02  1.1709E-02  1.5034E-02 ',
                '       1.9305E-02  2.1875E-02  2.3579E-02  2.4176E-02  2.4788E-02 ',
                '       2.6058E-02  2.7000E-02  2.8501E-02  3.1828E-02  3.4307E-02 ',
                '       4.0868E-02  4.6309E-02  5.2475E-02  5.6562E-02  6.7380E-02 ',
                '       7.2025E-02  7.9499E-02  8.2503E-02  8.6517E-02  9.8037E-02 ',
                '       1.1109E-01  1.1679E-01  1.2277E-01  1.2907E-01  1.3569E-01 ',
                '       1.4264E-01  1.4996E-01  1.5764E-01  1.6573E-01  1.7422E-01 ',
                '       1.8316E-01  1.9255E-01  2.0242E-01  2.1280E-01  2.2371E-01 ',
                '       2.3518E-01  2.4724E-01  2.7324E-01  2.8725E-01  2.9452E-01 ',
                '       2.9721E-01  2.9849E-01  3.0197E-01  3.3373E-01  3.6883E-01 ',
                '       3.8774E-01  4.0762E-01  4.5049E-01  4.9787E-01  5.2340E-01 ',
                '       5.5023E-01  5.7844E-01  6.0810E-01  6.3928E-01  6.7206E-01 ',
                '       7.0651E-01  7.4274E-01  7.8082E-01  8.2085E-01  8.6294E-01 ',
                '       9.0718E-01  9.6167E-01  1.0026E+00  1.1080E+00  1.1648E+00 ',
                '       1.2246E+00  1.2874E+00  1.3534E+00  1.4227E+00  1.4957E+00 ',
                '       1.5724E+00  1.6530E+00  1.7377E+00  1.8268E+00  1.9205E+00 ',
                '       2.0190E+00  2.1225E+00  2.2313E+00  2.3069E+00  2.3457E+00 ',
                '       2.3653E+00  2.3851E+00  2.4660E+00  2.5924E+00  2.7253E+00 ',
                '       2.8651E+00  3.0119E+00  3.1664E+00  3.3287E+00  3.6788E+00 ',
                '       4.0657E+00  4.4933E+00  4.7237E+00  4.9659E+00  5.2205E+00 ',
                '       5.4881E+00  5.7695E+00  6.0653E+00  6.3763E+00  6.5924E+00 ',
                '       6.7032E+00  7.0469E+00  7.4082E+00  7.7880E+00  8.1873E+00 ',
                '       8.6071E+00  9.0484E+00  9.5123E+00  1.0000E+01  1.0513E+01 ',
                '       1.1052E+01  1.1618E+01  1.2214E+01  1.2523E+01  1.2840E+01 ',
                '       1.3499E+01  1.3840E+01  1.4191E+01  1.4550E+01  1.4918E+01 ',
                '       1.5683E+01  1.6487E+01  1.6905E+01  1.7333E+01  1.9640E+01',
                'fc$tally_number$4 dagmc inp=tetmesh.h5m out=tally_neutron_spectra.h5m',
                'c'
                ]


mesh_flux = ['c neutron flux on mesh',
             'fmesh$tally_number$4:n geom=dag',
             'fc$tally_number$4 dagmc inp=tetmesh.h5m out=tally_neutron_flux.h5m',
             'c'
             ]


mesh_neutron_heating = ['c neutron heating on mesh',
                        'fmesh$tally_number$4:n geom=dag',
                        'fc$tally_number$4 dagmc inp=tetmesh.h5m out=tally_neutron_heat.h5m',
                        'fm$tally_number$4 -1 0 1 -4',
                        'c'
                        ]

mesh_photon_heating = ['c photon heating on mesh',
                       'fmesh$tally_number$4:p geom=dag',
                       'fc$tally_number$4 dagmc inp=tetmesh.h5m out=tally_photon_heat.h5m',
                       'fm$tally_number$4 -1 0 -5 -6',
                       'c'
                       ]

mesh_tritium_production =['c tritium production on mesh',
                          'fmesh$tally_number$4:n geom=dag',
                          'fc$tally_number$4 dagmc inp=tetmesh.h5m out=tally_tbr.h5m',
                          'fm$tally_number$4 -1 0 205',
                          'c'
                          ]


#these cell tallies can be included via dagmc and trelis groups
#c 
#f54:n 70
#fc54 tritium_breeding_ratio
#fm54 -1 0 205
#c 
#f26:n 70
#fc26 neutron_heat_deposition_in_the_blanket
#c
#f36:p 70
#fc26 photon_heat_deposition_in_the_blanket
#c

#too slow for testing
#all_parts = [header,physics_card,mesh_spectra,mesh_flux,mesh_neutron_heating,mesh_photon_heating,mesh_tritium_production]
all_parts = [header,physics_card,mesh_spectra,mesh_tritium_production]

f = open("dagmc_demo.inp", "w")
for entry in all_parts:
    number_of_tallies=number_of_tallies+1   
    for line in entry:
        line=line.replace('$tally_number$',str(number_of_tallies))
        print(line)
        if line.endswith('\n'):
            f.write(line+'\n')
            # f.write(line)
        else:
            f.write(line+'\n')
f.close()

print('file written dagmc_demo.inp')

#original file
#this is jons demo dag-mcnp6 file
#c
#sdef x=600 y=0 z=0 erg=14.1
#print
#mode n p 
#nps 1e7
#cut:n    j 1e-11  0.2  0.1  j
#cut:p 1e+7 1e-3  -0.5 -0.25 j
#c
#c neutron flux
#fmesh4:n geom=dag
#       EMESH=1.0000E-07  4.1399E-07  5.3158E-07  6.8256E-07  8.7643E-07 
#       1.1254E-06  1.4450E-06  1.8554E-06  2.3824E-06  3.0590E-06 
#       3.9279E-06  5.0435E-06  6.4760E-06  8.3153E-06  1.0677E-05 
#       1.3710E-05  1.7604E-05  2.2603E-05  2.9023E-05  3.7267E-05 
#       4.7851E-05  6.1442E-05  7.8893E-05  1.0130E-04  1.3007E-04 
#       1.6702E-04  2.1445E-04  2.7536E-04  3.5358E-04  4.5400E-04 
#       5.8295E-04  7.4852E-04  9.6112E-04  1.2341E-03  1.5846E-03 
#       2.0347E-03  2.2487E-03  2.4852E-03  2.6126E-03  2.7465E-03 
#       3.0354E-03  3.3546E-03  3.7074E-03  4.3074E-03  5.5308E-03 
#       7.1017E-03  9.1188E-03  1.0595E-02  1.1709E-02  1.5034E-02 
#       1.9305E-02  2.1875E-02  2.3579E-02  2.4176E-02  2.4788E-02 
#       2.6058E-02  2.7000E-02  2.8501E-02  3.1828E-02  3.4307E-02 
#       4.0868E-02  4.6309E-02  5.2475E-02  5.6562E-02  6.7380E-02 
#       7.2025E-02  7.9499E-02  8.2503E-02  8.6517E-02  9.8037E-02 
#       1.1109E-01  1.1679E-01  1.2277E-01  1.2907E-01  1.3569E-01 
#       1.4264E-01  1.4996E-01  1.5764E-01  1.6573E-01  1.7422E-01 
#       1.8316E-01  1.9255E-01  2.0242E-01  2.1280E-01  2.2371E-01 
#       2.3518E-01  2.4724E-01  2.7324E-01  2.8725E-01  2.9452E-01 
#       2.9721E-01  2.9849E-01  3.0197E-01  3.3373E-01  3.6883E-01 
#       3.8774E-01  4.0762E-01  4.5049E-01  4.9787E-01  5.2340E-01 
#       5.5023E-01  5.7844E-01  6.0810E-01  6.3928E-01  6.7206E-01 
#       7.0651E-01  7.4274E-01  7.8082E-01  8.2085E-01  8.6294E-01 
#       9.0718E-01  9.6167E-01  1.0026E+00  1.1080E+00  1.1648E+00 
#       1.2246E+00  1.2874E+00  1.3534E+00  1.4227E+00  1.4957E+00 
#       1.5724E+00  1.6530E+00  1.7377E+00  1.8268E+00  1.9205E+00 
#       2.0190E+00  2.1225E+00  2.2313E+00  2.3069E+00  2.3457E+00 
#       2.3653E+00  2.3851E+00  2.4660E+00  2.5924E+00  2.7253E+00 
#       2.8651E+00  3.0119E+00  3.1664E+00  3.3287E+00  3.6788E+00 
#       4.0657E+00  4.4933E+00  4.7237E+00  4.9659E+00  5.2205E+00 
#       5.4881E+00  5.7695E+00  6.0653E+00  6.3763E+00  6.5924E+00 
#       6.7032E+00  7.0469E+00  7.4082E+00  7.7880E+00  8.1873E+00 
#       8.6071E+00  9.0484E+00  9.5123E+00  1.0000E+01  1.0513E+01 
#       1.1052E+01  1.1618E+01  1.2214E+01  1.2523E+01  1.2840E+01 
#       1.3499E+01  1.3840E+01  1.4191E+01  1.4550E+01  1.4918E+01 
#       1.5683E+01  1.6487E+01  1.6905E+01  1.7333E+01  1.9640E+01
#fc4 dagmc inp=tetmesh.h5m out=specflux.h5m
#c
#c neutron flux on mesh
#fmesh14:n geom=dag
#fc14 dagmc inp=tetmesh.h5m out=nflux.h5m
#c
#c neutron heating on mesh
#fmesh24:n geom=dag
#fc24 dagmc inp=tetmesh.h5m out=nheat.h5m
#fm24 -1 0 1 -4
#c
#c photon heating on mesh
#fmesh34:p geom=dag
#fc34 dagmc inp=tetmesh.h5m out=pheat.h5m
#fm34 -1 0 -5 -6
#c
#c tritium production on mesh
#fmesh44:n geom=dag
#fc44 dagmc inp=tetmesh.h5m out=tbr.h5m
#fm44 -1 0 103
#c
#c
#c 
#f54:n 70
#fc54 tritium_breeding_ratio
#fm54 -1 0 205
#c
#c
#c
#c 
#f26:n 70
#fc26 integrated_neutron_heat_deposition_in_the_blanket
#c
#f36:p 70
#fc26 integrated_photon_heat_deposition_in_the_blanket
#c