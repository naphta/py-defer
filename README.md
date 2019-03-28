[![image](https://img.shields.io/pypi/v/py-defer.svg)](https://pypi.org/project/py-defer/)
[![image](https://img.shields.io/pypi/l/py-defer.svg)](https://pypi.org/project/py-defer/)
[![image](https://img.shields.io/pypi/pyversions/py-defer.svg)](https://pypi.org/project/py-defer/)
[![travis-ci.org](https://travis-ci.org/naphta/py-defer.svg?branch=master)](https://travis-ci.org/naphta/py-defer)
[![codecov.io](https://codecov.io/github/naphta/py-defer/coverage.svg?branch=master)](https://codecov.io/github/naphta/py-defer)
[![image](https://img.shields.io/github/contributors/naphta/py-defer.svg)](https://github.com/naphta/py-defer/graphs/contributors)
[![image](https://img.shields.io/badge/say%20thanks-!-1EAEDB.svg)](https://saythanks.io/to/naphta)

Defer
============
Add a simple golang-esque deferral system for python.

# Usage

```
import defer


@defer.with_defer
def example_function():
    print("Hello")
    defer.defer(print, "!")
    print("World")
    
example_function()
> Hello
> World
> !
```