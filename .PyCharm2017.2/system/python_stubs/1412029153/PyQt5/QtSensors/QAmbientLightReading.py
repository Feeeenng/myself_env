# encoding: utf-8
# module PyQt5.QtSensors
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QSensorReading import QSensorReading

class QAmbientLightReading(QSensorReading):
    # no doc
    def lightLevel(self): # real signature unknown; restored from __doc__
        """ lightLevel(self) -> QAmbientLightReading.LightLevel """
        pass

    def setLightLevel(self, QAmbientLightReading_LightLevel): # real signature unknown; restored from __doc__
        """ setLightLevel(self, QAmbientLightReading.LightLevel) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Bright = 4
    Dark = 1
    Light = 3
    Sunny = 5
    Twilight = 2
    Undefined = 0


