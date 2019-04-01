<!-- @prettier -->

# Defer

[![PyPi-version](https://img.shields.io/pypi/v/py-defer.svg?style=flat-square)](https://pypi.org/project/py-defer/)
[![PyPi-versions](https://img.shields.io/pypi/pyversions/py-defer.svg?style=flat-square)](https://pypi.org/project/py-defer/)
[![PyPi-license](https://img.shields.io/pypi/l/py-defer.svg?style=flat-square)](https://pypi.org/project/py-defer/)
[![Travis CI](https://img.shields.io/travis/naphta/py-defer.svg?style=flat-square)](https://travis-ci.org/naphta/py-defer)
[![CodeCov](https://img.shields.io/codecov/c/github/naphta/py-defer.svg?style=flat-square)](https://codecov.io/github/naphta/py-defer)
[![Codacy](https://img.shields.io/codacy/grade/3a5de3a9d2544c60be2e45d4548a97cb.svg?style=flat-square)](https://www.codacy.com/app/jake_5/py-defer?utm_source=github.com&utm_medium=referral&utm_content=naphta/py-defer&utm_campaign=Badge_Grade)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)
[![Code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/ambv/black)
[![Thanks](https://img.shields.io/badge/say%20thanks-!-1EAEDB.svg?style=flat-square)](https://saythanks.io/to/naphta)

Add a simple golang-esque deferral system for python.

## TODO

- [x] Add deferrals for a function
- [x] Tests
- [x] 95% testing coverage
- [ ] Add deferrals for a class
- [ ] Add deferrals for a module

## Example

```text
In [1]: import defer

In [2]: @defer.with_defer
   ...: def example_function():
   ...:     print("Hello")
   ...:     defer.defer(print, "!")
   ...:     print("World")
   ...:

In [3]: example_function()
Hello
World
!
```
