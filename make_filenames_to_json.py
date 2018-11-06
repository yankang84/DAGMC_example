

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-ffs', '--faceted_filename_stub', type=str)
parser.add_argument('-mfs', '--mesh_filename_stub', type=str)
parser.add_argument('-mf', '--materials_filename', type=str)
parser.add_argument('-md', '--model_description', type=str)
parser.add_argument('-mcf', '--mcnp_filename', type=str)
parser.add_argument('-pzf', '--post_zip_filename', type=str)
args = parser.parse_args()


filename_details={'faceted_filename_stub':args.faceted_filename_stub,
                  'mesh_filename_stub':args.mesh_filename_stub,
                  'materials_filename':args.materials_filename,
                  'model_description':args.model_description,
                  'mcnp_filename':args.mcnp_filename,
                  'post_zip_filename':args.post_zip_filename
                 }


with open('filename_details.json', 'w') as outfile:
    json.dump(filename_details, outfile, indent =4)