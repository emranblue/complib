#!/usr/bin/env python3
import numpy as np
import math as mt
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as fn
from complib.util.lib import *
class Interpolation:  
    def __init__(self,**kwargs):
        if list(kwargs.keys())==[]:
            raise Exception("provide an arry or file")
        elif list(kwargs.keys())[0]=='array':
            self.array=list(kwargs.values())[0]
            self.stat=0
        elif list(kwargs.keys())[0]=='file_name':
            self.file_name=list(kwargs.values())[0]
            self.stat=1            
    def lagrange(xn,data):
        result=0
        n=len(data[0])
        L=np.ones(n)
        for i in range(n):
            for j in range(n):
                if not i==j:
                    L[i]=L[i]*((xn-data[0][j])/(data[0][i]-data[0][j]))
            result+=L[i]*data[1][i]
        return result
    def for_array(xn,x):
        arr=[]
        for i in xn:
            arr.append(Interpolation.lagrange(i,x))
        return arr   
    def interpolate(self,xn):
        if self.stat==0:
            n=len(self.array)
            x=np.ndarray((2,n))
            y=np.linspace(1,n,n).reshape(1,n)
            x[0,:]=y
            temp=np.array(self.array).reshape(1,n)
            x[1,:]=temp[0,:]
            if isinstance(xn,list) or isinstance(xn,np.ndarray):
                return Interpolation.for_array(xn,x)
            else:    
                return Interpolation.lagrange(xn,x)
        elif self.stat==1:
            if os.path.exists(self.file_name):
                data=np.loadtxt(self.file_name,unpack=True)
                if len(data.shape)==1:
                    n=len(data)
                    x=np.ndarray((2,n))
                    y=np.linspace(1,n,n).reshape(1,n)
                    data=data.reshape(1,n)
                    x[0,:]=y[0,:]
                    x[1,:]=data[0,:]
                    if isinstance(xn,list) or isinstance(xn,np.ndarray):      
                        return Interpolation.for_array(xn,x)   
                    else:
                        return Interpolation.lagrange(xn,x)
                elif len(data.shape)==2:
                    if isinstance(xn,list) or isinstance(xn,np.ndarray):
                        return Interpolation.for_array(xn,data)    
                    else:    
                        return Interpolation.lagrange(xn,data)
                else:
                    print("not a valid file")         
            else:
                print("file does not exists")
        else:
            raise Exception("wrong operation")  
class Nsolution:
    def __init__(self,func,err=0.00001):
        self.func=func
        self.err=err
    def bisec(self,a,b):
        if self.func(a)*self.func(b)<0:
            iter=0
            while(abs(a-b)>self.err):
                if self.func((a+b)/2)*self.func(b)>0:
                    b=(a+b)/2
                else:
                    a=(a+b)/2
                iter+=1    
            return a,iter
        else:
            print("Not solvable,try different pair")          
    def fixed(self,a):
        pass
class Node:
    def __init__(self,func,main_func=None):
        self.func=func
        self.main_func=main_func
    def euler(self,ival,step,start,stop):
        x=np.arange(start,stop+step,step)
        y=[ival]
        for i in range(len(x)-1):
            y.append(y[i]+step*self.func(x[i],y[i]))
        y=np.array(y)
        return x,y  
    def name(self):
        loc=os.getcwd()
        file_name='complib_anim'
        extn='.mp4'
        fname=file_name+extn
        flist=os.listdir(loc)
        i=0
        while True:
            if fname in flist:
                i+=1
                fname=file_name+str(i)+extn
            else:
                break
        return fname                    
    def draw(self,ival,step,start,stop,xlim,ylim,s,color):
        plt.xlim((-xlim, xlim))
        plt.ylim((-ylim, ylim))
        plt.autoscale(False)
        plt.axis('off')
        plt.text(xlim-3,ylim-1,s,fontsize=15)
        plt.plot(*self.euler(ival,step,start,stop),color=color,linewidth=2,scalex=False,scaley=False)  
    def anim_euler(self,ival,frames,start,stop,xlim=10,ylim=10,fps=15,show=True,interval=500,color='#904BB4'):
        plt.style.use('dark_background')
        fig,ax=plt.subplots()
        dlist=np.linspace(0.1,xlim,200)
        fname=self.name()
        def animate(i):
            ax.cla()
            ax.axvline(color='white',linewidth=3)
            ax.axhline(color='white',linewidth=3)
            s='h = {}'.format(i)
            self.draw(ival,i,start,stop,xlim,ylim,s,color)
            if not self.main_func==None:
                plt.plot(dlist,self.main_func(dlist),linewidth=2,color='red')
        manim=fn(fig,animate,frames=np.linspace(frames[0],frames[1],frames[2]),repeat=False,interval=interval)
        manim.save(fname,fps=fps,writer='ffmpeg')
        beep(0.3,400)    
        if show:
            os.system('xdg-open {}'.format(fname))
    def draw_euler(self,ival,step,start,stop,xlim=10,ylim=10,color='#904BB4'):
        self.draw(ival,step,start,stop,xlim,ylim,s,color)
        plt.show()    
            
            
            
            
            
            
            
                         
if __name__=='main':
    pass 

