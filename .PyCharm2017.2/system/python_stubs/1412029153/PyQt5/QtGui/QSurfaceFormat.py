# encoding: utf-8
# module PyQt5.QtGui
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QSurfaceFormat(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QSurfaceFormat()
    QSurfaceFormat(QSurfaceFormat.FormatOptions)
    QSurfaceFormat(QSurfaceFormat)
    """
    def alphaBufferSize(self): # real signature unknown; restored from __doc__
        """ alphaBufferSize(self) -> int """
        return 0

    def blueBufferSize(self): # real signature unknown; restored from __doc__
        """ blueBufferSize(self) -> int """
        return 0

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ defaultFormat() -> QSurfaceFormat """
        return QSurfaceFormat

    def depthBufferSize(self): # real signature unknown; restored from __doc__
        """ depthBufferSize(self) -> int """
        return 0

    def greenBufferSize(self): # real signature unknown; restored from __doc__
        """ greenBufferSize(self) -> int """
        return 0

    def hasAlpha(self): # real signature unknown; restored from __doc__
        """ hasAlpha(self) -> bool """
        return False

    def majorVersion(self): # real signature unknown; restored from __doc__
        """ majorVersion(self) -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ minorVersion(self) -> int """
        return 0

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QSurfaceFormat.FormatOptions """
        pass

    def profile(self): # real signature unknown; restored from __doc__
        """ profile(self) -> QSurfaceFormat.OpenGLContextProfile """
        pass

    def redBufferSize(self): # real signature unknown; restored from __doc__
        """ redBufferSize(self) -> int """
        return 0

    def renderableType(self): # real signature unknown; restored from __doc__
        """ renderableType(self) -> QSurfaceFormat.RenderableType """
        pass

    def samples(self): # real signature unknown; restored from __doc__
        """ samples(self) -> int """
        return 0

    def setAlphaBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setAlphaBufferSize(self, int) """
        pass

    def setBlueBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setBlueBufferSize(self, int) """
        pass

    def setDefaultFormat(self, QSurfaceFormat): # real signature unknown; restored from __doc__
        """ setDefaultFormat(QSurfaceFormat) """
        pass

    def setDepthBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setDepthBufferSize(self, int) """
        pass

    def setGreenBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setGreenBufferSize(self, int) """
        pass

    def setMajorVersion(self, p_int): # real signature unknown; restored from __doc__
        """ setMajorVersion(self, int) """
        pass

    def setMinorVersion(self, p_int): # real signature unknown; restored from __doc__
        """ setMinorVersion(self, int) """
        pass

    def setOption(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setOption(self, QSurfaceFormat.FormatOptions)
        setOption(self, QSurfaceFormat.FormatOption, on: bool = True)
        """
        pass

    def setOptions(self, QSurfaceFormat_FormatOptions): # real signature unknown; restored from __doc__
        """ setOptions(self, QSurfaceFormat.FormatOptions) """
        pass

    def setProfile(self, QSurfaceFormat_OpenGLContextProfile): # real signature unknown; restored from __doc__
        """ setProfile(self, QSurfaceFormat.OpenGLContextProfile) """
        pass

    def setRedBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setRedBufferSize(self, int) """
        pass

    def setRenderableType(self, QSurfaceFormat_RenderableType): # real signature unknown; restored from __doc__
        """ setRenderableType(self, QSurfaceFormat.RenderableType) """
        pass

    def setSamples(self, p_int): # real signature unknown; restored from __doc__
        """ setSamples(self, int) """
        pass

    def setStencilBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setStencilBufferSize(self, int) """
        pass

    def setStereo(self, bool): # real signature unknown; restored from __doc__
        """ setStereo(self, bool) """
        pass

    def setSwapBehavior(self, QSurfaceFormat_SwapBehavior): # real signature unknown; restored from __doc__
        """ setSwapBehavior(self, QSurfaceFormat.SwapBehavior) """
        pass

    def setSwapInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setSwapInterval(self, int) """
        pass

    def setVersion(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setVersion(self, int, int) """
        pass

    def stencilBufferSize(self): # real signature unknown; restored from __doc__
        """ stencilBufferSize(self) -> int """
        return 0

    def stereo(self): # real signature unknown; restored from __doc__
        """ stereo(self) -> bool """
        return False

    def swapBehavior(self): # real signature unknown; restored from __doc__
        """ swapBehavior(self) -> QSurfaceFormat.SwapBehavior """
        pass

    def swapInterval(self): # real signature unknown; restored from __doc__
        """ swapInterval(self) -> int """
        return 0

    def testOption(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        testOption(self, QSurfaceFormat.FormatOptions) -> bool
        testOption(self, QSurfaceFormat.FormatOption) -> bool
        """
        return False

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> Tuple[int, int] """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CompatibilityProfile = 2
    CoreProfile = 1
    DebugContext = 2
    DefaultRenderableType = 0
    DefaultSwapBehavior = 0
    DeprecatedFunctions = 4
    DoubleBuffer = 2
    NoProfile = 0
    OpenGL = 1
    OpenGLES = 2
    OpenVG = 4
    ResetNotification = 8
    SingleBuffer = 1
    StereoBuffers = 1
    TripleBuffer = 3
    __hash__ = None


