surrealism
==========

surrealism module for Python
----------------------------


This module allows you to generate surreal sentences and error messages very easily from within your python programs.  


This module is a derivative work (used with permission) from www.ravenblack.net.  


Credit also goes to Kevan Davis on whose work the surrealism generator at www.ravenblack.net is based on.


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
   >>> sentence = surrealism.getsentence()
   >>> print sentence
   >>> If I can get the Pot Noodle to enter Radiohead's Lead Singer, the lego-brick will dilute Julian Assange and I'll be able to spy on Neil Armstrong!

   
**Generate a surreal error message**:

::

   >>> import surrealism
   >>> sentence = surrealism.getfault()
   >>> print sentence
   >>> obelisk.c:471: empty error in 'Spaniard()' - poltergeist is not set to an instance of a triffid.


Please feel free to leave bug reports and feature requests on the github homepage at https://github.com/Morrolan/surrealism.

All comments are welcome!


Changelog
---------

0.5.1
-----
Added basic 

0.5.0
-----

Removed unnecessary Class, now making it even easier and simpler to use.


0.4.1
-----

Minor bug fix to the getfault sentences where 2 periods were printing instead of 1.


0.4
---

Urgent bug fix to getfault where returned result was incomplete.
