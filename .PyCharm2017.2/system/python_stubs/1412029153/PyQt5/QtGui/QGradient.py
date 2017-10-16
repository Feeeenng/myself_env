# encoding: utf-8
# module PyQt5.QtGui
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QGradient(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QGradient()
    QGradient(QGradient)
    """
    def coordinateMode(self): # real signature unknown; restored from __doc__
        """ coordinateMode(self) -> QGradient.CoordinateMode """
        pass

    def setColorAt(self, p_float, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setColorAt(self, float, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCoordinateMode(self, QGradient_CoordinateMode): # real signature unknown; restored from __doc__
        """ setCoordinateMode(self, QGradient.CoordinateMode) """
        pass

    def setSpread(self, QGradient_Spread): # real signature unknown; restored from __doc__
        """ setSpread(self, QGradient.Spread) """
        pass

    def setStops(self, p_object): # real signature unknown; restored from __doc__
        """ setStops(self, object) """
        pass

    def spread(self): # real signature unknown; restored from __doc__
        """ spread(self) -> QGradient.Spread """
        pass

    def stops(self): # real signature unknown; restored from __doc__
        """ stops(self) -> object """
        return object()

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QGradient.Type """
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

    def __init__(self, QGradient=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    ConicalGradient = 2
    LinearGradient = 0
    LogicalMode = 0
    NoGradient = 3
    ObjectBoundingMode = 2
    PadSpread = 0
    RadialGradient = 1
    ReflectSpread = 1
    RepeatSpread = 2
    StretchToDeviceMode = 1
    __hash__ = None


