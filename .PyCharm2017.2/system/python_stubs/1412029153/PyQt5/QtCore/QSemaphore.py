# encoding: utf-8
# module PyQt5.QtCore
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


class QSemaphore(): # skipped bases: <class 'sip.simplewrapper'>
    """ QSemaphore(n: int = 0) """
    def acquire(self, n=1): # real signature unknown; restored from __doc__
        """ acquire(self, n: int = 1) """
        pass

    def available(self): # real signature unknown; restored from __doc__
        """ available(self) -> int """
        return 0

    def release(self, n=1): # real signature unknown; restored from __doc__
        """ release(self, n: int = 1) """
        pass

    def tryAcquire(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        tryAcquire(self, n: int = 1) -> bool
        tryAcquire(self, int, int) -> bool
        """
        return False

    def __init__(self, n=0): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



