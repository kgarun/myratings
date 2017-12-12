=========
myratings
=========


.. image:: https://img.shields.io/pypi/v/myratings.svg
        :target: https://pypi.python.org/pypi/myratings

.. image:: https://img.shields.io/travis/kgarun/myratings.svg
        :target: https://travis-ci.org/kgarun/myratings

.. image:: https://readthedocs.org/projects/myratings/badge/?version=latest
        :target: https://myratings.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/kgarun/myratings/shield.svg
     :target: https://pyup.io/repos/github/kgarun/myratings/
     :alt: Updates


Displays ratings of the user from various competitive programming sites in the terminal !!


* Free software: MIT license
* Documentation: https://myratings.readthedocs.io.


Features
--------

* Mode 1:
        In this mode user handles and ratings are stored in the disk when user enters them 
        for the first time so that the user need not enter them in the future and also it 
        provides a comparison summary between old and new ratings.It is the default mode.


* Mode 2:
        If it is not possible to maintain log, users can still view their
        ratings by simply selecting competitive programming site option number
        and entering handle.
       
Installation 
-------------
Type the following command in the terminal::

 pip install myratings



Usage
-----


* Type "myratings" from the commandline

For the first time users are supposed to enter their respective handles,

.. image:: https://user-images.githubusercontent.com/21175650/33887427-a1af9780-df41-11e7-8fbb-b44b6fbd3419.png
     :alt: Demo1


On subsequent usage output will resemble the following :

.. image:: https://user-images.githubusercontent.com/21175650/33887437-a69a8ffc-df41-11e7-9ac3-6fecc0483c40.png
     :alt: Demo2



Configuration
--------------

To add or update handle type the following command::

 myratings config

To use myratings in a project : 
-------------------------------

Simply type the following import statement::
 
 import myratings

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

