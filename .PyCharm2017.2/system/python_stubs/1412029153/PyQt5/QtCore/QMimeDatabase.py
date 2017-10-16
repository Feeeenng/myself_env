# encoding: utf-8
# module PyQt5.QtCore
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


class QMimeDatabase(): # skipped bases: <class 'sip.simplewrapper'>
    """ QMimeDatabase() """
    def allMimeTypes(self): # real signature unknown; restored from __doc__
        """ allMimeTypes(self) -> List[QMimeType] """
        return []

    def mimeTypeForData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mimeTypeForData(self, Union[QByteArray, bytes, bytearray]) -> QMimeType
        mimeTypeForData(self, QIODevice) -> QMimeType
        """
        return QMimeType

    def mimeTypeForFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mimeTypeForFile(self, str, mode: QMimeDatabase.MatchMode = QMimeDatabase.MatchDefault) -> QMimeType
        mimeTypeForFile(self, QFileInfo, mode: QMimeDatabase.MatchMode = QMimeDatabase.MatchDefault) -> QMimeType
        """
        return QMimeType

    def mimeTypeForFileNameAndData(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mimeTypeForFileNameAndData(self, str, QIODevice) -> QMimeType
        mimeTypeForFileNameAndData(self, str, Union[QByteArray, bytes, bytearray]) -> QMimeType
        """
        return QMimeType

    def mimeTypeForName(self, p_str): # real signature unknown; restored from __doc__
        """ mimeTypeForName(self, str) -> QMimeType """
        return QMimeType

    def mimeTypeForUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ mimeTypeForUrl(self, QUrl) -> QMimeType """
        return QMimeType

    def mimeTypesForFileName(self, p_str): # real signature unknown; restored from __doc__
        """ mimeTypesForFileName(self, str) -> object """
        return object()

    def suffixForFileName(self, p_str): # real signature unknown; restored from __doc__
        """ suffixForFileName(self, str) -> str """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    MatchContent = 2
    MatchDefault = 0
    MatchExtension = 1


