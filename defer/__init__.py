import functools
import contextlib
import typing
import inspect


class Deferred:
    __slots__ = []
    deferred: typing.List = []

    def add(self, f, *args, **kwargs):
        self.deferred.append(lambda: f(*args, **kwargs))

    def close(self):
        for f in self.deferred:  # ensure deferrals ran synchronously.
            f()


def with_defer(f: typing.Callable):
    @functools.wraps(f)
    def wrapper(*args: typing.Tuple, **kwargs: typing.Dict[str, typing.Any]):
        __deferred__ = Deferred()
        with contextlib.closing(__deferred__):
            return f(*args, **kwargs)

    return wrapper


def defer(f: typing.Callable, *args: typing.Tuple, **kwargs: typing.Dict[str, typing.Any]):
    # inspect the local variables from 2 functions up
    # this is to find the wrapped function variables.
    wrapped_locals = inspect.stack(context=0)[2][0].f_locals
    if "__deferred__" not in wrapped_locals:
        raise ValueError("Function not decorated with `defer.with_defer`")
    wrapped_locals['__deferred__'].add(f, *args, **kwargs)