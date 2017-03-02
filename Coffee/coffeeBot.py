import os
import time
from subprocess import call

call(["sudo", "python", "turnOnGPIO.py"])

while 1:
    mail = ''

    call(["fetchmail"])

    fastq = [f for f in os.listdir('.') if f.endswith('.coffee')]

    if fastq:
        mail = fastq[0]

    if mail:
        call(["sudo", "python", "doGpio.py"])
        print "\n------------------------------\nCOFFEE REQUEST RECEIVED!\n------------------------------\n"
        call(["rm", mail])
    #else:
        #print "No new messages received :("
    time.sleep(3)
