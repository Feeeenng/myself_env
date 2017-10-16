# encoding: utf-8
# module PyQt5.QtNetwork
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QHostAddress(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QHostAddress()
    QHostAddress(QHostAddress.SpecialAddress)
    QHostAddress(int)
    QHostAddress(str)
    QHostAddress(Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int])
    QHostAddress(Union[QHostAddress, QHostAddress.SpecialAddress])
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def isInSubnet(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isInSubnet(self, Union[QHostAddress, QHostAddress.SpecialAddress], int) -> bool
        isInSubnet(self, object) -> bool
        """
        return False

    def isLoopback(self): # real signature unknown; restored from __doc__
        """ isLoopback(self) -> bool """
        return False

    def isMulticast(self): # real signature unknown; restored from __doc__
        """ isMulticast(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def parseSubnet(self, p_str): # real signature unknown; restored from __doc__
        """ parseSubnet(str) -> Tuple[QHostAddress, int] """
        pass

    def protocol(self): # real signature unknown; restored from __doc__
        """ protocol(self) -> QAbstractSocket.NetworkLayerProtocol """
        pass

    def scopeId(self): # real signature unknown; restored from __doc__
        """ scopeId(self) -> str """
        return ""

    def setAddress(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAddress(self, int)
        setAddress(self, str) -> bool
        setAddress(self, Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int])
        """
        return False

    def setScopeId(self, p_str): # real signature unknown; restored from __doc__
        """ setScopeId(self, str) """
        pass

    def swap(self, QHostAddress): # real signature unknown; restored from __doc__
        """ swap(self, QHostAddress) """
        pass

    def toIPv4Address(self): # real signature unknown; restored from __doc__
        """ toIPv4Address(self) -> int """
        return 0

    def toIPv6Address(self): # real signature unknown; restored from __doc__
        """ toIPv6Address(self) -> Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int] """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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


    Any = 4
    AnyIPv4 = 6
    AnyIPv6 = 5
    Broadcast = 1
    LocalHost = 2
    LocalHostIPv6 = 3
    Null = 0


