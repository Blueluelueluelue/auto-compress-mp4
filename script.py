from os import *
from os.path import *
import ffmpy
import sys

videopath = getcwd()
alreadycompressedprefix = 'done-'
compressedfileprefix = 'compressed-'

if len(sys.argv) >= 2:
    videopath = sys.argv[1]
    if not exists(videopath):
        print('provided path doesn\'t exist, exiting...')
        exit()
compressedpath = join(videopath, 'Compressed' )   

if not exists(compressedpath):
    mkdir(compressedpath)
    print('Created a new directory {} where the compressed files will be saved'.format(compressedpath))

try:
    allfilesanddirs = listdir(videopath)
    videofilesmp4 = [f for f in allfilesanddirs if isfile(join(videopath, f)) and f.endswith('.mp4') and not f.startswith(alreadycompressedprefix)]
except:
    print('something went wrong')
else:
    print(videofilesmp4)
    crf = 25
    for file_name in videofilesmp4:
        output_name = join(compressedpath, compressedfileprefix + file_name)
        inp={join(videopath, file_name):None}
        outp = {output_name:'-vcodec libx264 -crf %d'%crf}
        ff=ffmpy.FFmpeg(inputs=inp,outputs=outp)
        print(ff.cmd) # just to verify that it produces the correct ffmpeg command
        ff.run()
        rename(join(videopath, file_name), join(videopath, alreadycompressedprefix + file_name))
        print('{0} renamed to {1}{0}'.format(file_name,alreadycompressedprefix))
    print('done!')