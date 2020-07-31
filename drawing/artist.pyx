from matplotlib.animation import FuncAnimation as anim
import matplotlib.pyplot as plt
from numpy import *
import os
import sys
from platform import system
from complib.util.lib import *
from data import Data

cdef class Art(Data):


    '''If you want to customise anything,then change only class variable,that may work for you,you should not change any of those method below'''


    cdef void __init__(self,func=None,video=None):
        self.func=func
        self.video=video


    cpdef char* __name(self,file_name):
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


    cpdef void __axis(self):
        if self.AXIS_STATUS:
            plt.axvline(color=self.AXIS_COLOR,linewidth=self.AXIS_WIDTH)
            plt.axhline(color=self.AXIS_COLOR,linewidth=self.AXIS_WIDTH)


    cpdef void __design(self):
        plt.style.use(self.BACKGROUND)
        plt.xlim(-self.XLI, self.XLI)
        plt.ylim(-self.YLI, self.YLI)
        plt.autoscale(self.AUTOSCALE)
        plt.axis(self.AXIS)


    cdef void remove(self,fig):
        plt.gca().lines.remove(fig)


    cpdef void __pdraw(self,a,b,xfunc,yfunc,color):
        data=linspace(a,b,self.DATA_FOR_PDRAW)
        self.__design()
        self.__axis()
        plt.plot(xfunc(data),yfunc(data),linewidth=self.PDRAW_WIDTH,scalex=self.SCALEX,scaley=self.SCALEY,color=color)
        plt.axes().set_aspect('equal')



    cpdef void __fdraw(self,func,color):
        data=linspace(-self.XLI,self.YLI,self.DATA_FOR_PDRAW)
        self.__design()
        plt.plot(data,func(data),linewidth=self.PDRAW_WIDTH,scalex=self.SCALEX,scaley=self.SCALEY,color=color)


    cdef void pplot(self,a,b,xfunc,yfunc):
        self.__pdraw(a,b,xfunc,yfunc,self.PPLOT_COLOR)
        



    cpdef void __vsave(self,fig,animat,frames,fps,fname):
        self.video=self.__name(fname)
        manim=anim(fig,animat,frames=frames,repeat=False,interval=0)
        manim.save(self.video,fps=fps,writer=self.VIDEO_WRITER)
        if system()=='Linux':
            beep(0.5,self.HZ)


    cdef void fplot(self,func):
        self.__fdraw(func,self.FPLOT_COLOR)


    cdef void show(self):
        plt.show()

    cdef void wait(self):
        plt.pause(self.WAIT)

    cdef void __anim(self,func,i):
        func(i)
        self.__axis()
        self.__design()



    cdef void animate(self,func,a,b):
        def animat(i):
            func(i)
            self.__axis()
            self.__design()
        self.__vsave(plt.gcf(),animat,linspace(a,b,self.DATA_PER_UNIT*(b-a)),fname=self.FILE_NAME,fps=self.FPS)


    cdef void clear(self):
        plt.cla()


    cdef void show_anim(self):
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
        return plt.plot([0,x],[0,y],color=self.CENTER_LINE_COLOR,linewidth=self.CENTER_LINE_WIDTH,alpha=self.CENTER_LINE_ALPHA)

    def point(self,x,y):
        return plt.scatter(x,y,color=self.POINT_COLOR)

    def project_on_x(self,x,y):
        return plt.plot([0,x],[0,0],color=self.PROJECTION_COLOR,linewidth=self.PROJECTION_WIDTH,alpha=self.PROJECTION_ALPHA)

    def project_on_y(self,x,y):
        return plt.plot([0,0],[0,y],color=self.PROJECTION_COLOR,linewidth=self.PROJECTION_WIDTH,alpha=self.PROJECTION_ALPHA)
        
    def vector(self,x,y,color=None):
        origin=[0],[0]
        if color is None:
            color=self.VECTOR_COLOR
        return plt.quiver(*origin,x,y,color=color,scale_units='xy',units='xy',angles='xy',scale=1,width=self.VECTOR_WIDTH,alpha=self.VECTOR_ALPHA)
        

    def line(self,x0,y0,x,y):
        return plt.plot([x0,x],[y0,y],color=self.LINE_COLOR,linewidth=self.CENTER_LINE_WIDTH,alpha=self.CENTER_LINE_ALPHA)

'''going...

    def from_to(self,points=[0,0,3,3],**kwarg):
        xspan=linspace(points[0],points[2],80)
        yspan=linspace(points[1],points[3],80)
        
        '''
