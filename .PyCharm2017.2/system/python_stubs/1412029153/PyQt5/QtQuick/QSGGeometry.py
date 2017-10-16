# encoding: utf-8
# module PyQt5.QtQuick
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml


class QSGGeometry(): # skipped bases: <class 'sip.wrapper'>
    """
    QSGGeometry(QSGGeometry.AttributeSet, int, indexCount: int = 0, indexType: int = GL_UNSIGNED_SHORT)
    QSGGeometry(QSGGeometry)
    """
    def allocate(self, p_int, indexCount=0): # real signature unknown; restored from __doc__
        """ allocate(self, int, indexCount: int = 0) """
        pass

    def attributeCount(self): # real signature unknown; restored from __doc__
        """ attributeCount(self) -> int """
        return 0

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> sip.array[QSGGeometry.Attribute] """
        pass

    def defaultAttributes_ColoredPoint2D(self): # real signature unknown; restored from __doc__
        """ defaultAttributes_ColoredPoint2D() -> QSGGeometry.AttributeSet """
        pass

    def defaultAttributes_Point2D(self): # real signature unknown; restored from __doc__
        """ defaultAttributes_Point2D() -> QSGGeometry.AttributeSet """
        pass

    def defaultAttributes_TexturedPoint2D(self): # real signature unknown; restored from __doc__
        """ defaultAttributes_TexturedPoint2D() -> QSGGeometry.AttributeSet """
        pass

    def drawingMode(self): # real signature unknown; restored from __doc__
        """ drawingMode(self) -> int """
        return 0

    def indexCount(self): # real signature unknown; restored from __doc__
        """ indexCount(self) -> int """
        return 0

    def indexData(self): # real signature unknown; restored from __doc__
        """ indexData(self) -> sip.voidptr """
        pass

    def indexDataAsUInt(self): # real signature unknown; restored from __doc__
        """ indexDataAsUInt(self) -> sip.array[int] """
        pass

    def indexDataAsUShort(self): # real signature unknown; restored from __doc__
        """ indexDataAsUShort(self) -> sip.array[int] """
        pass

    def indexDataPattern(self): # real signature unknown; restored from __doc__
        """ indexDataPattern(self) -> QSGGeometry.DataPattern """
        pass

    def indexType(self): # real signature unknown; restored from __doc__
        """ indexType(self) -> int """
        return 0

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> float """
        return 0.0

    def markIndexDataDirty(self): # real signature unknown; restored from __doc__
        """ markIndexDataDirty(self) """
        pass

    def markVertexDataDirty(self): # real signature unknown; restored from __doc__
        """ markVertexDataDirty(self) """
        pass

    def setDrawingMode(self, p_int): # real signature unknown; restored from __doc__
        """ setDrawingMode(self, int) """
        pass

    def setIndexDataPattern(self, QSGGeometry_DataPattern): # real signature unknown; restored from __doc__
        """ setIndexDataPattern(self, QSGGeometry.DataPattern) """
        pass

    def setLineWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setLineWidth(self, float) """
        pass

    def setVertexDataPattern(self, QSGGeometry_DataPattern): # real signature unknown; restored from __doc__
        """ setVertexDataPattern(self, QSGGeometry.DataPattern) """
        pass

    def sizeOfIndex(self): # real signature unknown; restored from __doc__
        """ sizeOfIndex(self) -> int """
        return 0

    def sizeOfVertex(self): # real signature unknown; restored from __doc__
        """ sizeOfVertex(self) -> int """
        return 0

    def updateRectGeometry(self, QSGGeometry, QRectF): # real signature unknown; restored from __doc__
        """ updateRectGeometry(QSGGeometry, QRectF) """
        pass

    def updateTexturedRectGeometry(self, QSGGeometry, QRectF, QRectF_1): # real signature unknown; restored from __doc__
        """ updateTexturedRectGeometry(QSGGeometry, QRectF, QRectF) """
        pass

    def vertexCount(self): # real signature unknown; restored from __doc__
        """ vertexCount(self) -> int """
        return 0

    def vertexData(self): # real signature unknown; restored from __doc__
        """ vertexData(self) -> sip.voidptr """
        pass

    def vertexDataAsColoredPoint2D(self): # real signature unknown; restored from __doc__
        """ vertexDataAsColoredPoint2D(self) -> sip.array[QSGGeometry.ColoredPoint2D] """
        pass

    def vertexDataAsPoint2D(self): # real signature unknown; restored from __doc__
        """ vertexDataAsPoint2D(self) -> sip.array[QSGGeometry.Point2D] """
        pass

    def vertexDataAsTexturedPoint2D(self): # real signature unknown; restored from __doc__
        """ vertexDataAsTexturedPoint2D(self) -> sip.array[QSGGeometry.TexturedPoint2D] """
        pass

    def vertexDataPattern(self): # real signature unknown; restored from __doc__
        """ vertexDataPattern(self) -> QSGGeometry.DataPattern """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AlwaysUploadPattern = 0
    DynamicPattern = 2
    GL_BYTE = 5120
    GL_DOUBLE = 5130
    GL_FLOAT = 5126
    GL_INT = 5124
    GL_LINES = 1
    GL_LINE_LOOP = 2
    GL_LINE_STRIP = 3
    GL_POINTS = 0
    GL_TRIANGLES = 4
    GL_TRIANGLE_FAN = 6
    GL_TRIANGLE_STRIP = 5
    StaticPattern = 3
    StreamPattern = 1


