# encoding: utf-8
# module PyQt5.Enginio
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\Enginio.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


# no functions
# classes

class Enginio(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessControlOperation = 1
    Authenticated = 2
    Authenticating = 1
    AuthenticationFailure = 3
    BackendError = 2
    CreatedAtRole = 258
    CustomPropertyRole = 266
    FileOperation = 5
    IdRole = 260
    JsonObjectRole = 262
    NetworkError = 1
    NoError = 0
    NotAuthenticated = 0
    ObjectOperation = 0
    ObjectTypeRole = 261
    SyncedRole = 257
    UpdatedAtRole = 259
    UsergroupMembersOperation = 4
    UsergroupOperation = 3
    UserOperation = 2


class EnginioClientConnection(__PyQt5_QtCore.QObject):
    # no doc
    def authenticationState(self): # real signature unknown; restored from __doc__
        """ authenticationState(self) -> Enginio.AuthenticationState """
        pass

    def authenticationStateChanged(self, Enginio_AuthenticationState): # real signature unknown; restored from __doc__
        """ authenticationStateChanged(self, Enginio.AuthenticationState) [signal] """
        pass

    def backendId(self): # real signature unknown; restored from __doc__
        """ backendId(self) -> QByteArray """
        pass

    def backendIdChanged(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ backendIdChanged(self, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def identity(self): # real signature unknown; restored from __doc__
        """ identity(self) -> EnginioIdentity """
        return EnginioIdentity

    def identityChanged(self, EnginioIdentity): # real signature unknown; restored from __doc__
        """ identityChanged(self, EnginioIdentity) [signal] """
        pass

    def networkManager(self): # real signature unknown; restored from __doc__
        """ networkManager(self) -> QNetworkAccessManager """
        pass

    def serviceUrl(self): # real signature unknown; restored from __doc__
        """ serviceUrl(self) -> QUrl """
        pass

    def serviceUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ serviceUrlChanged(self, QUrl) [signal] """
        pass

    def setBackendId(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setBackendId(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setIdentity(self, EnginioIdentity): # real signature unknown; restored from __doc__
        """ setIdentity(self, EnginioIdentity) """
        pass

    def setServiceUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setServiceUrl(self, QUrl) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class EnginioClient(EnginioClientConnection):
    """ EnginioClient(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, Dict, p_str=None, QJsonValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ create(self, Dict[str, QJsonValue], operation: Enginio.Operation = Enginio.ObjectOperation) -> EnginioReply """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def downloadUrl(self, Dict, p_str=None, QJsonValue=None): # real signature unknown; restored from __doc__
        """ downloadUrl(self, Dict[str, QJsonValue]) -> EnginioReply """
        return EnginioReply

    def error(self, EnginioReply): # real signature unknown; restored from __doc__
        """ error(self, EnginioReply) [signal] """
        pass

    def finished(self, EnginioReply): # real signature unknown; restored from __doc__
        """ finished(self, EnginioReply) [signal] """
        pass

    def fullTextSearch(self, Dict, p_str=None, QJsonValue=None): # real signature unknown; restored from __doc__
        """ fullTextSearch(self, Dict[str, QJsonValue]) -> EnginioReply """
        return EnginioReply

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def query(self, Dict, p_str=None, QJsonValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ query(self, Dict[str, QJsonValue], operation: Enginio.Operation = Enginio.ObjectOperation) -> EnginioReply """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, Dict, p_str=None, QJsonValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ remove(self, Dict[str, QJsonValue], operation: Enginio.Operation = Enginio.ObjectOperation) -> EnginioReply """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sessionAuthenticated(self, EnginioReply): # real signature unknown; restored from __doc__
        """ sessionAuthenticated(self, EnginioReply) [signal] """
        pass

    def sessionAuthenticationError(self, EnginioReply): # real signature unknown; restored from __doc__
        """ sessionAuthenticationError(self, EnginioReply) [signal] """
        pass

    def sessionTerminated(self): # real signature unknown; restored from __doc__
        """ sessionTerminated(self) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, Dict, p_str=None, QJsonValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ update(self, Dict[str, QJsonValue], operation: Enginio.Operation = Enginio.ObjectOperation) -> EnginioReply """
        pass

    def uploadFile(self, Dict, p_str=None, QJsonValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ uploadFile(self, Dict[str, QJsonValue], QUrl) -> EnginioReply """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class EnginioIdentity(__PyQt5_QtCore.QObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class EnginioModel(__PyQt5_QtCore.QAbstractListModel):
    """ EnginioModel(parent: QObject = None) """
    def append(self, Dict, p_str=None, QJsonValue=None): # real signature unknown; restored from __doc__
        """ append(self, Dict[str, QJsonValue]) -> EnginioReply """
        return EnginioReply

    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def client(self): # real signature unknown; restored from __doc__
        """ client(self) -> EnginioClient """
        return EnginioClient

    def clientChanged(self, EnginioClient): # real signature unknown; restored from __doc__
        """ clientChanged(self, EnginioClient) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def operation(self): # real signature unknown; restored from __doc__
        """ operation(self) -> Enginio.Operation """
        pass

    def operationChanged(self, Enginio_Operation): # real signature unknown; restored from __doc__
        """ operationChanged(self, Enginio.Operation) [signal] """
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> Dict[str, QJsonValue] """
        return {}

    def queryChanged(self, Dict, p_str=None, QJsonValue=None): # real signature unknown; restored from __doc__
        """ queryChanged(self, Dict[str, QJsonValue]) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ reload(self) -> EnginioReply """
        return EnginioReply

    def remove(self, p_int): # real signature unknown; restored from __doc__
        """ remove(self, int) -> EnginioReply """
        return EnginioReply

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setClient(self, EnginioClient): # real signature unknown; restored from __doc__
        """ setClient(self, EnginioClient) """
        pass

    def setData(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setData(self, int, Any, str) -> EnginioReply
        setData(self, int, Dict[str, QJsonValue]) -> EnginioReply
        """
        return EnginioReply

    def setOperation(self, Enginio_Operation): # real signature unknown; restored from __doc__
        """ setOperation(self, Enginio.Operation) """
        pass

    def setQuery(self, Dict, p_str=None, QJsonValue=None): # real signature unknown; restored from __doc__
        """ setQuery(self, Dict[str, QJsonValue]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class EnginioOAuth2Authentication(EnginioIdentity):
    """ EnginioOAuth2Authentication(parent: QObject = None) """
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

    def password(self): # real signature unknown; restored from __doc__
        """ password(self) -> str """
        return ""

    def passwordChanged(self, p_str): # real signature unknown; restored from __doc__
        """ passwordChanged(self, str) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setPassword(self, p_str): # real signature unknown; restored from __doc__
        """ setPassword(self, str) """
        pass

    def setUser(self, p_str): # real signature unknown; restored from __doc__
        """ setUser(self, str) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def user(self): # real signature unknown; restored from __doc__
        """ user(self) -> str """
        return ""

    def userChanged(self, p_str): # real signature unknown; restored from __doc__
        """ userChanged(self, str) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class EnginioReply(__PyQt5_QtCore.QObject):
    # no doc
    def backendStatus(self): # real signature unknown; restored from __doc__
        """ backendStatus(self) -> int """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> Dict[str, QJsonValue] """
        return {}

    def dataChanged(self): # real signature unknown; restored from __doc__
        """ dataChanged(self) [signal] """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def errorType(self): # real signature unknown; restored from __doc__
        """ errorType(self) -> Enginio.ErrorType """
        pass

    def finished(self, EnginioReply): # real signature unknown; restored from __doc__
        """ finished(self, EnginioReply) [signal] """
        pass

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def networkError(self): # real signature unknown; restored from __doc__
        """ networkError(self) -> QNetworkReply.NetworkError """
        pass

    def progress(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ progress(self, int, int) [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values



