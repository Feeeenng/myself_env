# encoding: utf-8
# module PyQt5.QtGui
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QSurface(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def supportsOpenGL(self): # real signature unknown; restored from __doc__
        """ supportsOpenGL(self) -> bool """
        return False

    def surfaceClass(self): # real signature unknown; restored from __doc__
        """ surfaceClass(self) -> QSurface.SurfaceClass """
        pass

    def surfaceType(self): # real signature unknown; restored from __doc__
        """ surfaceType(self) -> QSurface.SurfaceType """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Offscreen = 1
    OpenGLSurface = 1
    RasterGLSurface = 2
    RasterSurface = 0
    Window = 0


