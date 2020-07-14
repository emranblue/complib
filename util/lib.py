# !/usr/bin/env python3
# import os,signal
# import subprocess
# import sys
# from multiprocessing import Process
# import keyboard as key 

# class Util:
#     audio_pid=-100000
#     def __init__(self):
#         pass
#     def beep(self,time,freq):
#         print('beping...')
#         subprocess.getoutput('speaker-test -X -t sine -f {} -l 1 & sleep {} && kill -9 $!'.format(freq,time))
#         print('finfished')
#     def sox(file_name):
#         Util.audio_pid=os.getpid()
#         print(Util.audio_pid)
#         subprocess.getoutput('rec {}'.format(file_name))
#     def audio_rec(self,file_name):
#         print('audio recording...')
#         rec=Process(target=Util.sox,args=file_name)
#         rec.start()
#         print(Util.audio_pid)
#         while True:
#             if key.is_pressed('q'):
#                 os.kill(Util.audio_pid,signal.SIGKILL)
#                 break
#         rec.join()    
#         print('record finished')    
import argparse 
from subprocess import call
from sys import argv

def main():
   parser = argparse.ArgumentParser("Recording video and audio using ffmpeg\nMade by Peter Gottesman\n")
   parser.add_argument("output", help="Set output file")
   parser.add_argument("--vcodec", help="Set video codec")
   parser.add_argument("--acodec", help="Set the audio codec. Setting this will enable audio, if it is not set no audio will be recorded")
   parser.add_argument("-ox", "--offsetx", type=int, default=1680, help="Set the x offset")
   parser.add_argument("-oy", "--offsety", type=int, help="Set the y offset")
   parser.add_argument("-r", "--fps", type=int, default=30, help="Set the y offset")
   parser.add_argument("-W", "--width", type=int, default=1920, help="Set the y offset")
   parser.add_argument("-H", "--height", type=int, default=1080, help="Set the y offset")
   parser.add_argument("-ac", "--audio_channels", type=int, default=2, help="Set the y offset")
   args = parser.parse_args()
   record(args)
   
def record(args):
   output="Unedited/" + args.output
   vcodec=args.vcodec
   acodec=args.acodec
   offsetx=str(args.offsetx)
   offsety=str(args.offsety)
   fps=str(args.fps)
   width=str(args.width)
   height=str(args.height)
   ac=str(args.audio_channels)
   print(args)
   
   cmdstr = "ffmpeg -n -f x11grab -s " + width + "x" + height + "  -i :0.0+" + offsetx + "," + offsety + " -ac " + ac + " -f alsa -i pulse -acodec libmp3lame " + output
   call(cmdstr, shell=True)


if __name__ == "__main__":
    main()