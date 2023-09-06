from functools import partialmethod


class _F():
    """
    meta class. When used as a decorator, decorates the function input to
    allow
    ```
    decorated @ input (from left to right)
    ```
    """

    def __init__(self, fn, name=None, method=False):
        try:
            self.__name__ = name or fn.__name__
        except:
            self.__name__ = "F"
        self.fn = fn

    def __str__(self):
        return "{} @ ".format(self.__name__)

    def __repr__(self):
        return "{} @ ".format(self.__name__)

    def __imatmul__(self, other):
        return self @ other

    def __rmatmul__(self, left_fn):
        raise NotImplementedError(left_fn)

    def __matmul__(self, other):
        if hasattr(other, '__call__'):
            name = "{} @ {}".format(self.__name__, other.__name__)
            return _F(lambda *args, **kwargs: self.fn(other(*args, **kwargs)), name=name)
        return self.fn(other)

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)


@_F
def F(fn):
    if hasattr(fn, '__call__'):
        _ = _F(fn)
        try:
            _.__name__ = f.__name__
        except:
            _.__name__ = "F"
        return _
    else:
        return fn


def prefixmethod(fn):
    """ decorator that supports class methods. """
    return partialmethod(_F, fn)

# this means fn is a class method that requires `self` as the
# first positional argument.
