# encoding: utf-8
# module PyQt5.QtSensors
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QSensor import QSensor

class QLightSensor(QSensor):
    """ QLightSensor(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def fieldOfView(self): # real signature unknown; restored from __doc__
        """ fieldOfView(self) -> float """
        return 0.0

    def fieldOfViewChanged(self, p_float): # real signature unknown; restored from __doc__
        """ fieldOfViewChanged(self, float) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QLightReading """
        return QLightReading

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFieldOfView(self, p_float): # real signature unknown; restored from __doc__
        """ setFieldOfView(self, float) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

