from matplotlib.animation import FuncAnimation as anim
import matplotlib.pyplot as plt
from numpy import *
import os
import sys
from platform import system
from complib.util.lib import *

class Art:
    def __init__(self,func=None,video=None):
        self.func=func
        self.video=video


    def __name(self,file_name):
        loc=os.getcwd()
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


    def __axis(self):
        plt.axvline(color='white',linewidth=1)
        plt.axhline(color='white',linewidth=1)


    def __design(self,xli,yli,stat,axis):
        plt.style.use('dark_background')
        plt.xlim(-xli, xli)
        plt.ylim(-yli, yli)
        plt.autoscale(stat)
        plt.axis(axis)


    def __pdraw(self,a,b,xfunc,yfunc,xli,yli,color,stat,axis):
        data=linspace(a,b,500)
        self.__design(xli,yli,stat,axis)
        self.__axis()
        plt.plot(xfunc(data),yfunc(data),linewidth=2,scalex=False,scaley=False,color=color)
        plt.axes().set_aspect('equal')



    def __fdraw(self,func,xli,yli,color,stat,axis):
        data=linspace(-xli,xli,400)
        self.__design(xli,yli,stat,axis)
        #plt.text(xli-3,yli-1,s,fontsize=fs)
        plt.plot(data,func(data),linewidth=2,scalex=False,scaley=False,color=color)


    def pplot(self,a,b,xfunc,yfunc,xli=10,yli=10,color='#c79eff',stat=False,axis='off'):
        self.__pdraw(a,b,xfunc,yfunc,xli,yli,color,stat,axis)
        



    def __vsave(self,fig,animat,frames,arg,fname,fps):
        self.video=self.__name(fname)
        manim=anim(fig,animat,frames=frames,repeat=False,interval=0,fargs=arg)
        manim.save(self.video,fps=fps,writer='ffmpeg')
        if system() is 'Linux':
            beep(0.5,500)


    def fplot(self,func,xli=10,yli=10,color='#c869ff',axis='off',stat=False):
        self.__fdraw(func,xli,yli,color,stat,axis)    


    def show(self):
        plt.show()



    def __anim(self,func,i,xli,yli,stat,axis):
        func(i)
        self.__axis()
        self.__design(xli,yli,stat,axis)



    def animate(self,func,fram,xli=10,yli=10,stat=False,axis='off'):
        arg=[xli,yli,stat,axis]
        def animat(i,*arg):
            plt.cla()
            func(i)
            self.__axis()
            self.__design(*arg)
        self.__vsave(plt.gcf(),animat,fram,arg,fname='complib_anim',fps=10)



    def show_anim(self):
        systm=system()
        if not self.video==None:
            if systm=='Linux':
                os.system('xdg-open {}'.format(self.video))   
            elif systm=='Windows':
                os.system('{}'.format(self.video))
            else:
                print("Not supported system")
        else:
            print("No video found")



    def from_center_to(self,x,y,color='#65dbff',width=2,alpha=2):
        plt.plot([0,x],[0,y],color=color,linewidth=width,alpha=alpha)

    def point(self,x,y,color='white'):
        plt.scatter(x,y,color=color)

    def project_on_x(self,x,y,color='#c1ff5d',width=4,alpha=3):
        plt.plot([0,x],[0,0],color=color,linewidth=width,alpha=alpha)

    def project_on_y(self,x,y):
        plt.plot([0,0],[0,y],color='#9c9faa',linewidth=4,alpha=3)
        
    def vector(self,x,y,color='red'):
        origin=[0],[0]
        plt.quiver(*origin,x,y,color=color,scale_units='xy',units='xy',angles='xy',scale=1,width=0.3,alpha=3)    
        

    def line(self,x0,y0,x,y):
        plt.plot([x0,x],[y0,y],color='#57aa9e',linewidth=2,alpha=3)


    def from_to(self,points=[0,0,3,3],**kwarg):
        xspan=linspace(points[0],points[2],80)
        yspan=linspace(points[1],points[3],80)
