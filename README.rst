surrealism
==========

surrealism module for Python
----------------------------

|   |license|   |versions|  |status|
|   |test-status|   |quality-status|    |docs|  |code-cov|
|   |kit|   |downloads| |format|    |repos|
|   |stars| |forks|


This module allows you to generate surreal sentences and error messages very easily from within your python programs.  


Installation
------------

If you have downloaded the source distribution, to install do the following at the commandline: 

::
   
   $ python setup.py install


Or using easy_install:

::

   $ easy_install surrealism


And it will download and install the latest version from the Python Package Index.


Or pip:

::

   $ pip install surrealism


And it will download and install the latest version from the Python Package Index.




Usage Examples
--------------

**Generate a surreal sentence**:

::

   >>> import surrealism
   
   >>> sentence = surrealism.get_sentence()
   
   >>> print sentence
   
   >>> If I can get the Pot Noodle to enter Radiohead's Lead Singer, the lego-brick will dilute Julian Assange and I'll be able to spy on Neil Armstrong!

You can also specify an integer representing the relevant row ID from the database in order to return a specific sentence:

::

   >>> import surrealism
   
   >>> sentence = surrealism.get_sentence(39)
   
   >>> print sentence
   
   >>> Don't drop things on X-Wings - get blood out of deep-fat friers!

   
**Generate a surreal error message**:

::

   >>> import surrealism
   
   >>> print surrealism.get_fault()
   
   >>> thing.c:466: fearsome error in 'blow-up doll()' - missing thing-a-ma-jig.

You can also specify an integer representing the relevant row ID from the database in order to return a specific sentence:

::

   >>> import surrealism
   
   >>> print surrealism.get_fault(3)
   
   >>> Traceback (most recent call last):  File '/party popper/fighter plane/glistening_seashell/anti-depressant.py', line 20, in straggly_particle accelerator.  waterproofError: salmon mousse did not deep-fry hand-drill.



Please feel free to leave bug reports and feature requests on the github homepage at https://github.com/Morrolan/surrealism.

All comments are welcome!

License
-------
.. |versions| image: https://img.shields.io/pypi/pyversions/coverages.svg?logo=python&logoColor=FBE072
    :target: https://pypi.org/projects/surrealism/
.. |status| image: https://img.shields.io/pypi/status/coverages.svg
    :target: https://pypi.org/projects/surrealism/
.. |downloads| image: https://img.shields.io/pypi/dw/coverages.svg
    :target: https://pypi.org/projects/surrealism/
.. |license| image: https://img.shields.io/pypi/l/coverages.svg
    :target: https://pypi.org/projects/surrealism/
.. |format| image: https://img.shields.io/pypi/format/coverages.svg
    :target: https://pypi.org/projects/surrealism/