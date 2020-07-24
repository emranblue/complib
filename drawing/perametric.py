#!/usr/bin/env python3
from complib.drawing.artist import Art
import numpy as np


class Pera(Art):
    DATA=100
    STAT=True
    UNIT=3
    TRACKER_COLOR='red'
    PERAMETER_COLOR='yellow'

    def __init__(self,xfunc=None,yfunc=None):
        self.xf=xfunc
        self.yf=yfunc


    def getpera(self,a,b):
        
        def anim(i):
            self.pplot(a,b,self.xf,self.yf)
            self.point(self.xf(i),self.yf(i))
            self.vector(self.xf(i),self.yf(i),self.TRACKER_COLOR)
            if self.STAT:
                self.vector(self.UNIT*np.cos(i),self.UNIT*np.sin(i),self.PERAMETER_COLOR)
        self.animate(anim,np.linspace(a,b,self.DATA))
        self.show_anim()


class Polar(Pera):
    def __init__(self,func):
        self.xf=lambda x:func(x)*np.cos(x)
        self.yf=lambda x:func(x)*np.sin(x)


    def getpolar(self,a,b):
        self.getpera(a,b)
