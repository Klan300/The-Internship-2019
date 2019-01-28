from xmltodict import parse
import json


def create_file_name(filename):
    """
    change name from xml to json name 
    """
    sep = filename.split('.')
    name = './' + './' + '/' + sep[0] + '.json'
    return name, sep


filename = input('file name(INPUT WITH .xml): ')
file = open(filename).read()
diction = parse(file)
name, sep = create_file_name(filename)
with open(name, 'w') as fp:
    json.dump(diction, fp, indent=4)

print(sep[0] + '.json')
