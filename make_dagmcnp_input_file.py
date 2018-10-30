#!/usr/env/python3
import os
import json




with open('geometry_details.json') as f:
    geometry_details = json.load(f)

for entry in geometry_details:
    if 'tally' in entry.keys():
        print(entry)


number_of_tallies = 0

# print(geometry_details)


physics_card = ['sdef x=600 y=0 z=0 erg=14.1'
                'print'
                'mode n p'
                'nps 1e7'
                'cut:n    j 1e-11  0.2  0.1  j'
                'cut:p 1e+7 1e-3  -0.5 -0.25 j'
                ]