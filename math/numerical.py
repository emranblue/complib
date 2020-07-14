#!/usr/bin/env python3
import numpy as np
import math as mt
import os
import matplotlib.pyplot as plt

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
    def __init__(self,func):
        self.func=func
    def euler(self,ival,step,start,stop):
        x=np.arange(start,stop+step,step)
        y=[ival]
        for i in range(len(x)-1):
            y.append(y[i]+step*self.func(x[i],y[i]))
        y=np.array(y)
        return x,y  
    def draw_euler(self,ival,step,start,stop):
        plt.plot(*self.euler(ival,step,start,stop))
        plt.show()    

            
            
            
            
            
            
            
                         
if __name__=='main':
    pass 

