#!/usr/bin/env python3
from complib.drawing.artist import Art
import numpy as np
class Pera(Art):
    def __init__(self,xfunc=None,yfunc=None,t0=-np.pi,t1=np.pi):
        self.xf=xfunc
        self.yf=yfunc
        self.t0=t0
        self.t1=t1
    def getpera(self,a,b,data=100,stat=True):
        def anim(i):
            self.pplot(self.t0,self.t1,self.xf,self.yf)
            self.point(self.xf(i),self.yf(i))
            self.vector(self.xf(i),self.yf(i))
            if stat:
                self.vector(3*np.cos(i),3*np.sin(i),color='yellow')
        self.animate(anim,np.linspace(a,b,data))
        self.show_anim()
class Polar(Pera):
    def __init__(self,func,t0,t1):
        self.xf=lambda x:func(x)*np.cos(x)
        self.yf=lambda x:func(x)*np.sin(x)
        self.t0=t0
        self.t1=t1
    def getpolar(self,a=self.t0,b=self.t1):
        self.getpera(a,b)
