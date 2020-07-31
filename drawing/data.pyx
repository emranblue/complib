cdef class cData:
    cdef int DATA_PER_UNIT
    cdef str AXIS_COLOR
    cdef bint AXIS_STATUS
    cdef float AXIS_WIDTH
    cdef int FPS
    cdef str FILE_NAME
    cdef float CENTER_LINE_COLOR
    cdef float CENTER_LINE_WIDTH
    cdef float CENTER_LINE_ALPHA
    cdef str POINT_COLOR
    cdef str VECTOR_COLOR
    cdef float VECTOR_WIDTH
    cdef float VECTOR_ALPHA
    cdef str PROJECTION_COLOR
    cdef float PROJECTION_WIDTH
    cdef float PROJECTION_ALPHA
    cdef str LINE_COLOR
    cdef str BACKGROUND
    cdef int DATA_FOR_PDRAW
    cdef float PDRAW_WIDTH
    cdef bint SCALEX
    cdef bint SCALEY
    cdef float XLI
    cdef float YLI
    cdef str PPLOT_COLOR
    cdef str FPLOT_COLOR
    cdef str AXIS
    cdef bint AUTOSCALE
    cdef float HZ
    cdef str VIDEO_WRITER
    cdef float WAIT

    
    def __init__(self):
        self.DATA_PER_UNIT=100
        self.AXIS_COLOR='white'
        self.AXIS_STATUS=True
        self.AXIS_WIDTH=1
        self.FPS=15
        self.FILE_NAME='complib_anim'
        self.CENTER_LINE_COLOR='#65dbff'
        self.CENTER_LINE_WIDTH=2
        self.CENTER_LINE_ALPHA=3
        self.POINT_COLOR='white'
        self.VECTOR_COLOR='red'
        self.VECTOR_WIDTH=0.3
        self.VECTOR_ALPHA=3
        self.PROJECTION_COLOR='#c1ff5d'
        self.PROJECTION_WIDTH=4
        self.PROJECTION_ALPHA=3
        self.LINE_COLOR='#57aa9e'
        self.BACKGROUND='dark_background'
        self.DATA_FOR_PDRAW=500
        self.PDRAW_WIDTH=2
        self.SCALEX=False
        self.SCALEY=False
        self.XLI=10
        self.YLI=10
        self.PPLOT_COLOR='#c79eff'
        self.FPLOT_COLOR='#c869ff'
        self.AXIS='off'
        self.AUTOSCALE=False
        self.HZ=550
        self.VIDEO_WRITER='ffmpeg'
        self.WAIT=0.05
 
 
class Data(CData): pass        
