#!/usr/bin/env python3
from complib.drawing.artist import Art
import numpy as np


class Pera(Art):
    FRAME=100
    TRACKER_STATUS=True
    UNIT=3
    TRACKER_COLOR='red'
    PERAMETER_COLOR='yellow'

    def __init__(self,xfunc=None,yfunc=None):
        self.xf=xfunc
        self.yf=yfunc


    def getpera(self,a,b):
        
        def anim(i):
            self.clear()
            self.pplot(a,b,self.xf,self.yf)
            self.point(self.xf(i),self.yf(i))
            self.vector(self.xf(i),self.yf(i),self.TRACKER_COLOR)
            if self.TRACKER_STATUS:
                self.vector(self.UNIT*np.cos(i),self.UNIT*np.sin(i),self.PERAMETER_COLOR)
        self.animate(anim,np.linspace(a,b,self.FRAME))
        self.show_anim()


class Polar(Pera):
    DATA_PER_PI=50


    def __init__(self,func):
        self.xf=lambda x:func(x)*np.cos(x)
        self.yf=lambda x:func(x)*np.sin(x)


    def getpolar(self,a,b):
        self.FRAME=int(self.DATA_PER_PI*(b-a)/np.pi)
        self.getpera(a,b)
