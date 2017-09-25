#! /usr/bin/python
# Main script for running the HDR capture-merge sequence
from capturehdr import *
from mergehdr import *
from time import sleep
from datetime import datetime
from subprocess import call
from socket import gethostname
from os import path, makedirs
from shutil import rmtree
from json import loads
from sys import argv

if __name__=="__main__":
    if path.exists('~/pi-hdr-timelapse/static/picams/'):
        rmtree('~/pi-hdr-timelapse/static/picams/')
    makedirs('~/pi-hdr-timelapse/static/picams/')
    data = loads(argv[1])
    # Options for timelapse
    nimages = data['nimages']
    delay = data['delay']
    basename = 'image'
    foldername = gethostname()
    if path.exists(foldername):
        rmtree(foldername)
    makedirs(foldername)
    
    datestring = datetime.now().__format__('%Y-%m-%d_%I%p')
    timelapsename = '%s.mp4' % (datestring)
    # Options for capture
    emin = data['emin']
    emax = data['emax']
    nexp = data['nexp']
    w = data['w']
    h = data['h']
    # Options for merging
    # nothing yet
    # Options for ffmpeg
    # nothing yet

    # Log file
    f = open('hdrpi.log', 'a')
    f.write('Starting HDR sequence.\n')
    f.write('Current Time: ' + datetime.now().isoformat())

    # Initalize camera and set resolution
    camera = InitalizeCamera()
    camera.resolution = (w, h)
    f.write('Initialized Camera.\n')

    
    # Capture our images
    for ii in range(nimages):
        images = CaptureHDRStack(camera, emin, emax, nexp, foldername, ii + 1)
        WriteResponseFile(images)
        f.write('Captured HDR Stack.\n')
        # Merge them into an HDR image
        if not path.exists(foldername + '/hdr'):
            makedirs(foldername + '/hdr')
        imgname = '%s/hdr/%s_%04d.jpg' % (foldername, basename, ii + 1)
        MergeHDRStack(foldername, imgname)
        f.write('Merged HDR Stack.\n')
        sleep(delay)

    # Create the time lapse
    if not path.exists(foldername + '/mp4'):
        makedirs(foldername + '/mp4')
    call(["avconv", "-r", "10", "-i", foldername + "/hdr/" + basename + "_%04d.jpg", "-vcodec", "libx264", "-crf",  "20", "-g", "15", foldername + '/mp4/' + timelapsename])
    f.write('Wrote video\n.')
    f.write('Current Time: ' + datetime.now().isoformat())
    call(['sshpass -p hello123 scp -r -o StrictHostKeyChecking=no ' + foldername + '/ pi@picam1.local:~/pi-hdr-timelapse/static/picams/' + foldername + '/'])
