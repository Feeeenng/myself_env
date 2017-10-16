# encoding: utf-8
# module PyQt5.QtQuick
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml


class QSGMaterial(): # skipped bases: <class 'sip.wrapper'>
    """ QSGMaterial() """
    def compare(self, QSGMaterial): # real signature unknown; restored from __doc__
        """ compare(self, QSGMaterial) -> int """
        return 0

    def createShader(self): # real signature unknown; restored from __doc__
        """ createShader(self) -> QSGMaterialShader """
        return QSGMaterialShader

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QSGMaterial.Flags """
        pass

    def setFlag(self, QSGMaterial_Flags, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, QSGMaterial.Flags, enabled: bool = True) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QSGMaterialType """
        return QSGMaterialType

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Blending = 1
    CustomCompileStep = 16
    RequiresDeterminant = 2
    RequiresFullMatrix = 14
    RequiresFullMatrixExceptTranslate = 6


