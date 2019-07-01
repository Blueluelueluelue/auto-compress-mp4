from os import listdir, rename
from os.path import isfile, join
import ffmpy

videopath = 'E:/Work/Call Recordings'
compressedpath = videopath + '/Compressed'
videofilesmp4 = [f for f in listdir(videopath) if isfile(join(videopath, f)) and f.endswith('.mp4') and not f.startswith('comp-')]
print(videofilesmp4)
crf = 25
for file_name in videofilesmp4:
    output_name = join(compressedpath, 'comp-' + file_name)
    inp={join(videopath, file_name):None}
    outp = {output_name:'-vcodec libx264 -crf %d'%crf}
    ff=ffmpy.FFmpeg(inputs=inp,outputs=outp)
    print(ff.cmd) # just to verify that it produces the correct ffmpeg command
    ff.run()
    rename(join(videopath, file_name), join(videopath, 'comp-' + file_name))
    print('{0} renamed to comp-{0}'.format(file_name))
print('done!')