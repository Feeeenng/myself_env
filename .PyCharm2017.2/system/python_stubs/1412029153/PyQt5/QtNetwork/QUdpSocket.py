# encoding: utf-8
# module PyQt5.QtNetwork
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QAbstractSocket import QAbstractSocket

class QUdpSocket(QAbstractSocket):
    """ QUdpSocket(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hasPendingDatagrams(self): # real signature unknown; restored from __doc__
        """ hasPendingDatagrams(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def joinMulticastGroup(self, Union, QHostAddress=None, QHostAddress_SpecialAddress=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        joinMulticastGroup(self, Union[QHostAddress, QHostAddress.SpecialAddress]) -> bool
        joinMulticastGroup(self, Union[QHostAddress, QHostAddress.SpecialAddress], QNetworkInterface) -> bool
        """
        return False

    def leaveMulticastGroup(self, Union, QHostAddress=None, QHostAddress_SpecialAddress=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        leaveMulticastGroup(self, Union[QHostAddress, QHostAddress.SpecialAddress]) -> bool
        leaveMulticastGroup(self, Union[QHostAddress, QHostAddress.SpecialAddress], QNetworkInterface) -> bool
        """
        return False

    def multicastInterface(self): # real signature unknown; restored from __doc__
        """ multicastInterface(self) -> QNetworkInterface """
        return QNetworkInterface

    def pendingDatagramSize(self): # real signature unknown; restored from __doc__
        """ pendingDatagramSize(self) -> int """
        return 0

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readDatagram(self, p_int): # real signature unknown; restored from __doc__
        """ readDatagram(self, int) -> Tuple[bytes, QHostAddress, int] """
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalPort(self, *args, **kwargs): # real signature unknown
        pass

    def setMulticastInterface(self, QNetworkInterface): # real signature unknown; restored from __doc__
        """ setMulticastInterface(self, QNetworkInterface) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerName(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerPort(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketError(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketState(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def writeDatagram(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeDatagram(self, bytes, Union[QHostAddress, QHostAddress.SpecialAddress], int) -> int
        writeDatagram(self, Union[QByteArray, bytes, bytearray], Union[QHostAddress, QHostAddress.SpecialAddress], int) -> int
        """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


