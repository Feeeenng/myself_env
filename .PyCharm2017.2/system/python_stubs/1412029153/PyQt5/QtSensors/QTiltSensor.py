# encoding: utf-8
# module PyQt5.QtSensors
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QSensor import QSensor

class QTiltSensor(QSensor):
    """ QTiltSensor(parent: QObject = None) """
    def calibrate(self): # real signature unknown; restored from __doc__
        """ calibrate(self) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QTiltReading """
        return QTiltReading

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


