# encoding: utf-8
# module PyQt5.QtWebKitWidgets
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtWebKitWidgets.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets


# no functions
# classes

class QGraphicsWebView(__PyQt5_QtWidgets.QGraphicsWidget):
    """ QGraphicsWebView(parent: QGraphicsItem = None) """
    def back(self): # real signature unknown; restored from __doc__
        """ back(self) """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QGraphicsSceneContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QGraphicsSceneContextMenuEvent) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, QGraphicsSceneDragDropEvent) """
        pass

    def dragLeaveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QGraphicsSceneDragDropEvent) """
        pass

    def dragMoveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QGraphicsSceneDragDropEvent) """
        pass

    def dropEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QGraphicsSceneDragDropEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def findText(self, p_str, options=0): # real signature unknown; restored from __doc__
        """ findText(self, str, options: QWebPage.FindFlags = 0) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def forward(self): # real signature unknown; restored from __doc__
        """ forward(self) """
        pass

    def grabKeyboardEvent(self, *args, **kwargs): # real signature unknown
        pass

    def grabMouseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> QWebHistory """
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, QGraphicsSceneHoverEvent) """
        pass

    def hoverMoveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, QGraphicsSceneHoverEvent) """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def iconChanged(self): # real signature unknown; restored from __doc__
        """ iconChanged(self) [signal] """
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def isModified(self): # real signature unknown; restored from __doc__
        """ isModified(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTiledBackingStoreFrozen(self): # real signature unknown; restored from __doc__
        """ isTiledBackingStoreFrozen(self) -> bool """
        return False

    def itemChange(self, QGraphicsItem_GraphicsItemChange, Any): # real signature unknown; restored from __doc__
        """ itemChange(self, QGraphicsItem.GraphicsItemChange, Any) -> Any """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def linkClicked(self, QUrl): # real signature unknown; restored from __doc__
        """ linkClicked(self, QUrl) [signal] """
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QUrl)
        load(self, QNetworkRequest, operation: QNetworkAccessManager.Operation = QNetworkAccessManager.GetOperation, body: Union[QByteArray, bytes, bytearray] = QByteArray())
        """
        pass

    def loadFinished(self, bool): # real signature unknown; restored from __doc__
        """ loadFinished(self, bool) [signal] """
        pass

    def loadProgress(self, p_int): # real signature unknown; restored from __doc__
        """ loadProgress(self, int) [signal] """
        pass

    def loadStarted(self): # real signature unknown; restored from __doc__
        """ loadStarted(self) [signal] """
        pass

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def mousePressEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def mouseReleaseEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def page(self): # real signature unknown; restored from __doc__
        """ page(self) -> QWebPage """
        return QWebPage

    def pageAction(self, QWebPage_WebAction): # real signature unknown; restored from __doc__
        """ pageAction(self, QWebPage.WebAction) -> QAction """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def polishEvent(self, *args, **kwargs): # real signature unknown
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ reload(self) """
        pass

    def renderHints(self): # real signature unknown; restored from __doc__
        """ renderHints(self) -> QPainter.RenderHints """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizesToContents(self): # real signature unknown; restored from __doc__
        """ resizesToContents(self) -> bool """
        return False

    def sceneEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ sceneEvent(self, QEvent) -> bool """
        return False

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setContent(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setContent(self, Union[QByteArray, bytes, bytearray], mimeType: str = '', baseUrl: QUrl = QUrl()) """
        pass

    def setGeometry(self, QRectF): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRectF) """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setHtml(self, p_str, baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHtml(self, str, baseUrl: QUrl = QUrl()) """
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setPage(self, QWebPage): # real signature unknown; restored from __doc__
        """ setPage(self, QWebPage) """
        pass

    def setRenderHint(self, QPainter_RenderHint, enabled=True): # real signature unknown; restored from __doc__
        """ setRenderHint(self, QPainter.RenderHint, enabled: bool = True) """
        pass

    def setRenderHints(self, QPainter_RenderHints): # real signature unknown; restored from __doc__
        """ setRenderHints(self, QPainter.RenderHints) """
        pass

    def setResizesToContents(self, bool): # real signature unknown; restored from __doc__
        """ setResizesToContents(self, bool) """
        pass

    def setTiledBackingStoreFrozen(self, bool): # real signature unknown; restored from __doc__
        """ setTiledBackingStoreFrozen(self, bool) """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ settings(self) -> QWebSettings """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ setZoomFactor(self, float) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, Qt_SizeHint, QSizeF): # real signature unknown; restored from __doc__
        """ sizeHint(self, Qt.SizeHint, QSizeF) -> QSizeF """
        pass

    def statusBarMessage(self, p_str): # real signature unknown; restored from __doc__
        """ statusBarMessage(self, str) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def titleChanged(self, p_str): # real signature unknown; restored from __doc__
        """ titleChanged(self, str) [signal] """
        pass

    def triggerPageAction(self, QWebPage_WebAction, checked=False): # real signature unknown; restored from __doc__
        """ triggerPageAction(self, QWebPage.WebAction, checked: bool = False) """
        pass

    def ungrabKeyboardEvent(self, *args, **kwargs): # real signature unknown
        pass

    def ungrabMouseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ updateGeometry(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def urlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ urlChanged(self, QUrl) [signal] """
        pass

    def wheelEvent(self, QGraphicsSceneWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QGraphicsSceneWheelEvent) """
        pass

    def windowFrameEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowFrameSectionAt(self, *args, **kwargs): # real signature unknown
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ zoomFactor(self) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWebFrame(__PyQt5_QtCore.QObject):
    # no doc
    def addToJavaScriptWindowObject(self, p_str, QObject, ownership=None): # real signature unknown; restored from __doc__
        """ addToJavaScriptWindowObject(self, str, QObject, ownership: QWebFrame.ValueOwnership = QWebFrame.QtOwnership) """
        pass

    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> QUrl """
        pass

    def childFrames(self): # real signature unknown; restored from __doc__
        """ childFrames(self) -> object """
        return object()

    def contentsSize(self): # real signature unknown; restored from __doc__
        """ contentsSize(self) -> QSize """
        pass

    def contentsSizeChanged(self, QSize): # real signature unknown; restored from __doc__
        """ contentsSizeChanged(self, QSize) [signal] """
        pass

    def documentElement(self): # real signature unknown; restored from __doc__
        """ documentElement(self) -> QWebElement """
        pass

    def evaluateJavaScript(self, p_str): # real signature unknown; restored from __doc__
        """ evaluateJavaScript(self, str) -> Any """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def findAllElements(self, p_str): # real signature unknown; restored from __doc__
        """ findAllElements(self, str) -> QWebElementCollection """
        pass

    def findFirstElement(self, p_str): # real signature unknown; restored from __doc__
        """ findFirstElement(self, str) -> QWebElement """
        pass

    def frameName(self): # real signature unknown; restored from __doc__
        """ frameName(self) -> str """
        return ""

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def hitTestContent(self, QPoint): # real signature unknown; restored from __doc__
        """ hitTestContent(self, QPoint) -> QWebHitTestResult """
        return QWebHitTestResult

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def iconChanged(self): # real signature unknown; restored from __doc__
        """ iconChanged(self) [signal] """
        pass

    def initialLayoutCompleted(self): # real signature unknown; restored from __doc__
        """ initialLayoutCompleted(self) [signal] """
        pass

    def javaScriptWindowObjectCleared(self): # real signature unknown; restored from __doc__
        """ javaScriptWindowObjectCleared(self) [signal] """
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QUrl)
        load(self, QNetworkRequest, operation: QNetworkAccessManager.Operation = QNetworkAccessManager.GetOperation, body: Union[QByteArray, bytes, bytearray] = QByteArray())
        """
        pass

    def loadFinished(self, bool): # real signature unknown; restored from __doc__
        """ loadFinished(self, bool) [signal] """
        pass

    def loadStarted(self): # real signature unknown; restored from __doc__
        """ loadStarted(self) [signal] """
        pass

    def metaData(self): # real signature unknown; restored from __doc__
        """ metaData(self) -> object """
        return object()

    def page(self): # real signature unknown; restored from __doc__
        """ page(self) -> QWebPage """
        return QWebPage

    def pageChanged(self): # real signature unknown; restored from __doc__
        """ pageChanged(self) [signal] """
        pass

    def parentFrame(self): # real signature unknown; restored from __doc__
        """ parentFrame(self) -> QWebFrame """
        return QWebFrame

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def print(self, QPrinter): # real signature unknown; restored from __doc__
        """ print(self, QPrinter) """
        pass

    def print_(self, QPrinter): # real signature unknown; restored from __doc__
        """ print_(self, QPrinter) """
        pass

    def render(self, QPainter, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        render(self, QPainter, clip: QRegion = QRegion())
        render(self, QPainter, QWebFrame.RenderLayers, clip: QRegion = QRegion())
        """
        pass

    def requestedUrl(self): # real signature unknown; restored from __doc__
        """ requestedUrl(self) -> QUrl """
        pass

    def scroll(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scroll(self, int, int) """
        pass

    def scrollBarGeometry(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ scrollBarGeometry(self, Qt.Orientation) -> QRect """
        pass

    def scrollBarMaximum(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ scrollBarMaximum(self, Qt.Orientation) -> int """
        return 0

    def scrollBarMinimum(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ scrollBarMinimum(self, Qt.Orientation) -> int """
        return 0

    def scrollBarPolicy(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ scrollBarPolicy(self, Qt.Orientation) -> Qt.ScrollBarPolicy """
        pass

    def scrollBarValue(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ scrollBarValue(self, Qt.Orientation) -> int """
        return 0

    def scrollPosition(self): # real signature unknown; restored from __doc__
        """ scrollPosition(self) -> QPoint """
        pass

    def scrollToAnchor(self, p_str): # real signature unknown; restored from __doc__
        """ scrollToAnchor(self, str) """
        pass

    def securityOrigin(self): # real signature unknown; restored from __doc__
        """ securityOrigin(self) -> QWebSecurityOrigin """
        pass

    def setContent(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setContent(self, Union[QByteArray, bytes, bytearray], mimeType: str = '', baseUrl: QUrl = QUrl()) """
        pass

    def setFocus(self): # real signature unknown; restored from __doc__
        """ setFocus(self) """
        pass

    def setHtml(self, p_str, baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHtml(self, str, baseUrl: QUrl = QUrl()) """
        pass

    def setScrollBarPolicy(self, Qt_Orientation, Qt_ScrollBarPolicy): # real signature unknown; restored from __doc__
        """ setScrollBarPolicy(self, Qt.Orientation, Qt.ScrollBarPolicy) """
        pass

    def setScrollBarValue(self, Qt_Orientation, p_int): # real signature unknown; restored from __doc__
        """ setScrollBarValue(self, Qt.Orientation, int) """
        pass

    def setScrollPosition(self, QPoint): # real signature unknown; restored from __doc__
        """ setScrollPosition(self, QPoint) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ setZoomFactor(self, float) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def titleChanged(self, p_str): # real signature unknown; restored from __doc__
        """ titleChanged(self, str) [signal] """
        pass

    def toHtml(self): # real signature unknown; restored from __doc__
        """ toHtml(self) -> str """
        return ""

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def urlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ urlChanged(self, QUrl) [signal] """
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ zoomFactor(self) -> float """
        return 0.0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AllLayers = 255
    AutoOwnership = 2
    ContentsLayer = 16
    PanIconLayer = 64
    QtOwnership = 0
    ScriptOwnership = 1
    ScrollBarLayer = 32


class QWebHitTestResult(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QWebHitTestResult()
    QWebHitTestResult(QWebHitTestResult)
    """
    def alternateText(self): # real signature unknown; restored from __doc__
        """ alternateText(self) -> str """
        return ""

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRect """
        pass

    def element(self): # real signature unknown; restored from __doc__
        """ element(self) -> QWebElement """
        pass

    def enclosingBlockElement(self): # real signature unknown; restored from __doc__
        """ enclosingBlockElement(self) -> QWebElement """
        pass

    def frame(self): # real signature unknown; restored from __doc__
        """ frame(self) -> QWebFrame """
        return QWebFrame

    def imageUrl(self): # real signature unknown; restored from __doc__
        """ imageUrl(self) -> QUrl """
        pass

    def isContentEditable(self): # real signature unknown; restored from __doc__
        """ isContentEditable(self) -> bool """
        return False

    def isContentSelected(self): # real signature unknown; restored from __doc__
        """ isContentSelected(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def linkElement(self): # real signature unknown; restored from __doc__
        """ linkElement(self) -> QWebElement """
        pass

    def linkTargetFrame(self): # real signature unknown; restored from __doc__
        """ linkTargetFrame(self) -> QWebFrame """
        return QWebFrame

    def linkText(self): # real signature unknown; restored from __doc__
        """ linkText(self) -> str """
        return ""

    def linkTitle(self): # real signature unknown; restored from __doc__
        """ linkTitle(self) -> QUrl """
        pass

    def linkTitleString(self): # real signature unknown; restored from __doc__
        """ linkTitleString(self) -> str """
        return ""

    def linkUrl(self): # real signature unknown; restored from __doc__
        """ linkUrl(self) -> QUrl """
        pass

    def mediaUrl(self): # real signature unknown; restored from __doc__
        """ mediaUrl(self) -> QUrl """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> QPixmap """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def __init__(self, QWebHitTestResult=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebInspector(__PyQt5_QtWidgets.QWidget):
    """ QWebInspector(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def page(self): # real signature unknown; restored from __doc__
        """ page(self) -> QWebPage """
        return QWebPage

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setPage(self, QWebPage): # real signature unknown; restored from __doc__
        """ setPage(self, QWebPage) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWebPage(__PyQt5_QtCore.QObject):
    """ QWebPage(parent: QObject = None) """
    def acceptNavigationRequest(self, QWebFrame, QNetworkRequest, QWebPage_NavigationType): # real signature unknown; restored from __doc__
        """ acceptNavigationRequest(self, QWebFrame, QNetworkRequest, QWebPage.NavigationType) -> bool """
        return False

    def action(self, QWebPage_WebAction): # real signature unknown; restored from __doc__
        """ action(self, QWebPage.WebAction) -> QAction """
        pass

    def applicationCacheQuotaExceeded(self, QWebSecurityOrigin, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ applicationCacheQuotaExceeded(self, QWebSecurityOrigin, int, int) [signal] """
        pass

    def bytesReceived(self): # real signature unknown; restored from __doc__
        """ bytesReceived(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def chooseFile(self, QWebFrame, p_str): # real signature unknown; restored from __doc__
        """ chooseFile(self, QWebFrame, str) -> str """
        return ""

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsChanged(self): # real signature unknown; restored from __doc__
        """ contentsChanged(self) [signal] """
        pass

    def createPlugin(self, p_str, QUrl, Iterable, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createPlugin(self, str, QUrl, Iterable[str], Iterable[str]) -> QObject """
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ createStandardContextMenu(self) -> QMenu """
        pass

    def createWindow(self, QWebPage_WebWindowType): # real signature unknown; restored from __doc__
        """ createWindow(self, QWebPage.WebWindowType) -> QWebPage """
        return QWebPage

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> QWebFrame """
        return QWebFrame

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def databaseQuotaExceeded(self, QWebFrame, p_str): # real signature unknown; restored from __doc__
        """ databaseQuotaExceeded(self, QWebFrame, str) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def downloadRequested(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ downloadRequested(self, QNetworkRequest) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def extension(self, QWebPage_Extension, option=None, output=None): # real signature unknown; restored from __doc__
        """ extension(self, QWebPage.Extension, option: QWebPage.ExtensionOption = None, output: QWebPage.ExtensionReturn = None) -> bool """
        return False

    def featurePermissionRequestCanceled(self, QWebFrame, QWebPage_Feature): # real signature unknown; restored from __doc__
        """ featurePermissionRequestCanceled(self, QWebFrame, QWebPage.Feature) [signal] """
        pass

    def featurePermissionRequested(self, QWebFrame, QWebPage_Feature): # real signature unknown; restored from __doc__
        """ featurePermissionRequested(self, QWebFrame, QWebPage.Feature) [signal] """
        pass

    def findText(self, p_str, options=0): # real signature unknown; restored from __doc__
        """ findText(self, str, options: QWebPage.FindFlags = 0) -> bool """
        return False

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def forwardUnsupportedContent(self): # real signature unknown; restored from __doc__
        """ forwardUnsupportedContent(self) -> bool """
        return False

    def frameAt(self, QPoint): # real signature unknown; restored from __doc__
        """ frameAt(self, QPoint) -> QWebFrame """
        return QWebFrame

    def frameCreated(self, QWebFrame): # real signature unknown; restored from __doc__
        """ frameCreated(self, QWebFrame) [signal] """
        pass

    def geometryChangeRequested(self, QRect): # real signature unknown; restored from __doc__
        """ geometryChangeRequested(self, QRect) [signal] """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> QWebHistory """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def isContentEditable(self): # real signature unknown; restored from __doc__
        """ isContentEditable(self) -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ isModified(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def javaScriptAlert(self, QWebFrame, p_str): # real signature unknown; restored from __doc__
        """ javaScriptAlert(self, QWebFrame, str) """
        pass

    def javaScriptConfirm(self, QWebFrame, p_str): # real signature unknown; restored from __doc__
        """ javaScriptConfirm(self, QWebFrame, str) -> bool """
        return False

    def javaScriptConsoleMessage(self, p_str, p_int, p_str_1): # real signature unknown; restored from __doc__
        """ javaScriptConsoleMessage(self, str, int, str) """
        pass

    def javaScriptPrompt(self, QWebFrame, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ javaScriptPrompt(self, QWebFrame, str, str) -> Tuple[bool, str] """
        pass

    def linkClicked(self, QUrl): # real signature unknown; restored from __doc__
        """ linkClicked(self, QUrl) [signal] """
        pass

    def linkDelegationPolicy(self): # real signature unknown; restored from __doc__
        """ linkDelegationPolicy(self) -> QWebPage.LinkDelegationPolicy """
        pass

    def linkHovered(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ linkHovered(self, str, str, str) [signal] """
        pass

    def loadFinished(self, bool): # real signature unknown; restored from __doc__
        """ loadFinished(self, bool) [signal] """
        pass

    def loadProgress(self, p_int): # real signature unknown; restored from __doc__
        """ loadProgress(self, int) [signal] """
        pass

    def loadStarted(self): # real signature unknown; restored from __doc__
        """ loadStarted(self) [signal] """
        pass

    def mainFrame(self): # real signature unknown; restored from __doc__
        """ mainFrame(self) -> QWebFrame """
        return QWebFrame

    def menuBarVisibilityChangeRequested(self, bool): # real signature unknown; restored from __doc__
        """ menuBarVisibilityChangeRequested(self, bool) [signal] """
        pass

    def microFocusChanged(self): # real signature unknown; restored from __doc__
        """ microFocusChanged(self) [signal] """
        pass

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> QNetworkAccessManager """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> QPalette """
        pass

    def pluginFactory(self): # real signature unknown; restored from __doc__
        """ pluginFactory(self) -> QWebPluginFactory """
        pass

    def preferredContentsSize(self): # real signature unknown; restored from __doc__
        """ preferredContentsSize(self) -> QSize """
        pass

    def printRequested(self, QWebFrame): # real signature unknown; restored from __doc__
        """ printRequested(self, QWebFrame) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def repaintRequested(self, QRect): # real signature unknown; restored from __doc__
        """ repaintRequested(self, QRect) [signal] """
        pass

    def restoreFrameStateRequested(self, QWebFrame): # real signature unknown; restored from __doc__
        """ restoreFrameStateRequested(self, QWebFrame) [signal] """
        pass

    def saveFrameStateRequested(self, QWebFrame, QWebHistoryItem): # real signature unknown; restored from __doc__
        """ saveFrameStateRequested(self, QWebFrame, QWebHistoryItem) [signal] """
        pass

    def scrollRequested(self, p_int, p_int_1, QRect): # real signature unknown; restored from __doc__
        """ scrollRequested(self, int, int, QRect) [signal] """
        pass

    def selectedHtml(self): # real signature unknown; restored from __doc__
        """ selectedHtml(self) -> str """
        return ""

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActualVisibleContentRect(self, QRect): # real signature unknown; restored from __doc__
        """ setActualVisibleContentRect(self, QRect) """
        pass

    def setContentEditable(self, bool): # real signature unknown; restored from __doc__
        """ setContentEditable(self, bool) """
        pass

    def setFeaturePermission(self, QWebFrame, QWebPage_Feature, QWebPage_PermissionPolicy): # real signature unknown; restored from __doc__
        """ setFeaturePermission(self, QWebFrame, QWebPage.Feature, QWebPage.PermissionPolicy) """
        pass

    def setForwardUnsupportedContent(self, bool): # real signature unknown; restored from __doc__
        """ setForwardUnsupportedContent(self, bool) """
        pass

    def setLinkDelegationPolicy(self, QWebPage_LinkDelegationPolicy): # real signature unknown; restored from __doc__
        """ setLinkDelegationPolicy(self, QWebPage.LinkDelegationPolicy) """
        pass

    def setNetworkAccessManager(self, QNetworkAccessManager): # real signature unknown; restored from __doc__
        """ setNetworkAccessManager(self, QNetworkAccessManager) """
        pass

    def setPalette(self, QPalette): # real signature unknown; restored from __doc__
        """ setPalette(self, QPalette) """
        pass

    def setPluginFactory(self, QWebPluginFactory): # real signature unknown; restored from __doc__
        """ setPluginFactory(self, QWebPluginFactory) """
        pass

    def setPreferredContentsSize(self, QSize): # real signature unknown; restored from __doc__
        """ setPreferredContentsSize(self, QSize) """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ settings(self) -> QWebSettings """
        pass

    def setView(self, QWidget): # real signature unknown; restored from __doc__
        """ setView(self, QWidget) """
        pass

    def setViewportSize(self, QSize): # real signature unknown; restored from __doc__
        """ setViewportSize(self, QSize) """
        pass

    def setVisibilityState(self, QWebPage_VisibilityState): # real signature unknown; restored from __doc__
        """ setVisibilityState(self, QWebPage.VisibilityState) """
        pass

    def shouldInterruptJavaScript(self): # real signature unknown; restored from __doc__
        """ shouldInterruptJavaScript(self) -> bool """
        return False

    def statusBarMessage(self, p_str): # real signature unknown; restored from __doc__
        """ statusBarMessage(self, str) [signal] """
        pass

    def statusBarVisibilityChangeRequested(self, bool): # real signature unknown; restored from __doc__
        """ statusBarVisibilityChangeRequested(self, bool) [signal] """
        pass

    def supportedContentTypes(self): # real signature unknown; restored from __doc__
        """ supportedContentTypes(self) -> List[str] """
        return []

    def supportsContentType(self, p_str): # real signature unknown; restored from __doc__
        """ supportsContentType(self, str) -> bool """
        return False

    def supportsExtension(self, QWebPage_Extension): # real signature unknown; restored from __doc__
        """ supportsExtension(self, QWebPage.Extension) -> bool """
        return False

    def swallowContextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ swallowContextMenuEvent(self, QContextMenuEvent) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toolBarVisibilityChangeRequested(self, bool): # real signature unknown; restored from __doc__
        """ toolBarVisibilityChangeRequested(self, bool) [signal] """
        pass

    def totalBytes(self): # real signature unknown; restored from __doc__
        """ totalBytes(self) -> int """
        return 0

    def triggerAction(self, QWebPage_WebAction, checked=False): # real signature unknown; restored from __doc__
        """ triggerAction(self, QWebPage.WebAction, checked: bool = False) """
        pass

    def undoStack(self): # real signature unknown; restored from __doc__
        """ undoStack(self) -> QUndoStack """
        pass

    def unsupportedContent(self, QNetworkReply): # real signature unknown; restored from __doc__
        """ unsupportedContent(self, QNetworkReply) [signal] """
        pass

    def updatePositionDependentActions(self, QPoint): # real signature unknown; restored from __doc__
        """ updatePositionDependentActions(self, QPoint) """
        pass

    def userAgentForUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ userAgentForUrl(self, QUrl) -> str """
        return ""

    def view(self): # real signature unknown; restored from __doc__
        """ view(self) -> QWidget """
        pass

    def viewportAttributesForSize(self, QSize): # real signature unknown; restored from __doc__
        """ viewportAttributesForSize(self, QSize) -> QWebPage.ViewportAttributes """
        pass

    def viewportChangeRequested(self): # real signature unknown; restored from __doc__
        """ viewportChangeRequested(self) [signal] """
        pass

    def viewportSize(self): # real signature unknown; restored from __doc__
        """ viewportSize(self) -> QSize """
        pass

    def visibilityState(self): # real signature unknown; restored from __doc__
        """ visibilityState(self) -> QWebPage.VisibilityState """
        pass

    def windowCloseRequested(self): # real signature unknown; restored from __doc__
        """ windowCloseRequested(self) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AlignCenter = 63
    AlignJustified = 64
    AlignLeft = 65
    AlignRight = 66
    Back = 8
    ChooseMultipleFilesExtension = 0
    Copy = 13
    CopyImageToClipboard = 7
    CopyImageUrlToClipboard = 68
    CopyLinkToClipboard = 4
    CopyMediaUrlToClipboard = 71
    Cut = 12
    DelegateAllLinks = 2
    DelegateExternalLinks = 1
    DeleteEndOfWord = 42
    DeleteStartOfWord = 41
    DontDelegateLinks = 0
    DownloadImageToDisk = 6
    DownloadLinkToDisk = 3
    DownloadMediaToDisk = 70
    ErrorPageExtension = 1
    FindAtWordBeginningsOnly = 16
    FindBackward = 1
    FindBeginsInSelection = 64
    FindCaseSensitively = 2
    FindWrapsAroundDocument = 4
    Forward = 9
    Geolocation = 1
    HighlightAllOccurrences = 8
    Http = 1
    Indent = 61
    InsertLineSeparator = 51
    InsertOrderedList = 60
    InsertParagraphSeparator = 50
    InsertUnorderedList = 59
    InspectElement = 49
    MoveToEndOfBlock = 26
    MoveToEndOfDocument = 28
    MoveToEndOfLine = 24
    MoveToNextChar = 17
    MoveToNextLine = 21
    MoveToNextWord = 19
    MoveToPreviousChar = 18
    MoveToPreviousLine = 22
    MoveToPreviousWord = 20
    MoveToStartOfBlock = 25
    MoveToStartOfDocument = 27
    MoveToStartOfLine = 23
    NavigationTypeBackOrForward = 2
    NavigationTypeFormResubmitted = 4
    NavigationTypeFormSubmitted = 1
    NavigationTypeLinkClicked = 0
    NavigationTypeOther = 5
    NavigationTypeReload = 3
    Notifications = 0
    NoWebAction = -1
    OpenFrameInNewWindow = 2
    OpenImageInNewWindow = 5
    OpenLink = 0
    OpenLinkInNewWindow = 1
    OpenLinkInThisWindow = 69
    Outdent = 62
    Paste = 14
    PasteAndMatchStyle = 54
    PermissionDeniedByUser = 2
    PermissionGrantedByUser = 1
    PermissionUnknown = 0
    QtNetwork = 0
    Redo = 16
    Reload = 11
    ReloadAndBypassCache = 53
    RemoveFormat = 55
    SelectAll = 52
    SelectEndOfBlock = 38
    SelectEndOfDocument = 40
    SelectEndOfLine = 36
    SelectNextChar = 29
    SelectNextLine = 33
    SelectNextWord = 31
    SelectPreviousChar = 30
    SelectPreviousLine = 34
    SelectPreviousWord = 32
    SelectStartOfBlock = 37
    SelectStartOfDocument = 39
    SelectStartOfLine = 35
    SetTextDirectionDefault = 43
    SetTextDirectionLeftToRight = 44
    SetTextDirectionRightToLeft = 45
    Stop = 10
    StopScheduledPageRefresh = 67
    ToggleBold = 46
    ToggleItalic = 47
    ToggleMediaControls = 72
    ToggleMediaLoop = 73
    ToggleMediaMute = 75
    ToggleMediaPlayPause = 74
    ToggleStrikethrough = 56
    ToggleSubscript = 57
    ToggleSuperscript = 58
    ToggleUnderline = 48
    ToggleVideoFullscreen = 76
    TreatMedialCapitalAsWordBeginning = 32
    Undo = 15
    VisibilityStateHidden = 1
    VisibilityStatePrerender = 2
    VisibilityStateUnloaded = 3
    VisibilityStateVisible = 0
    WebBrowserWindow = 0
    WebKit = 2
    WebModalDialog = 1


class QWebView(__PyQt5_QtWidgets.QWidget):
    """ QWebView(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def back(self): # real signature unknown; restored from __doc__
        """ back(self) """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createWindow(self, QWebPage_WebWindowType): # real signature unknown; restored from __doc__
        """ createWindow(self, QWebPage.WebWindowType) -> QWebView """
        return QWebView

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def findText(self, p_str, options=0): # real signature unknown; restored from __doc__
        """ findText(self, str, options: QWebPage.FindFlags = 0) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def forward(self): # real signature unknown; restored from __doc__
        """ forward(self) """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> QWebHistory """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def iconChanged(self): # real signature unknown; restored from __doc__
        """ iconChanged(self) [signal] """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def isModified(self): # real signature unknown; restored from __doc__
        """ isModified(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def linkClicked(self, QUrl): # real signature unknown; restored from __doc__
        """ linkClicked(self, QUrl) [signal] """
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QUrl)
        load(self, QNetworkRequest, operation: QNetworkAccessManager.Operation = QNetworkAccessManager.GetOperation, body: Union[QByteArray, bytes, bytearray] = QByteArray())
        """
        pass

    def loadFinished(self, bool): # real signature unknown; restored from __doc__
        """ loadFinished(self, bool) [signal] """
        pass

    def loadProgress(self, p_int): # real signature unknown; restored from __doc__
        """ loadProgress(self, int) [signal] """
        pass

    def loadStarted(self): # real signature unknown; restored from __doc__
        """ loadStarted(self) [signal] """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def page(self): # real signature unknown; restored from __doc__
        """ page(self) -> QWebPage """
        return QWebPage

    def pageAction(self, QWebPage_WebAction): # real signature unknown; restored from __doc__
        """ pageAction(self, QWebPage.WebAction) -> QAction """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def print(self, QPrinter): # real signature unknown; restored from __doc__
        """ print(self, QPrinter) """
        pass

    def print_(self, QPrinter): # real signature unknown; restored from __doc__
        """ print_(self, QPrinter) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ reload(self) """
        pass

    def renderHints(self): # real signature unknown; restored from __doc__
        """ renderHints(self) -> QPainter.RenderHints """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def selectedHtml(self): # real signature unknown; restored from __doc__
        """ selectedHtml(self) -> str """
        return ""

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setContent(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setContent(self, Union[QByteArray, bytes, bytearray], mimeType: str = '', baseUrl: QUrl = QUrl()) """
        pass

    def setHtml(self, p_str, baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHtml(self, str, baseUrl: QUrl = QUrl()) """
        pass

    def setPage(self, QWebPage): # real signature unknown; restored from __doc__
        """ setPage(self, QWebPage) """
        pass

    def setRenderHint(self, QPainter_RenderHint, enabled=True): # real signature unknown; restored from __doc__
        """ setRenderHint(self, QPainter.RenderHint, enabled: bool = True) """
        pass

    def setRenderHints(self, QPainter_RenderHints): # real signature unknown; restored from __doc__
        """ setRenderHints(self, QPainter.RenderHints) """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ settings(self) -> QWebSettings """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ setZoomFactor(self, float) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def statusBarMessage(self, p_str): # real signature unknown; restored from __doc__
        """ statusBarMessage(self, str) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def titleChanged(self, p_str): # real signature unknown; restored from __doc__
        """ titleChanged(self, str) [signal] """
        pass

    def triggerPageAction(self, QWebPage_WebAction, checked=False): # real signature unknown; restored from __doc__
        """ triggerPageAction(self, QWebPage.WebAction, checked: bool = False) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def urlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ urlChanged(self, QUrl) [signal] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ zoomFactor(self) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values



