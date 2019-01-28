from xmltodict import parse
import json


def create_file_name(filename):
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

# https://www.google.co.th/search?ei=8M1NXOCyNovevASdo4zoBQ&q=how+to+write+json+file+in+python&oq=how+to+write+js&gs_l=psy-ab.3.1.0l10.3654.9508..12172...1.0..0.138.1426.12j4......0....1..gws-wiz.......0i71j0i131i67j0i67j0i131.4Mlgl9uNJwg#kpvalbx=1
# https://stackoverflow.com/questions/17043860/python-dump-dict-to-json-file
