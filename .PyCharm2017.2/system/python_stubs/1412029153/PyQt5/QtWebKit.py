# encoding: utf-8
# module PyQt5.QtWebKit
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtWebKit.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


# functions

def qWebKitMajorVersion(): # real signature unknown; restored from __doc__
    """ qWebKitMajorVersion() -> int """
    return 0

def qWebKitMinorVersion(): # real signature unknown; restored from __doc__
    """ qWebKitMinorVersion() -> int """
    return 0

def qWebKitVersion(): # real signature unknown; restored from __doc__
    """ qWebKitVersion() -> str """
    return ""

# classes

class QWebDatabase(): # skipped bases: <class 'sip.simplewrapper'>
    """ QWebDatabase(QWebDatabase) """
    def displayName(self): # real signature unknown; restored from __doc__
        """ displayName(self) -> str """
        return ""

    def expectedSize(self): # real signature unknown; restored from __doc__
        """ expectedSize(self) -> int """
        return 0

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> QWebSecurityOrigin """
        return QWebSecurityOrigin

    def removeAllDatabases(self): # real signature unknown; restored from __doc__
        """ removeAllDatabases() """
        pass

    def removeDatabase(self, QWebDatabase): # real signature unknown; restored from __doc__
        """ removeDatabase(QWebDatabase) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def __init__(self, QWebDatabase): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebElement(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QWebElement()
    QWebElement(QWebElement)
    """
    def addClass(self, p_str): # real signature unknown; restored from __doc__
        """ addClass(self, str) """
        pass

    def appendInside(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        appendInside(self, str)
        appendInside(self, QWebElement)
        """
        pass

    def appendOutside(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        appendOutside(self, str)
        appendOutside(self, QWebElement)
        """
        pass

    def attribute(self, p_str, defaultValue=''): # real signature unknown; restored from __doc__
        """ attribute(self, str, defaultValue: str = '') -> str """
        return ""

    def attributeNames(self, namespaceUri=''): # real signature unknown; restored from __doc__
        """ attributeNames(self, namespaceUri: str = '') -> List[str] """
        return []

    def attributeNS(self, p_str, p_str_1, defaultValue=''): # real signature unknown; restored from __doc__
        """ attributeNS(self, str, str, defaultValue: str = '') -> str """
        return ""

    def classes(self): # real signature unknown; restored from __doc__
        """ classes(self) -> List[str] """
        return []

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> QWebElement """
        return QWebElement

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> QWebElement """
        return QWebElement

    def encloseContentsWith(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        encloseContentsWith(self, QWebElement)
        encloseContentsWith(self, str)
        """
        pass

    def encloseWith(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        encloseWith(self, str)
        encloseWith(self, QWebElement)
        """
        pass

    def evaluateJavaScript(self, p_str): # real signature unknown; restored from __doc__
        """ evaluateJavaScript(self, str) -> Any """
        pass

    def findAll(self, p_str): # real signature unknown; restored from __doc__
        """ findAll(self, str) -> QWebElementCollection """
        return QWebElementCollection

    def findFirst(self, p_str): # real signature unknown; restored from __doc__
        """ findFirst(self, str) -> QWebElement """
        return QWebElement

    def firstChild(self): # real signature unknown; restored from __doc__
        """ firstChild(self) -> QWebElement """
        return QWebElement

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def hasAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ hasAttribute(self, str) -> bool """
        return False

    def hasAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ hasAttributeNS(self, str, str) -> bool """
        return False

    def hasAttributes(self): # real signature unknown; restored from __doc__
        """ hasAttributes(self) -> bool """
        return False

    def hasClass(self, p_str): # real signature unknown; restored from __doc__
        """ hasClass(self, str) -> bool """
        return False

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def lastChild(self): # real signature unknown; restored from __doc__
        """ lastChild(self) -> QWebElement """
        return QWebElement

    def localName(self): # real signature unknown; restored from __doc__
        """ localName(self) -> str """
        return ""

    def namespaceUri(self): # real signature unknown; restored from __doc__
        """ namespaceUri(self) -> str """
        return ""

    def nextSibling(self): # real signature unknown; restored from __doc__
        """ nextSibling(self) -> QWebElement """
        return QWebElement

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QWebElement """
        return QWebElement

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def prependInside(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        prependInside(self, str)
        prependInside(self, QWebElement)
        """
        pass

    def prependOutside(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        prependOutside(self, str)
        prependOutside(self, QWebElement)
        """
        pass

    def previousSibling(self): # real signature unknown; restored from __doc__
        """ previousSibling(self) -> QWebElement """
        return QWebElement

    def removeAllChildren(self): # real signature unknown; restored from __doc__
        """ removeAllChildren(self) """
        pass

    def removeAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ removeAttribute(self, str) """
        pass

    def removeAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ removeAttributeNS(self, str, str) """
        pass

    def removeClass(self, p_str): # real signature unknown; restored from __doc__
        """ removeClass(self, str) """
        pass

    def removeFromDocument(self): # real signature unknown; restored from __doc__
        """ removeFromDocument(self) """
        pass

    def render(self, QPainter, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        render(self, QPainter)
        render(self, QPainter, QRect)
        """
        pass

    def replace(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        replace(self, str)
        replace(self, QWebElement)
        """
        pass

    def setAttribute(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ setAttribute(self, str, str) """
        pass

    def setAttributeNS(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ setAttributeNS(self, str, str, str) """
        pass

    def setFocus(self): # real signature unknown; restored from __doc__
        """ setFocus(self) """
        pass

    def setInnerXml(self, p_str): # real signature unknown; restored from __doc__
        """ setInnerXml(self, str) """
        pass

    def setOuterXml(self, p_str): # real signature unknown; restored from __doc__
        """ setOuterXml(self, str) """
        pass

    def setPlainText(self, p_str): # real signature unknown; restored from __doc__
        """ setPlainText(self, str) """
        pass

    def setStyleProperty(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ setStyleProperty(self, str, str) """
        pass

    def styleProperty(self, p_str, QWebElement_StyleResolveStrategy): # real signature unknown; restored from __doc__
        """ styleProperty(self, str, QWebElement.StyleResolveStrategy) -> str """
        return ""

    def tagName(self): # real signature unknown; restored from __doc__
        """ tagName(self) -> str """
        return ""

    def takeFromDocument(self): # real signature unknown; restored from __doc__
        """ takeFromDocument(self) -> QWebElement """
        return QWebElement

    def toggleClass(self, p_str): # real signature unknown; restored from __doc__
        """ toggleClass(self, str) """
        pass

    def toInnerXml(self): # real signature unknown; restored from __doc__
        """ toInnerXml(self) -> str """
        return ""

    def toOuterXml(self): # real signature unknown; restored from __doc__
        """ toOuterXml(self) -> str """
        return ""

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def webFrame(self): # real signature unknown; restored from __doc__
        """ webFrame(self) -> QWebFrame """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QWebElement=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    CascadedStyle = 1
    ComputedStyle = 2
    InlineStyle = 0
    __hash__ = None


class QWebElementCollection(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QWebElementCollection()
    QWebElementCollection(QWebElement, str)
    QWebElementCollection(QWebElementCollection)
    """
    def append(self, QWebElementCollection): # real signature unknown; restored from __doc__
        """ append(self, QWebElementCollection) """
        pass

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ at(self, int) -> QWebElement """
        return QWebElement

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> QWebElement """
        return QWebElement

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> QWebElement """
        return QWebElement

    def toList(self): # real signature unknown; restored from __doc__
        """ toList(self) -> object """
        return object()

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebHistory(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def back(self): # real signature unknown; restored from __doc__
        """ back(self) """
        pass

    def backItem(self): # real signature unknown; restored from __doc__
        """ backItem(self) -> QWebHistoryItem """
        return QWebHistoryItem

    def backItems(self, p_int): # real signature unknown; restored from __doc__
        """ backItems(self, int) -> List[QWebHistoryItem] """
        return []

    def canGoBack(self): # real signature unknown; restored from __doc__
        """ canGoBack(self) -> bool """
        return False

    def canGoForward(self): # real signature unknown; restored from __doc__
        """ canGoForward(self) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> QWebHistoryItem """
        return QWebHistoryItem

    def currentItemIndex(self): # real signature unknown; restored from __doc__
        """ currentItemIndex(self) -> int """
        return 0

    def forward(self): # real signature unknown; restored from __doc__
        """ forward(self) """
        pass

    def forwardItem(self): # real signature unknown; restored from __doc__
        """ forwardItem(self) -> QWebHistoryItem """
        return QWebHistoryItem

    def forwardItems(self, p_int): # real signature unknown; restored from __doc__
        """ forwardItems(self, int) -> List[QWebHistoryItem] """
        return []

    def goToItem(self, QWebHistoryItem): # real signature unknown; restored from __doc__
        """ goToItem(self, QWebHistoryItem) """
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QWebHistoryItem """
        return QWebHistoryItem

    def items(self): # real signature unknown; restored from __doc__
        """ items(self) -> object """
        return object()

    def maximumItemCount(self): # real signature unknown; restored from __doc__
        """ maximumItemCount(self) -> int """
        return 0

    def setMaximumItemCount(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumItemCount(self, int) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebHistoryInterface(__PyQt5_QtCore.QObject):
    """ QWebHistoryInterface(parent: QObject = None) """
    def addHistoryEntry(self, p_str): # real signature unknown; restored from __doc__
        """ addHistoryEntry(self, str) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultInterface(self): # real signature unknown; restored from __doc__
        """ defaultInterface() -> QWebHistoryInterface """
        return QWebHistoryInterface

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def historyContains(self, p_str): # real signature unknown; restored from __doc__
        """ historyContains(self, str) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultInterface(self, QWebHistoryInterface): # real signature unknown; restored from __doc__
        """ setDefaultInterface(QWebHistoryInterface) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWebHistoryItem(): # skipped bases: <class 'sip.simplewrapper'>
    """ QWebHistoryItem(QWebHistoryItem) """
    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastVisited(self): # real signature unknown; restored from __doc__
        """ lastVisited(self) -> QDateTime """
        pass

    def originalUrl(self): # real signature unknown; restored from __doc__
        """ originalUrl(self) -> QUrl """
        pass

    def setUserData(self, Any): # real signature unknown; restored from __doc__
        """ setUserData(self, Any) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def userData(self): # real signature unknown; restored from __doc__
        """ userData(self) -> Any """
        pass

    def __init__(self, QWebHistoryItem): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebPluginFactory(__PyQt5_QtCore.QObject):
    """ QWebPluginFactory(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, p_str, QUrl, Iterable, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ create(self, str, QUrl, Iterable[str], Iterable[str]) -> QObject """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def extension(self, QWebPluginFactory_Extension, option=None, output=None): # real signature unknown; restored from __doc__
        """ extension(self, QWebPluginFactory.Extension, option: QWebPluginFactory.ExtensionOption = None, output: QWebPluginFactory.ExtensionReturn = None) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def plugins(self): # real signature unknown; restored from __doc__
        """ plugins(self) -> object """
        return object()

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refreshPlugins(self): # real signature unknown; restored from __doc__
        """ refreshPlugins(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def supportsExtension(self, QWebPluginFactory_Extension): # real signature unknown; restored from __doc__
        """ supportsExtension(self, QWebPluginFactory.Extension) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass



class QWebSecurityOrigin(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QWebSecurityOrigin(QUrl)
    QWebSecurityOrigin(QWebSecurityOrigin)
    """
    def addAccessWhitelistEntry(self, p_str, p_str_1, QWebSecurityOrigin_SubdomainSetting): # real signature unknown; restored from __doc__
        """ addAccessWhitelistEntry(self, str, str, QWebSecurityOrigin.SubdomainSetting) """
        pass

    def addLocalScheme(self, p_str): # real signature unknown; restored from __doc__
        """ addLocalScheme(str) """
        pass

    def allOrigins(self): # real signature unknown; restored from __doc__
        """ allOrigins() -> object """
        return object()

    def databaseQuota(self): # real signature unknown; restored from __doc__
        """ databaseQuota(self) -> int """
        return 0

    def databases(self): # real signature unknown; restored from __doc__
        """ databases(self) -> object """
        return object()

    def databaseUsage(self): # real signature unknown; restored from __doc__
        """ databaseUsage(self) -> int """
        return 0

    def host(self): # real signature unknown; restored from __doc__
        """ host(self) -> str """
        return ""

    def localSchemes(self): # real signature unknown; restored from __doc__
        """ localSchemes() -> List[str] """
        return []

    def port(self): # real signature unknown; restored from __doc__
        """ port(self) -> int """
        return 0

    def removeAccessWhitelistEntry(self, p_str, p_str_1, QWebSecurityOrigin_SubdomainSetting): # real signature unknown; restored from __doc__
        """ removeAccessWhitelistEntry(self, str, str, QWebSecurityOrigin.SubdomainSetting) """
        pass

    def removeLocalScheme(self, p_str): # real signature unknown; restored from __doc__
        """ removeLocalScheme(str) """
        pass

    def scheme(self): # real signature unknown; restored from __doc__
        """ scheme(self) -> str """
        return ""

    def setApplicationCacheQuota(self, p_int): # real signature unknown; restored from __doc__
        """ setApplicationCacheQuota(self, int) """
        pass

    def setDatabaseQuota(self, p_int): # real signature unknown; restored from __doc__
        """ setDatabaseQuota(self, int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AllowSubdomains = 0
    DisallowSubdomains = 1


class QWebSettings(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def clearIconDatabase(self): # real signature unknown; restored from __doc__
        """ clearIconDatabase() """
        pass

    def clearMemoryCaches(self): # real signature unknown; restored from __doc__
        """ clearMemoryCaches() """
        pass

    def cssMediaType(self): # real signature unknown; restored from __doc__
        """ cssMediaType(self) -> str """
        return ""

    def defaultTextEncoding(self): # real signature unknown; restored from __doc__
        """ defaultTextEncoding(self) -> str """
        return ""

    def enablePersistentStorage(self, path=''): # real signature unknown; restored from __doc__
        """ enablePersistentStorage(path: str = '') """
        pass

    def fontFamily(self, QWebSettings_FontFamily): # real signature unknown; restored from __doc__
        """ fontFamily(self, QWebSettings.FontFamily) -> str """
        return ""

    def fontSize(self, QWebSettings_FontSize): # real signature unknown; restored from __doc__
        """ fontSize(self, QWebSettings.FontSize) -> int """
        return 0

    def globalSettings(self): # real signature unknown; restored from __doc__
        """ globalSettings() -> QWebSettings """
        return QWebSettings

    def iconDatabasePath(self): # real signature unknown; restored from __doc__
        """ iconDatabasePath() -> str """
        return ""

    def iconForUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ iconForUrl(QUrl) -> QIcon """
        pass

    def localStoragePath(self): # real signature unknown; restored from __doc__
        """ localStoragePath(self) -> str """
        return ""

    def maximumPagesInCache(self): # real signature unknown; restored from __doc__
        """ maximumPagesInCache() -> int """
        return 0

    def offlineStorageDefaultQuota(self): # real signature unknown; restored from __doc__
        """ offlineStorageDefaultQuota() -> int """
        return 0

    def offlineStoragePath(self): # real signature unknown; restored from __doc__
        """ offlineStoragePath() -> str """
        return ""

    def offlineWebApplicationCachePath(self): # real signature unknown; restored from __doc__
        """ offlineWebApplicationCachePath() -> str """
        return ""

    def offlineWebApplicationCacheQuota(self): # real signature unknown; restored from __doc__
        """ offlineWebApplicationCacheQuota() -> int """
        return 0

    def resetAttribute(self, QWebSettings_WebAttribute): # real signature unknown; restored from __doc__
        """ resetAttribute(self, QWebSettings.WebAttribute) """
        pass

    def resetFontFamily(self, QWebSettings_FontFamily): # real signature unknown; restored from __doc__
        """ resetFontFamily(self, QWebSettings.FontFamily) """
        pass

    def resetFontSize(self, QWebSettings_FontSize): # real signature unknown; restored from __doc__
        """ resetFontSize(self, QWebSettings.FontSize) """
        pass

    def setAttribute(self, QWebSettings_WebAttribute, bool): # real signature unknown; restored from __doc__
        """ setAttribute(self, QWebSettings.WebAttribute, bool) """
        pass

    def setCSSMediaType(self, p_str): # real signature unknown; restored from __doc__
        """ setCSSMediaType(self, str) """
        pass

    def setDefaultTextEncoding(self, p_str): # real signature unknown; restored from __doc__
        """ setDefaultTextEncoding(self, str) """
        pass

    def setFontFamily(self, QWebSettings_FontFamily, p_str): # real signature unknown; restored from __doc__
        """ setFontFamily(self, QWebSettings.FontFamily, str) """
        pass

    def setFontSize(self, QWebSettings_FontSize, p_int): # real signature unknown; restored from __doc__
        """ setFontSize(self, QWebSettings.FontSize, int) """
        pass

    def setIconDatabasePath(self, p_str): # real signature unknown; restored from __doc__
        """ setIconDatabasePath(str) """
        pass

    def setLocalStoragePath(self, p_str): # real signature unknown; restored from __doc__
        """ setLocalStoragePath(self, str) """
        pass

    def setMaximumPagesInCache(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumPagesInCache(int) """
        pass

    def setObjectCacheCapacities(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ setObjectCacheCapacities(int, int, int) """
        pass

    def setOfflineStorageDefaultQuota(self, p_int): # real signature unknown; restored from __doc__
        """ setOfflineStorageDefaultQuota(int) """
        pass

    def setOfflineStoragePath(self, p_str): # real signature unknown; restored from __doc__
        """ setOfflineStoragePath(str) """
        pass

    def setOfflineWebApplicationCachePath(self, p_str): # real signature unknown; restored from __doc__
        """ setOfflineWebApplicationCachePath(str) """
        pass

    def setOfflineWebApplicationCacheQuota(self, p_int): # real signature unknown; restored from __doc__
        """ setOfflineWebApplicationCacheQuota(int) """
        pass

    def setThirdPartyCookiePolicy(self, QWebSettings_ThirdPartyCookiePolicy): # real signature unknown; restored from __doc__
        """ setThirdPartyCookiePolicy(self, QWebSettings.ThirdPartyCookiePolicy) """
        pass

    def setUserStyleSheetUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUserStyleSheetUrl(self, QUrl) """
        pass

    def setWebGraphic(self, QWebSettings_WebGraphic, QPixmap): # real signature unknown; restored from __doc__
        """ setWebGraphic(QWebSettings.WebGraphic, QPixmap) """
        pass

    def testAttribute(self, QWebSettings_WebAttribute): # real signature unknown; restored from __doc__
        """ testAttribute(self, QWebSettings.WebAttribute) -> bool """
        return False

    def thirdPartyCookiePolicy(self): # real signature unknown; restored from __doc__
        """ thirdPartyCookiePolicy(self) -> QWebSettings.ThirdPartyCookiePolicy """
        pass

    def userStyleSheetUrl(self): # real signature unknown; restored from __doc__
        """ userStyleSheetUrl(self) -> QUrl """
        pass

    def webGraphic(self, QWebSettings_WebGraphic): # real signature unknown; restored from __doc__
        """ webGraphic(QWebSettings.WebGraphic) -> QPixmap """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Accelerated2dCanvasEnabled = 32
    AcceleratedCompositingEnabled = 17
    AllowThirdPartyWithExistingCookies = 2
    AlwaysAllowThirdPartyCookies = 0
    AlwaysBlockThirdPartyCookies = 1
    AutoLoadImages = 0
    CaretBrowsingEnabled = 29
    CSSGridLayoutEnabled = 27
    CSSRegionsEnabled = 25
    CursiveFont = 4
    DefaultFixedFontSize = 3
    DefaultFontSize = 2
    DefaultFrameIconGraphic = 2
    DeveloperExtrasEnabled = 7
    DnsPrefetchEnabled = 15
    FantasyFont = 5
    FixedFont = 1
    FrameFlatteningEnabled = 21
    HyperlinkAuditingEnabled = 26
    InputSpeechButtonGraphic = 5
    JavaEnabled = 2
    JavascriptCanAccessClipboard = 6
    JavascriptCanCloseWindows = 23
    JavascriptCanOpenWindows = 5
    JavascriptEnabled = 1
    LinksIncludedInFocusChain = 8
    LocalContentCanAccessFileUrls = 19
    LocalContentCanAccessRemoteUrls = 14
    LocalStorageDatabaseEnabled = 13
    LocalStorageEnabled = 13
    MinimumFontSize = 0
    MinimumLogicalFontSize = 1
    MissingImageGraphic = 0
    MissingPluginGraphic = 1
    NotificationsEnabled = 30
    OfflineStorageDatabaseEnabled = 11
    OfflineWebApplicationCacheEnabled = 12
    PluginsEnabled = 3
    PrintElementBackgrounds = 10
    PrivateBrowsingEnabled = 4
    SansSerifFont = 3
    ScrollAnimatorEnabled = 28
    SearchCancelButtonGraphic = 6
    SearchCancelButtonPressedGraphic = 7
    SerifFont = 2
    SiteSpecificQuirksEnabled = 22
    SpatialNavigationEnabled = 18
    StandardFont = 0
    TextAreaSizeGripCornerGraphic = 3
    TiledBackingStoreEnabled = 20
    WebAudioEnabled = 31
    WebGLEnabled = 24
    XSSAuditingEnabled = 16
    ZoomTextOnly = 9


# variables with complex values



