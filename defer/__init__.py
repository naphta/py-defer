import functools
import contextlib
import types
import typing
import inspect


class Deferred:
    __slots__: typing.List = ["deferred"]
    deferred: typing.List

    def __init__(self):
        self.deferred = list()

    def add(self, f: typing.Callable, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Add a deferred function call.

        :param f: Function to be called
        :param args: Arguments to pass into the function
        :param kwargs: Keyword arguments to pass into the function.
        """
        self.deferred.append(lambda: f(*args, **kwargs))

    def close(self):
        """
        Loop through all deferred functions and call them.

        Method is named close to support contextlib.closing.
        """
        for f in self.deferred:  # ensure deferrals ran synchronously.
            f()


def with_defer(f: typing.Callable) -> typing.Callable:
    """
    Decorate a function to include support for function deferrals.

    :param f: Function to decorate, currently unsupported on classes.
    """

    @functools.wraps(f)
    def wrapper(*args: typing.Any, **kwargs: typing.Any):
        __deferred__: Deferred = Deferred()
        with contextlib.closing(__deferred__):
            return f(*args, **kwargs)

    return wrapper if isinstance(f, types.FunctionType) else f


def defer(f: typing.Callable, *args: typing.Any, **kwargs: typing.Any) -> None:
    """
    Defer a function call until the very end.

    :param f: Function to be called
    :param args: Arguments to pass into the function
    :param kwargs: Keyword arguments to pass into the function.
    """

    # loop the local variables starting from 2 functions up, adding the deferred function
    # if it can find a local with the name `__deferred__` and of type defer.Deferred
    for local in inspect.stack(context=0)[2:]:
        if isinstance(local[0].f_locals.get("__deferred__"), Deferred):
            deferred: Deferred = local[0].f_locals["__deferred__"]
            deferred.add(f, *args, **kwargs)
            return
    else:
        raise ValueError("Function not decorated with `defer.with_defer`")
