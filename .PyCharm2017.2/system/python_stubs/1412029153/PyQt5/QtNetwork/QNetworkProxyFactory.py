# encoding: utf-8
# module PyQt5.QtNetwork
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QNetworkProxyFactory(): # skipped bases: <class 'sip.wrapper'>
    """
    QNetworkProxyFactory()
    QNetworkProxyFactory(QNetworkProxyFactory)
    """
    def proxyForQuery(self, QNetworkProxyQuery): # real signature unknown; restored from __doc__
        """ proxyForQuery(QNetworkProxyQuery) -> List[QNetworkProxy] """
        return []

    def queryProxy(self, query=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ queryProxy(self, query: QNetworkProxyQuery = QNetworkProxyQuery()) -> object """
        pass

    def setApplicationProxyFactory(self, QNetworkProxyFactory): # real signature unknown; restored from __doc__
        """ setApplicationProxyFactory(QNetworkProxyFactory) """
        pass

    def setUseSystemConfiguration(self, bool): # real signature unknown; restored from __doc__
        """ setUseSystemConfiguration(bool) """
        pass

    def systemProxyForQuery(self, query=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ systemProxyForQuery(query: QNetworkProxyQuery = QNetworkProxyQuery()) -> List[QNetworkProxy] """
        pass

    def __init__(self, QNetworkProxyFactory=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



