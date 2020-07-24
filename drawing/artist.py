from matplotlib.animation import FuncAnimation as anim
import matplotlib.pyplot as plt
from numpy import *
import os
import sys
from platform import system
from complib.util.lib import *

class Art:
    AXIS_COLOR='white'
    AXIS_WIDTH=1
    FPS=10
    FILE_NAME='complib_anim'
    CENTER_LINE_COLOR='#65dbff'
    CENTER_LINE_WIDTH=2
    CENTER_LINE_ALPHA=3
    POINT_COLOR='white'
    VECTOR_COLOR='red'
    PROJECTION_COLOR='#c1ff5d'
    PROJECTION_WIDTH=4
    PROJECTION_ALPHA=3
    LINE_COLOR='#57aa9e'
    BACKGROUND='dark_background'
    DATA_FOR_PDRAW=500
    PDRAW_WIDTH=2
    SCALEX=False
    SCALEY=False
    XLI=10
    YLI=10
    PPLOT_COLOR='#c79eff'
    FPLOT_COLOR='#c869ff'
    AXIS='off'
    AUTOSCALE=False
    HZ=550



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
        plt.axvline(color=self.AXIS_COLOR,linewidth=self.AXIS_WIDTH)
        plt.axhline(color=self.AXIS_COLOR,linewidth=self.AXIS_WIDTH)


    def __design(self):
        plt.style.use(self.BACKGROUND)
        plt.xlim(-self.XLI, self.XLI)
        plt.ylim(-self.YLI, self.YLI)
        plt.autoscale(self.AUTOSCALE)
        plt.axis(self.AXIS)


    def __pdraw(self,a,b,xfunc,yfunc,color):
        data=linspace(a,b,self.DATA_FOR_PDRAW)
        self.__design()
        self.__axis()
        plt.plot(xfunc(data),yfunc(data),linewidth=self.PDRAW_WIDTH,scalex=self.SCALEX,scaley=self.SCALEY,color=color)
        plt.axes().set_aspect('equal')



    def __fdraw(self,func,color):
        data=linspace(-self.XLI,self.YLI,self.DATA_FOR_PDRAW)
        self.__design()
        plt.plot(data,func(data),linewidth=self.PDRAW_WIDTH,scalex=self.SCALEX,scaley=self.SCALEY,color=color)


    def pplot(self,a,b,xfunc,yfunc):
        self.__pdraw(a,b,xfunc,yfunc,self.PPLOT_COLOR)
        



    def __vsave(self,fig,animat,frames,fps,fname):
        self.video=self.__name(fname)
        manim=anim(fig,animat,frames=frames,repeat=False,interval=0)
        manim.save(self.video,fps=fps,writer='ffmpeg')
        if system() is 'Linux':
            beep(0.5,self.HZ)


    def fplot(self,func):
        self.__fdraw(func,self.FPLOT_COLOR)    


    def show(self):
        plt.show()



    def __anim(self,func,i):
        func(i)
        self.__axis()
        self.__design()



    def animate(self,func,fram):
        def animat(i):
            plt.cla()
            func(i)
            self.__axis()
            self.__design()
        self.__vsave(plt.gcf(),animat,fram,fname=self.FILE_NAME,fps=self.FPS)



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



    def from_center_to(self,x,y):
        plt.plot([0,x],[0,y],color=color,linewidth=self.CENTER_LINE_WIDTH,alpha=self.CENTER_LINE_ALPHA)

    def point(self,x,y):
        plt.scatter(x,y,color=self.POINT_COLOR)

    def project_on_x(self,x,y):
        plt.plot([0,x],[0,0],color=self.PROJECTION_COLOR,linewidth=self.WIDTH,alpha=self.ALPHA)

    def project_on_y(self,x,y):
        plt.plot([0,0],[0,y],color=self.PROJECTION_COLOR,linewidth=self.PROJECTON_WIDTH,alpha=self.PROJECTION_ALPHA)
        
    def vector(self,x,y,color=None):
        origin=[0],[0]
        if color is None:
            color=self.VECTOR_COLOR
        plt.quiver(*origin,x,y,color=color,scale_units='xy',units='xy',angles='xy',scale=1,width=0.3,alpha=3)    
        

    def line(self,x0,y0,x,y):
        plt.plot([x0,x],[y0,y],color=self.LINE_COLOR,linewidth=self.CENTER_LINE_WIDTH,alpha=self.CENTER_LINE_ALPHA)

'''going...

    def from_to(self,points=[0,0,3,3],**kwarg):
        xspan=linspace(points[0],points[2],80)
        yspan=linspace(points[1],points[3],80)
        
        '''
