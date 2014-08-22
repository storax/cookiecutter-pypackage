#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
import io
import re
import os
import sys


here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


long_description = read('README.rst', 'HISTORY.rst')


setup(
    name='{{ cookiecutter.repo_name }}',
    version=find_version("{{ cookiecutter.repo_name }}", "__init__.py"),
    description='{{ cookiecutter.project_short_description }}',
    long_description=long_description,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    include_package_data=True,
    tests_require=['pytest'],
    install_requires=[
    ],
    cmdclass={'test': PyTest},
    license='MIT',
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    test_suite='{{ cookiecutter.repo_name }}.test.{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    extras_require={
        'testing': ['pytest'],
    }
)
