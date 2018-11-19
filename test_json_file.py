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



with open('filename_details.json') as f:
    filename_details = byteify(json.load(f))

output_filename_stub = filename_details['faceted_filename_stub']
model_description = filename_details['model_description']

print('loading ',model_description)
with open(model_description) as f:
    geometry_details = byteify(json.load(f))

print(geometry_details)