# Python script for capturing hdr images
import picamera
from os import path, makedirs

def InitalizeCamera():
    """Initalizes the python pi camera interface."""
    camera = picamera.PiCamera()
    return camera

def CaptureHDRStack(camera, exposure_min, exposure_max, nimages, foldername, count):
    """CaptureHDRStack(exposure_min, exposure_max, nimages)
        captures a set of nimages from the pi's camera with
        exposures ranging from min to max.
        Returns a list of filenames of images saved.
    """

    exp_step = (exposure_max - exposure_min) / (nimages-1)
    exposures = range(exposure_min, exposure_max+1, exp_step)
    fnames = []
    for step in exposures:
        # Set filename based on exposure
        if not path.exists(foldername + '/exposures'):
            makedirs(foldername + '/exposures')
        fname = foldername + '/exposures/%de%d.jpg' % (count, step)
        fnames.append(fname)
        # Set camera properties and capture
        camera.brightness = step
        camera.capture(fname)
    return fnames

def WriteResponseFile(fnames):
    """WriteResponseFile(fnames)
        writes the file names to hdrstack
    """
    f = open('hdrstack', 'w')
    for name in fnames:
        f.write(name +'\n')
    f.close()
    return True

if __name__=="__main__":
    pass
