surrealism
==========

surrealism module for Python
----------------------------


This module allows you to generate surreal sentences and error messages very easily from within your python programs.  


<<<<<<< HEAD
Many thanks go to Raven Black from www.ravenblack.net.  


=======
>>>>>>> be76eb42a70bc6308f44e46d568c242fd742f921
This module is a derivative work (used with permission) from www.ravenblack.net.  


Credit also goes to Kevan Davis on whose work the surrealism generator at www.ravenblack.net is based on.


Installation
------------

If you have downloaded the source distribution, to install do the following at the commandline: 

::
   
   $ python setup.py install


<<<<<<< HEAD
If you can use and install Python Egg's, you can do:
=======
Or using easy_install:
>>>>>>> be76eb42a70bc6308f44e46d568c242fd742f921

::

   $ easy_install surrealism


And it will download and install the latest version from the Python Package Index.

<<<<<<< HEAD
You can also do:
=======
Or pip:
>>>>>>> be76eb42a70bc6308f44e46d568c242fd742f921

::

   $ pip install surrealism


And it will download and install the latest version from the Python Package Index.




Usage Examples
--------------

**Generate a surreal sentence**:

::

   >>> import surrealism
<<<<<<< HEAD
   >>> sentence = surrealism.getsentence()
   >>> print sentence
   >>> Why did the Gallifreyan helmet hide apples behind the bright porridge-bowl?  Because it was being penetrated by the will-o'-the-wisp!
=======
   >>> surreal = surrealism.Surrealism()
   >>> sentence = surreal.getsentence()
   
   >>> If I can get the Pot Noodle to enter Radiohead's Lead Singer, the lego-brick will dilute Julian Assange and I'll be able to spy on Neil Armstrong!
>>>>>>> be76eb42a70bc6308f44e46d568c242fd742f921
   

   
**Generate a surreal error message**:

::

   >>> import surrealism
<<<<<<< HEAD
   >>> sentence = surrealism.getfault()
   >>> print sentence
   >>> obelisk.c:471: empty error in 'Spaniard()' - poltergeist is not set to an instance of a triffid.
   
   
Still to do:
=======
   >>> surreal = surrealism.Surrealism()
   >>> fault = surreal.getfault()
   
   >>> jump-lead .c:147: sleepy error before 'stick insect' - 'salt crystal' undeclared.
   
>>>>>>> be76eb42a70bc6308f44e46d568c242fd742f921

Please feel free to leave bug reports and feature requests on the github homepage at https://github.com/Morrolan/surrealism.

All comments are welcome!


Changelog
---------

<<<<<<< HEAD
0.5.0
-----

Removed unnecessary Class, now making it even easier and simpler to use.


0.4.1
-----

Minor bug fix to the getfault sentences where 2 periods were printing instead of 1.
=======
0.4.1
-----

Minor database tweak for error messages.
>>>>>>> be76eb42a70bc6308f44e46d568c242fd742f921


0.4
---

Urgent bug fix to getfault where returned result was incomplete.