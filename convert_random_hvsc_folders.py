#!/usr/bin/env python2

import sys
import os
import random
import subprocess
import datetime
import convert_hvsc_folder

if(len(sys.argv) > 2):
    print('Pass zero or one arguments. Aborting!')
    sys.exit(1)

count = 1
if(len(sys.argv) == 2):
    count = int(sys.argv[1])

output = 'converting ' + str(count) + ' random HVSC folder'
if(count == 1):
    output += '...'
else:
    output += 's...'
print(output)

matches = []
for root, dirnames, filenames in os.walk('./C64Music/MUSICIANS'):
    if( not dirnames ):
        matches.append(root)

converted = []
while(count > 0 and len(matches) > 0):
    path = random.choice(matches)

    # see if parent contains .sid as well
    useparent = False
    ppath = path+'/..'
    for filename in os.listdir(ppath):
        if(filename.endswith('.sid')):
            useparent = True
    if(useparent):
        path = ppath        

    # check if folder was already converted
    newpath=path.replace('./C64Music', './C64Music-ogg')
    if(os.path.exists(newpath)):
       matches.remove(path)
       continue

    convert_hvsc_folder.convert_hvsc_folder(path)
    converted.append(newpath)

    matches.remove(path)
    count -= 1

print('')
print('Converted directories:')
for c in converted:
    print(c)
