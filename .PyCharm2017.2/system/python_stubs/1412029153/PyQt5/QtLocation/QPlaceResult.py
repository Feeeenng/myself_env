# encoding: utf-8
# module PyQt5.QtLocation
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


from .QPlaceSearchResult import QPlaceSearchResult

class QPlaceResult(QPlaceSearchResult):
    """
    QPlaceResult()
    QPlaceResult(QPlaceSearchResult)
    QPlaceResult(QPlaceResult)
    """
    def distance(self): # real signature unknown; restored from __doc__
        """ distance(self) -> float """
        return 0.0

    def isSponsored(self): # real signature unknown; restored from __doc__
        """ isSponsored(self) -> bool """
        return False

    def place(self): # real signature unknown; restored from __doc__
        """ place(self) -> QPlace """
        return QPlace

    def setDistance(self, p_float): # real signature unknown; restored from __doc__
        """ setDistance(self, float) """
        pass

    def setPlace(self, QPlace): # real signature unknown; restored from __doc__
        """ setPlace(self, QPlace) """
        pass

    def setSponsored(self, bool): # real signature unknown; restored from __doc__
        """ setSponsored(self, bool) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


