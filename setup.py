import sys

from setuptools import Command
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = []

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main([
            '--quiet',
            '--capture=no',
            '--tb=native',
            '--doctest-modules',
            '--cov=disciplines',
            '--cov-report=term-missing',
            'tests'
        ]))


class ScrapeCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.distribution.fetch_build_eggs(self.distribution.install_requires)
        import disciplines
        disciplines.main()


setup(
    name='disciplines',
    version='0.1',
    py_modules=['disciplines'],
    install_requires=[
        'requests',
        'beautifulsoup4',
        'numpy',
        'scipy',
        'networkx',
        'matplotlib',
        'pandas',
        'nltk',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'httmock',
        'setuptools',
    ],
    cmdclass={
        'scrape': ScrapeCommand,
    },
)
