# encoding: utf-8
# module PyQt5.QtNetwork
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QNetworkInterface(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QNetworkInterface()
    QNetworkInterface(QNetworkInterface)
    """
    def addressEntries(self): # real signature unknown; restored from __doc__
        """ addressEntries(self) -> object """
        return object()

    def allAddresses(self): # real signature unknown; restored from __doc__
        """ allAddresses() -> List[QHostAddress] """
        return []

    def allInterfaces(self): # real signature unknown; restored from __doc__
        """ allInterfaces() -> object """
        return object()

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QNetworkInterface.InterfaceFlags """
        pass

    def hardwareAddress(self): # real signature unknown; restored from __doc__
        """ hardwareAddress(self) -> str """
        return ""

    def humanReadableName(self): # real signature unknown; restored from __doc__
        """ humanReadableName(self) -> str """
        return ""

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> int """
        return 0

    def interfaceFromIndex(self, p_int): # real signature unknown; restored from __doc__
        """ interfaceFromIndex(int) -> QNetworkInterface """
        return QNetworkInterface

    def interfaceFromName(self, p_str): # real signature unknown; restored from __doc__
        """ interfaceFromName(str) -> QNetworkInterface """
        return QNetworkInterface

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def swap(self, QNetworkInterface): # real signature unknown; restored from __doc__
        """ swap(self, QNetworkInterface) """
        pass

    def __init__(self, QNetworkInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CanBroadcast = 4
    CanMulticast = 32
    IsLoopBack = 8
    IsPointToPoint = 16
    IsRunning = 2
    IsUp = 1


