sshpass -p hello123 ssh -oStrictHostKeyChecking=no pi@picam1.local 'python ~/pi-hdr-timelapse/runhdrpi.py' &
sshpass -p hello123 ssh -oStrictHostKeyChecking=no pi@picam2.local 'python ~/pi-hdr-timelapse/runhdrpi.py' &
sshpass -p hello123 ssh -oStrictHostKeyChecking=no pi@picam3.local 'python ~/pi-hdr-timelapse/runhdrpi.py' &
