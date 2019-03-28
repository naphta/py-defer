import defer
import functools


def test_single_deferred():

    output = []

    @defer.with_defer
    def func():
        output.append("Hello")
        defer.defer(output.append, "World!")

    func()
    assert output == ["Hello", "World!"]


def test_multiple_decorated():

    output_1 = list()
    output_2 = list()

    def dummy_decorator(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            __deferred__ = "I'm a secret variable with the same name."
            f(*args, **kwargs)

        return wrapped

    @defer.with_defer
    @dummy_decorator
    def func_1():
        output_1.append("Hello")
        defer.defer(output_1.append, "World!")

    @dummy_decorator
    @defer.with_defer
    def func_2():
        output_2.append("Hello")
        defer.defer(output_2.append, "World!")

    func_1()
    func_2()

    assert output_1 == ["Hello", "World!"]
    assert output_2 == ["Hello", "World!"]


def test_defer_order():
    output = []

    @defer.with_defer
    def func():
        output.append("Hello")
        defer.defer(output.append, "World")
        defer.defer(output.append, "I'm")
        defer.defer(output.append, "Alive!")

    func()
    assert output == ["Hello", "World", "I'm", "Alive!"]


def test_defer_ends():
    output = []

    @defer.with_defer
    def func():
        output.append("Hello")
        defer.defer(output.append, "I'm")
        defer.defer(output.append, "Alive!")
        output.append("World")

    func()
    assert output == ["Hello", "World", "I'm", "Alive!"]


def test_defer_not_decorated():
    output = []

    def func():
        output.append("Hello")
        defer.defer(output.append, "I'm")
        defer.defer(output.append, "Alive!")
        output.append("World")

    try:
        func()
    except Exception as e:
        assert isinstance(e, ValueError)

    assert output == ["Hello"]


def test_defer_decorated_class():

    @defer.with_defer
    class ExampleClass:

        def __init__(self):
            self.things = list()

        def do_a_thing(self):
            self.things.append(f"Thing {len(self.things) + 1}")
            defer.defer(self.do_a_thing, "Thing added!")

    ec = ExampleClass()

    try:
        ec.do_a_thing()
    except Exception as e:
        assert isinstance(e, ValueError)

    assert ec.things == ["Thing 1"]
