surrealism
==========

[![Build Status](https://travis-ci.org/Morrolan/surrealism.svg?branch=master)](https://travis-ci.org/Morrolan/surrealism)
[![Coverage Status](https://coveralls.io/repos/Morrolan/surrealism/badge.png?branch=master)](https://coveralls.io/r/Morrolan/surrealism?branch=master)
[![PyPI](http://img.shields.io/pypi/dm/surrealism.svg)](http://img.shields.io/pypi/dm/surrealism.svg)
[![Gitter](https://badges.gitter.im/Morrolan/surrealism.png)](https://gitter.im/Morrolan/surrealism)


surrealism module for Python
----------------------------


This module allows you to generate surreal sentences and error messages very easily from within your python programs.  


Installation
------------

If you have downloaded the source distribution, to install do the following at the commandline: 

   
   `$ python setup.py install`

Or using easy_install:


   `$ easy_install surrealism`


And it will download and install the latest version from the Python Package Index.


Or pip:


   `$ pip install surrealism`


And it will download and install the latest version from the Python Package Index.




Usage Examples
--------------

**Generate a surreal sentence**:

    >>> import surrealism
    >>> sentence = surrealism.getsentence()`
    >>> print sentence
    >>> If I can get the Pot Noodle to enter Radiohead's Lead Singer, the lego-brick will dilute Julian Assange and I'll be able to spy on Neil Armstrong!

You can also specify an integer representing the relevant row ID from the database in order to return a specific sentence:


    >>> import surrealism
    >>> sentence = surrealism.getsentence(39)
    >>> print sentence
    >>> Don't drop things on X-Wings - get blood out of deep-fat friers!

   
**Generate a surreal error message**:

    >>> import surrealism
    >>> print surrealism.getfault()
    >>> thing.c:466: fearsome error in 'blow-up doll()' - missing thing-a-ma-jig.

You can also specify an integer representing the relevant row ID from the database in order to return a specific sentence:


    >>> import surrealism
    >>> print surrealism.getfault(3)
    >>> Traceback (most recent call last):  File '/party popper/fighter plane/glistening_seashell/anti-depressant.py', line 20, in straggly_particle accelerator.  waterproofError: salmon mousse did not deep-fry hand-drill.



Please feel free to leave bug reports and feature requests on the github homepage at https://github.com/Morrolan/surrealism.

All comments are welcome!

