#!/usr/bin/env python3
import os,signal
import subprocess
import sys
from platform import system
def beep(time,freq):
    if system() is 'Linux':
        subprocess.getoutput('speaker-test -X -t sine -f {} -l 1 & sleep {} && kill -9 $!'.format(freq,time))
