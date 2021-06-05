import os
import shutil
import pathlib
import glob
import json
import yaml

#shutil.move('file.txt', 'path/to/new/directory/')
arr = os.listdir(".")

source_texture_pack ='texturepack_source'
destination_texture_pack='texturepack_dest'

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

def copy_if(source, destination):
    if os.path.exists(source):
        shutil.copy2(source, destination)

# Check if texturepack is compatible
with open(source_texture_pack + '/pack.mcmeta') as json_file:
    data = json.load(json_file)
    if(data['pack']['pack_format'] == 7):
        print('Going to convert...')
    else:
        print('Unsupported pack_format, must be equal: 7 instead: ' + str(data['pack']['pack_format']))
        if not yes_or_no('Do you want to continue ?'):
            exit(0)

copy_if(source_texture_pack + '/pack.png', destination_texture_pack + '/screenshot.png')

if os.path.exists(source_texture_pack + '/CHANGELOG.md'):
    shutil.copy2(source_texture_pack + '/CHANGELOG.md', destination_texture_pack + '/CHANGELOG.md')

if os.path.exists(source_texture_pack + '/LICENSE.txt'):
    shutil.copy2(source_texture_pack + '/LICENSE.txt', destination_texture_pack + '/LICENSE.txt')

txtfiles = []
for file in glob.glob(source_texture_pack + '/**', recursive = True):
    print(file)


data =  []
with open('data/data.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

if (data['TextureConverter'][0]['options'][0]['Version'] == 7):
    print(data['TextureConverter'][1]['Blocks'])
else:
    print('Unsupported pack_format, must be equal: 7 instead: ' + str(data['TextureConverter'][0]['options'][0]['Version']))

with open('data/data2.yaml', 'w') as outfile:
    yaml.dump(data, outfile, default_style=None, default_flow_style=False)