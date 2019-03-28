import functools
import contextlib
import typing


class Deferred:

    deferred: typing.List = []

    def add(self, f, *args, **kwargs):
        self.deferred.append(lambda: f(*args, **kwargs))

    def close(self):
        for f in self.deferred:  # ensure deferrals ran synchronously.
            f()


def _defer(
    deferred: typing.List[typing.Callable],
    f: typing.Callable,
    *args: typing.Tuple,
    **kwargs: typing.Dict[str, typing.Any]
):
    deferred += lambda: f(args=args, kwargs=kwargs)


def with_defer(f: typing.Callable):
    @functools.wraps(f)
    def wrapper(*args: typing.Tuple, **kwargs: typing.Dict[str, typing.Any]):
        __deferred__ = Deferred()

        def d(
            func: typing.Callable, *a: typing.Tuple, **kw: typing.Dict[str, typing.Any]
        ):
            __deferred__.add(func, *a, **kw)

        with contextlib.closing(__deferred__):
            return f(defer=d, *args, **kwargs)

    return wrapper
