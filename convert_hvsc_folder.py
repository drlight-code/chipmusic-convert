#!/usr/bin/env python2

import sys
import os
import datetime
import subprocess
import re

from subprocess import Popen, PIPE
from saunaklub_collection import *

def convert_hvsc_folder(path):
    # make path clean and relative to tmpdir
    if(path.startswith('./C64Music')):
        path = path.replace('./C64Music', '../C64Music')
    else:
        path = '../' + path

    tmpdirname = '.'+str(datetime.datetime.now())
    os.mkdir(tmpdirname)
    os.chdir(tmpdirname)
 
    print('changed to working directory: ' + tmpdirname)
    
    years = []
    authors = []
    for root, dirnames, filenames in os.walk(path):
        for f in filenames:
            if(not f.endswith('.sid')):
               continue

            siddir=root
            sid   =root+'/'+f
            oggdir=root.replace('../C64Music', '../C64Music-ogg')

            if(not os.path.exists(oggdir)):
                os.makedirs(oggdir)

            # sidplay conversion
            command = ['sidplay2', '-s', '-w', sid]
            for part in command:
                print part,
            print('')

            p = Popen(command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = p.communicate()

            songinfo = {}
            # parse sidplay output for author name and year
            for row in stderr.splitlines():
                if ":" in row:
                    row = row.strip('|').strip()
                    key, value = row.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    songinfo[key] = value
                    print( key + ' = ' + value )

            authors.append(songinfo['Author'])

            # clean released value and collect multiple years for sc-meta
            origrel = songinfo['Released']
            rel = ''
            p = re.compile('\d\d\d\d.*')
            m = p.match(origrel)
            if(m):
                rel = origrel[0:4]
                years.append(rel)
            songinfo['Released'] = rel

            # encode as ogg
            for wavfile in os.listdir('.'):
                if wavfile.endswith('.wav'):
                    filename = clean_string(songinfo['Author']) + ' - ' + \
                               clean_string(songinfo['Title']) + ' - ' + \
                               'HVSC - ' + \
                               clean_string(origrel) + '.ogg'
                               
                    #ogg=oggdir+'/'+wavfile.replace('.wav', '.ogg')
                    ogg=oggdir+'/'+filename

                    command = ['oggenc', '-a', songinfo['Author'], '-G', 'Chiptune', '-t', songinfo['Title'], '-l', 'HVSC']
                    if(songinfo['Released'] != ''):
                        command.extend(['-d', songinfo['Released']])
                    command.extend(['-q', str(8), '-o', ogg, wavfile])

                    for part in command:
                        print part,
                    print('')
                    subprocess.call(command)
                    os.remove(wavfile)

            # create saunaklub collection metafile
            mo = meta_object()

            authors = sorted(set(authors))
            authorentry = ''
            for author in authors:
                authorentry += author + '; '
            authorentry = authorentry.rstrip('; ')
#            mo.data_map['year'] = authorentry

#            mo.data_map['artist'] = songinfo['Author'].replace(', ', '; ')

            mo.data_map['artist'] =  authorentry
            mo.data_map['title'] = 'Songs'
            mo.data_map['label'] = 'HVSC'
            mo.data_map['style'] = 'Chiptune'
                        
            years = sorted(set(years))
            yearentry = ''
            for year in years:
                yearentry = yearentry + year + '; '
            yearentry = yearentry.strip('; ')
            mo.data_map['year'] = yearentry

            mo.write_to_metafile(oggdir+'/'+'.saunaklub.meta')
            print('Created saunaklub metafile.')
    
    os.chdir('..')
    os.rmdir(tmpdirname)
    print('Converted: ' + path)



if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print('Please supply the path relative to HVSC as argument! Aborting.')
        sys.exit(1)
    convert_hvsc_folder(sys.argv[1])
