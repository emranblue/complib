#!/usr/bin/env python3
from complib.drawing.artist import Art
import numpy as np


class Pera(Art):


    CONFIG={
            'DATA':100,
            'STAT':True,
            'UNIT':3,
            'TRACKER_COLOR'='red',
            'PERAMETER_COLOR':'yellow'
            }


    def __init__(self,xfunc=None,yfunc=None):
        self.xf=xfunc
        self.yf=yfunc


    def getpera(self,a,b,data=CONFIG['DATA'],stat=CONFIG['STAT']):
        
        def anim(i):
            self.pplot(a,b,self.xf,self.yf)
            self.point(self.xf(i),self.yf(i))
            self.vector(self.xf(i),self.yf(i),color=CONFIG['TRACKER_COLOR'])
            if stat:
                self.vector(CONFIG['UNIT']*np.cos(i),CONFIG['UNIT']*np.sin(i),color=CONFIG['PERAMETER_COLOR'])
        self.animate(anim,np.linspace(a,b,data))
        self.show_anim()


class Polar(Pera):
    def __init__(self,func):
        self.xf=lambda x:func(x)*np.cos(x)
        self.yf=lambda x:func(x)*np.sin(x)


    def getpolar(self,a,b):
        self.getpera(a,b)
