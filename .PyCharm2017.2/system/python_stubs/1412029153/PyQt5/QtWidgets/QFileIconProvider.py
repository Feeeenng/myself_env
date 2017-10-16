# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui


class QFileIconProvider(): # skipped bases: <class 'sip.simplewrapper'>
    """ QFileIconProvider() """
    def icon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        icon(self, QFileIconProvider.IconType) -> QIcon
        icon(self, QFileInfo) -> QIcon
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QFileIconProvider.Options """
        pass

    def setOptions(self, QFileIconProvider_Options): # real signature unknown; restored from __doc__
        """ setOptions(self, QFileIconProvider.Options) """
        pass

    def type(self, QFileInfo): # real signature unknown; restored from __doc__
        """ type(self, QFileInfo) -> str """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Computer = 0
    Desktop = 1
    DontUseCustomDirectoryIcons = 1
    Drive = 4
    File = 6
    Folder = 5
    Network = 3
    Trashcan = 2


