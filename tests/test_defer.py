import defer


def test_single_deferred():

    output = []

    @defer.with_defer
    def func():
        output.append("Hello")
        defer.defer(output.append, "World!")

    func()
    assert output == ["Hello", "World!"]


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
