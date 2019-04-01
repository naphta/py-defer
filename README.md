Defer
============

 [![PyPi-version](https://img.shields.io/pypi/v/py-defer.svg)](https://pypi.org/project/py-defer/)
 [![PyPi-license](https://img.shields.io/pypi/l/py-defer.svg)](https://pypi.org/project/py-defer/)
 [![PyPi-versions](https://img.shields.io/pypi/pyversions/py-defer.svg)](https://pypi.org/project/py-defer/)
 [![Travis CI](https://travis-ci.org/naphta/py-defer.svg?branch=master)](https://travis-ci.org/naphta/py-defer)
 [![CodeCov](https://codecov.io/github/naphta/py-defer/coverage.svg?branch=master)](https://codecov.io/github/naphta/py-defer)
 [![Codacy](https://api.codacy.com/project/badge/Grade/3a5de3a9d2544c60be2e45d4548a97cb)](https://www.codacy.com/app/jake_5/py-defer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=naphta/py-defer&amp;utm_campaign=Badge_Grade)
 [![Contributors](https://img.shields.io/github/contributors/naphta/py-defer.svg)](https://github.com/naphta/py-defer/graphs/contributors)
 [![Thanks](https://img.shields.io/badge/say%20thanks-!-1EAEDB.svg)](https://saythanks.io/to/naphta)

Add a simple golang-esque deferral system for python.

## Example

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