# encoding: utf-8
# module PyQt5.QtNetwork
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


class QNetworkAccessManager(__PyQt5_QtCore.QObject):
    """ QNetworkAccessManager(parent: QObject = None) """
    def activeConfiguration(self): # real signature unknown; restored from __doc__
        """ activeConfiguration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def authenticationRequired(self, QNetworkReply, QAuthenticator): # real signature unknown; restored from __doc__
        """ authenticationRequired(self, QNetworkReply, QAuthenticator) [signal] """
        pass

    def cache(self): # real signature unknown; restored from __doc__
        """ cache(self) -> QAbstractNetworkCache """
        return QAbstractNetworkCache

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearAccessCache(self): # real signature unknown; restored from __doc__
        """ clearAccessCache(self) """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ configuration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHost(self, p_str, port=80): # real signature unknown; restored from __doc__
        """ connectToHost(self, str, port: int = 80) """
        pass

    def connectToHostEncrypted(self, p_str, port=443, sslConfiguration=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ connectToHostEncrypted(self, str, port: int = 443, sslConfiguration: QSslConfiguration = QSslConfiguration.defaultConfiguration()) """
        pass

    def cookieJar(self): # real signature unknown; restored from __doc__
        """ cookieJar(self) -> QNetworkCookieJar """
        return QNetworkCookieJar

    def createRequest(self, QNetworkAccessManager_Operation, QNetworkRequest, device=None): # real signature unknown; restored from __doc__
        """ createRequest(self, QNetworkAccessManager.Operation, QNetworkRequest, device: QIODevice = None) -> QNetworkReply """
        return QNetworkReply

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deleteResource(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ deleteResource(self, QNetworkRequest) -> QNetworkReply """
        return QNetworkReply

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encrypted(self, QNetworkReply): # real signature unknown; restored from __doc__
        """ encrypted(self, QNetworkReply) [signal] """
        pass

    def finished(self, QNetworkReply): # real signature unknown; restored from __doc__
        """ finished(self, QNetworkReply) [signal] """
        pass

    def get(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ get(self, QNetworkRequest) -> QNetworkReply """
        return QNetworkReply

    def head(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ head(self, QNetworkRequest) -> QNetworkReply """
        return QNetworkReply

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def networkAccessible(self): # real signature unknown; restored from __doc__
        """ networkAccessible(self) -> QNetworkAccessManager.NetworkAccessibility """
        pass

    def networkAccessibleChanged(self, QNetworkAccessManager_NetworkAccessibility): # real signature unknown; restored from __doc__
        """ networkAccessibleChanged(self, QNetworkAccessManager.NetworkAccessibility) [signal] """
        pass

    def post(self, QNetworkRequest, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        post(self, QNetworkRequest, QIODevice) -> QNetworkReply
        post(self, QNetworkRequest, Union[QByteArray, bytes, bytearray]) -> QNetworkReply
        post(self, QNetworkRequest, QHttpMultiPart) -> QNetworkReply
        """
        return QNetworkReply

    def preSharedKeyAuthenticationRequired(self, QNetworkReply, QSslPreSharedKeyAuthenticator): # real signature unknown; restored from __doc__
        """ preSharedKeyAuthenticationRequired(self, QNetworkReply, QSslPreSharedKeyAuthenticator) [signal] """
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        return QNetworkProxy

    def proxyAuthenticationRequired(self, QNetworkProxy, QAuthenticator): # real signature unknown; restored from __doc__
        """ proxyAuthenticationRequired(self, QNetworkProxy, QAuthenticator) [signal] """
        pass

    def proxyFactory(self): # real signature unknown; restored from __doc__
        """ proxyFactory(self) -> QNetworkProxyFactory """
        return QNetworkProxyFactory

    def put(self, QNetworkRequest, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        put(self, QNetworkRequest, QIODevice) -> QNetworkReply
        put(self, QNetworkRequest, Union[QByteArray, bytes, bytearray]) -> QNetworkReply
        put(self, QNetworkRequest, QHttpMultiPart) -> QNetworkReply
        """
        return QNetworkReply

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sendCustomRequest(self, QNetworkRequest, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sendCustomRequest(self, QNetworkRequest, Union[QByteArray, bytes, bytearray], data: QIODevice = None) -> QNetworkReply """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCache(self, QAbstractNetworkCache): # real signature unknown; restored from __doc__
        """ setCache(self, QAbstractNetworkCache) """
        pass

    def setConfiguration(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ setConfiguration(self, QNetworkConfiguration) """
        pass

    def setCookieJar(self, QNetworkCookieJar): # real signature unknown; restored from __doc__
        """ setCookieJar(self, QNetworkCookieJar) """
        pass

    def setNetworkAccessible(self, QNetworkAccessManager_NetworkAccessibility): # real signature unknown; restored from __doc__
        """ setNetworkAccessible(self, QNetworkAccessManager.NetworkAccessibility) """
        pass

    def setProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, QNetworkProxy) """
        pass

    def setProxyFactory(self, QNetworkProxyFactory): # real signature unknown; restored from __doc__
        """ setProxyFactory(self, QNetworkProxyFactory) """
        pass

    def sslErrors(self, QNetworkReply, p_object): # real signature unknown; restored from __doc__
        """ sslErrors(self, QNetworkReply, object) [signal] """
        pass

    def supportedSchemes(self): # real signature unknown; restored from __doc__
        """ supportedSchemes(self) -> List[str] """
        return []

    def supportedSchemesImplementation(self): # real signature unknown; restored from __doc__
        """ supportedSchemesImplementation(self) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Accessible = 1
    CustomOperation = 6
    DeleteOperation = 5
    GetOperation = 2
    HeadOperation = 1
    NotAccessible = 0
    PostOperation = 4
    PutOperation = 3
    UnknownAccessibility = -1


