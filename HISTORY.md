1.1.0 (2019-03-28)
----------------------
- Add support for coexisting with other decorators in any order.
- Improve test coverage.

1.0.0 (2019-03-28)
----------------------
- Update defer function to be available globally, as 
  opposed to passing in a callable argument to the
  decorated function. 
- Version to 1.0 as it has breaking API changes vs 0.x
- Add MyPy type checking to tests
- Add automatic stub generation from MyPy (via setup.py)
- Remove attr dependency

0.0.2 (2019-03-28)
----------------------
- Update README
    - add shields
- Add travis build
- Add code coverage
- Drop accidental support of versions older than 3.6

0.0.1 (2019-03-28)
----------------------
- Initial concept and implementation.