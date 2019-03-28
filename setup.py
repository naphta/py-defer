#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py
import os
import sys

from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        try:
            from multiprocessing import cpu_count

            self.pytest_args = [
                "-n",
                str(cpu_count()),
                "--boxed",
                "--mypy",
                "--ignore=setup.py",
            ]
        except (ImportError, NotImplementedError):
            self.pytest_args = ["-n", "1", "--boxed", "--mypy", "--ignore=setup.py"]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python -m mypy.stubgen -m defer -o .")
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

packages = ["defer"]

requires = ["attr>=0.3.1"]
test_requirements = [
    "pytest-cov>=2.6.1",
    "pytest>=4.3.1",
    "pytest-xdist>=1.27.0",
    "pytest-cov>=2.6.1",
]

about = {}
with open(os.path.join(here, "defer", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()
with open("HISTORY.md", "r", "utf-8") as f:
    history = f.read()


setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=packages,
    package_data={"": ["LICENSE"], "defer": ["*.pyi"]},
    package_dir={"defer": "defer"},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requires,
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    cmdclass={"test": PyTest},
    tests_require=test_requirements,
)
