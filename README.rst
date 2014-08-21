======================
cookiecutter-pypackage
======================

Cookiecutter template for a Python package. See https://github.com/audreyr/cookiecutter.

I adapted the pypackage from nekroze a little bit for my needs.
The doc has the sphinx theme already installed. There 2 scripts that help
building the apidoc (generates rst files for your packages). The official apidoc
had a buggy formatting.

* Free software: BSD license
* Pytest_ runner: Supports `unittest`, `pytest`, `nose` style tests and more
* Travis-CI_: Ready for Travis Continuous integration testing
* Tox_ testing: Setup to easily test for python 2.6, 2.7, 3.3 and PyPy_
* Sphinx_ docs: Documentation raedy for generation with, for example, ReadTheDocs_
* Wheel_ support: Use the newest python package distribution standard from the get go

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/storax/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Run `tox` to make sure all tests pass.
* Release your package the standard Python way.

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `nekroze/cookiecutter-pypackage`_: The original pypackage, uses unittest
for testing and other minor changes.

Fork This
~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Once you have your fork working, add it to the
Similar Cookiecutter Templates list with a brief explanation. It's up to you
whether or not to rename your fork.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _Pytest: http://pytest.org/
.. _PyPy: http://pypy.org/
.. _Wheel: http://pythonwheels.com
