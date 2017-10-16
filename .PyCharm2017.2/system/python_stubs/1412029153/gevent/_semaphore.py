# encoding: utf-8
# module gevent._semaphore
# from D:\ProgramData\Anaconda3\lib\site-packages\gevent\_semaphore.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
from greenlet import getcurrent


# functions

def get_hub(*args, **kwargs): # reliably restored by inspect
    """
    Return the hub for the current thread.
    
        If a hub does not exist in the current thread, a new one is
        created of the type returned by :func:`get_hub_class`.
    """
    pass

# classes

class Semaphore(object):
    """
    Semaphore(value=1) -> Semaphore
    
        A semaphore manages a counter representing the number of release()
        calls minus the number of acquire() calls, plus an initial value.
        The acquire() method blocks if necessary until it can return
        without making the counter negative.
    
        If not given, ``value`` defaults to 1.
    
        The semaphore is a context manager and can be used in ``with`` statements.
    
        This Semaphore's ``__exit__`` method does not call the trace function
        on CPython, but does under PyPy.
    
        .. seealso:: :class:`BoundedSemaphore` for a safer version that prevents
           some classes of bugs.
    """
    def acquire(self, blocking=True, timeout=None): # real signature unknown; restored from __doc__
        """
        acquire(blocking=True, timeout=None) -> bool
        
                Acquire the semaphore.
        
                .. caution:: If this semaphore was initialized with a size of 0,
                   this method will block forever (unless a timeout is given or blocking is
                   set to false).
        
                :keyword bool blocking: If True (the default), this function will block
                   until the semaphore is acquired.
                :keyword float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A boolean indicating whether the semaphore was acquired.
                   If ``blocking`` is True and ``timeout`` is None (the default), then
                   (so long as this semaphore was initialized with a size greater than 0)
                   this will always return True. If a timeout was given, and it expired before
                   the semaphore was acquired, False will be returned. (Note that this can still
                   raise a ``Timeout`` exception, if some other caller had already started a timer.)
        """
        return False

    def locked(self, *args, **kwargs): # real signature unknown
        """
        Return a boolean indicating whether the semaphore can be acquired.
                Most useful with binary semaphores.
        """
        pass

    def rawlink(self, callback): # real signature unknown; restored from __doc__
        """
        rawlink(callback) -> None
        
                Register a callback to call when a counter is more than zero.
        
                *callback* will be called in the :class:`Hub <gevent.hub.Hub>`, so it must not use blocking gevent API.
                *callback* will be passed one argument: this instance.
        
                This method is normally called automatically by :meth:`acquire` and :meth:`wait`; most code
                will not need to use it.
        """
        pass

    def release(self, *args, **kwargs): # real signature unknown
        """ Release the semaphore, notifying any waiters if needed. """
        pass

    def unlink(self, callback): # real signature unknown; restored from __doc__
        """
        unlink(callback) -> None
        
                Remove the callback set by :meth:`rawlink`.
        
                This method is normally called automatically by :meth:`acquire`  and :meth:`wait`; most
                code will not need to use it.
        """
        pass

    def wait(self, timeout=None): # real signature unknown; restored from __doc__
        """
        wait(timeout=None) -> int
        
                Wait until it is possible to acquire this semaphore, or until the optional
                *timeout* elapses.
        
                .. caution:: If this semaphore was initialized with a size of 0,
                   this method will block forever if no timeout is given.
        
                :keyword float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A number indicating how many times the semaphore can be acquired
                    before blocking.
        """
        return 0

    def _notify_links(self, *args, **kwargs): # real signature unknown
        pass

    def _py3k_acquire(self, *args, **kwargs): # real signature unknown
        """
        acquire(blocking=True, timeout=None) -> bool
        
                Acquire the semaphore.
        
                .. caution:: If this semaphore was initialized with a size of 0,
                   this method will block forever (unless a timeout is given or blocking is
                   set to false).
        
                :keyword bool blocking: If True (the default), this function will block
                   until the semaphore is acquired.
                :keyword float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A boolean indicating whether the semaphore was acquired.
                   If ``blocking`` is True and ``timeout`` is None (the default), then
                   (so long as this semaphore was initialized with a size greater than 0)
                   this will always return True. If a timeout was given, and it expired before
                   the semaphore was acquired, False will be returned. (Note that this can still
                   raise a ``Timeout`` exception, if some other caller had already started a timer.)
        """
        pass

    def _start_notify(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, value=1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _links = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _notifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class BoundedSemaphore(Semaphore):
    """
    BoundedSemaphore(value=1) -> BoundedSemaphore
    
        A bounded semaphore checks to make sure its current value doesn't
        exceed its initial value. If it does, :class:`ValueError` is
        raised. In most situations semaphores are used to guard resources
        with limited capacity. If the semaphore is released too many times
        it's a sign of a bug.
    
        If not given, *value* defaults to 1.
    """
    def release(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, value=1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _initial_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _OVER_RELEASE_ERROR = ValueError
    __pyx_vtable__ = None # (!) real value is ''


class Timeout(BaseException):
    """
    Raise *exception* in the current greenlet after given time period::
    
            timeout = Timeout(seconds, exception)
            timeout.start()
            try:
                ...  # exception will be raised here, after *seconds* passed since start() call
            finally:
                timeout.cancel()
    
        .. note:: If the code that the timeout was protecting finishes
           executing before the timeout elapses, be sure to ``cancel`` the
           timeout so it is not unexpectedly raised in the future. Even if
           it is raised, it is a best practice to cancel it. This
           ``try/finally`` construct or a ``with`` statement is a
           recommended pattern.
    
        When *exception* is omitted or ``None``, the :class:`Timeout` instance itself is raised:
    
            >>> import gevent
            >>> gevent.Timeout(0.1).start()
            >>> gevent.sleep(0.2)  #doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            Timeout: 0.1 seconds
    
        To simplify starting and canceling timeouts, the ``with`` statement can be used::
    
            with gevent.Timeout(seconds, exception) as timeout:
                pass  # ... code block ...
    
        This is equivalent to the try/finally block above with one additional feature:
        if *exception* is the literal ``False``, the timeout is still raised, but the context manager
        suppresses it, so the code outside the with-block won't see it.
    
        This is handy for adding a timeout to the functions that don't
        support a *timeout* parameter themselves::
    
            data = None
            with gevent.Timeout(5, False):
                data = mysock.makefile().readline()
            if data is None:
                ...  # 5 seconds passed without reading a line
            else:
                ...  # a line was read within 5 seconds
    
        .. caution:: If ``readline()`` above catches and doesn't re-raise :class:`BaseException`
           (for example, with a bare ``except:``), then your timeout will fail to function and control
           won't be returned to you when you expect.
    
        When catching timeouts, keep in mind that the one you catch may
        not be the one you have set (a calling function may have set its
        own timeout); if you going to silence a timeout, always check that
        it's the instance you need::
    
            timeout = Timeout(1)
            timeout.start()
            try:
                ...
            except Timeout as t:
                if t is not timeout:
                    raise # not my timeout
    
        If the *seconds* argument is not given or is ``None`` (e.g.,
        ``Timeout()``), then the timeout will never expire and never raise
        *exception*. This is convenient for creating functions which take
        an optional timeout parameter of their own. (Note that this is not the same thing
        as a *seconds* value of 0.)
    
        .. caution::
           A *seconds* value less than 0.0 (e.g., -1) is poorly defined. In the future,
           support for negative values is likely to do the same thing as a value
           if ``None``.
    
        .. versionchanged:: 1.1b2
           If *seconds* is not given or is ``None``, no longer allocate a libev
           timer that will never be started.
        .. versionchanged:: 1.1
           Add warning about negative *seconds* values.
    """
    def cancel(self): # reliably restored by inspect
        """ If the timeout is pending, cancel it. Otherwise, do nothing. """
        pass

    def start(self): # reliably restored by inspect
        """ Schedule the timeout. """
        pass

    @classmethod
    def start_new(cls, *args, **kwargs): # real signature unknown
        """
        Create a started :class:`Timeout`.
        
                This is a shortcut, the exact action depends on *timeout*'s type:
        
                * If *timeout* is a :class:`Timeout`, then call its :meth:`start` method
                  if it's not already begun.
                * Otherwise, create a new :class:`Timeout` instance, passing (*timeout*, *exception*) as
                  arguments, then call its :meth:`start` method.
        
                Returns the :class:`Timeout` instance.
        """
        pass

    def _start_new_or_dummy(timeout, exception=None): # reliably restored by inspect
        # no doc
        pass

    def __enter__(self): # reliably restored by inspect
        # no doc
        pass

    def __exit__(self, typ, value, tb): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, seconds=None, exception=None, ref=True, priority=-1, _use_timer=True): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        """
        >>> raise Timeout #doctest: +IGNORE_EXCEPTION_DETAIL
                Traceback (most recent call last):
                    ...
                Timeout
        """
        pass

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return True if the timeout is scheduled to be raised."""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__all__ = [
    'Semaphore',
    'BoundedSemaphore',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}
