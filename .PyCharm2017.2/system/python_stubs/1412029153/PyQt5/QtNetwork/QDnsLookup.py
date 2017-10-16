# encoding: utf-8
# module PyQt5.QtNetwork
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QDnsLookup(__PyQt5_QtCore.QObject):
    """
    QDnsLookup(parent: QObject = None)
    QDnsLookup(QDnsLookup.Type, str, parent: QObject = None)
    QDnsLookup(QDnsLookup.Type, str, Union[QHostAddress, QHostAddress.SpecialAddress], parent: QObject = None)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def canonicalNameRecords(self): # real signature unknown; restored from __doc__
        """ canonicalNameRecords(self) -> object """
        return object()

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QDnsLookup.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def hostAddressRecords(self): # real signature unknown; restored from __doc__
        """ hostAddressRecords(self) -> object """
        return object()

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self): # real signature unknown; restored from __doc__
        """ lookup(self) """
        pass

    def mailExchangeRecords(self): # real signature unknown; restored from __doc__
        """ mailExchangeRecords(self) -> object """
        return object()

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nameChanged(self, p_str): # real signature unknown; restored from __doc__
        """ nameChanged(self, str) [signal] """
        pass

    def nameserver(self): # real signature unknown; restored from __doc__
        """ nameserver(self) -> QHostAddress """
        return QHostAddress

    def nameserverChanged(self, Union, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ nameserverChanged(self, Union[QHostAddress, QHostAddress.SpecialAddress]) [signal] """
        pass

    def nameServerRecords(self): # real signature unknown; restored from __doc__
        """ nameServerRecords(self) -> List[QDnsDomainNameRecord] """
        return []

    def pointerRecords(self): # real signature unknown; restored from __doc__
        """ pointerRecords(self) -> List[QDnsDomainNameRecord] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serviceRecords(self): # real signature unknown; restored from __doc__
        """ serviceRecords(self) -> object """
        return object()

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def setNameserver(self, Union, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setNameserver(self, Union[QHostAddress, QHostAddress.SpecialAddress]) """
        pass

    def setType(self, QDnsLookup_Type): # real signature unknown; restored from __doc__
        """ setType(self, QDnsLookup.Type) """
        pass

    def textRecords(self): # real signature unknown; restored from __doc__
        """ textRecords(self) -> object """
        return object()

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QDnsLookup.Type """
        pass

    def typeChanged(self, QDnsLookup_Type): # real signature unknown; restored from __doc__
        """ typeChanged(self, QDnsLookup.Type) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    A = 1
    AAAA = 28
    ANY = 255
    CNAME = 5
    InvalidReplyError = 4
    InvalidRequestError = 3
    MX = 15
    NoError = 0
    NotFoundError = 7
    NS = 2
    OperationCancelledError = 2
    PTR = 12
    ResolverError = 1
    ServerFailureError = 5
    ServerRefusedError = 6
    SRV = 33
    TXT = 16


