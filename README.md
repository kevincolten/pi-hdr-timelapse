# rPiCam

1. Download image from https://www.dropbox.com/s/qliv8t5ipl3fwj2/raspbian_backup.img?dl=0
1. Install image using [Etcher](https://etcher.io/)
1. Put SD card into raspberry pi. You should be able to test it was installed correctly by navigating to http://picam1.local in your browser
1. SSH into rPi using Terminal
    * ` ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no pi@picam1.local`
    * password `hello123`
1. Change host name via `sudo nano /etc/hostname` and `sudo nano /etc/hosts` to `picam[num]`
    * To Save, type `ctrl-x`, then `y`, then `enter`
1. `sudo reboot` and wait a few seconds
1. You should be able to see the UI at http://picam[num].local


## Contributing
```sh
sudo apt-get update
sudo apt-get install python-picamera enblend libav-tools git python-flask uwsgi
```


pi-hdr-timelapse
================

Python scripts for capturing and merging HDR images on the Raspberry Pi and stringing them into a timelapse.


Installation
------------
You'll need [picamera](https://pypi.python.org/pypi/picamera/) ([git source](https://github.com/waveform80/picamera/)) for managing the camera, [enblend/enfuse](http://enblend.sourceforge.net/) to generate the HDR images and [avconv](https://libav.org/avconv.html) to generate the movie from the images.
```
sudo apt-get update
sudo apt-get install python-picamera enblend libav-tools
```
Then grab these files;
```
git clone https://github.com/KEClaytor/pi-hdr-timelapse.git
```
You should be good to go! Edit the first few lines of runhdrpi.py to your liking (exposure steps, time lapse steps) and go;
```
nano runhdrpi.py
python runhdrpi.py
```

Scheduled Run
-------------
You can also schedule timelapse images with cron (eg. for morning / afternoon timelapse). Make sure that the first line of runhdrpi.py points to your python install. Then just add the following line to your crontab (run `crontab -e`):

```
0 5,20 * * * /home/pi/path-to-script/runhdrpi.py >> /home/pi/path-to-log/runhdrpi.log
```
The above will run the script at 5 AM and 8 PM every day.

**Note:** It seems as though the pi's cron is a bit pecular about time zones. For instance, it _should_ use the local time, however, I find mine only uses UTC ([it seems like others have this problem too](http://www.raspberrypi.org/forums/viewtopic.php?t=70809&p=514956)). So you may have to make allowances for that.
