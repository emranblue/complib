import os
from platform import system
package=open('requirment.txt').readlines()
systm=system()
for pack in package:
    try:
        if systm=='Linux':
            os.system('pip3 install {}'.format(pack[:-1]))
        elif systm=='Windows':
            os.system('pip install {}'.format(pack[:-1]))
    except:
        print("something bad happened,try again")
