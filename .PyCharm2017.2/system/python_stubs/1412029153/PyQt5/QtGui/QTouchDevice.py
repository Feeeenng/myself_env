# encoding: utf-8
# module PyQt5.QtGui
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QTouchDevice(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QTouchDevice()
    QTouchDevice(QTouchDevice)
    """
    def capabilities(self): # real signature unknown; restored from __doc__
        """ capabilities(self) -> QTouchDevice.Capabilities """
        pass

    def devices(self): # real signature unknown; restored from __doc__
        """ devices() -> object """
        return object()

    def maximumTouchPoints(self): # real signature unknown; restored from __doc__
        """ maximumTouchPoints(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def setCapabilities(self, QTouchDevice_Capabilities): # real signature unknown; restored from __doc__
        """ setCapabilities(self, QTouchDevice.Capabilities) """
        pass

    def setMaximumTouchPoints(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumTouchPoints(self, int) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def setType(self, QTouchDevice_DeviceType): # real signature unknown; restored from __doc__
        """ setType(self, QTouchDevice.DeviceType) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QTouchDevice.DeviceType """
        pass

    def __init__(self, QTouchDevice=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Area = 2
    MouseEmulation = 64
    NormalizedPosition = 32
    Position = 1
    Pressure = 4
    RawPositions = 16
    TouchPad = 1
    TouchScreen = 0
    Velocity = 8

