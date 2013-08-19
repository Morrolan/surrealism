surrealism
==========

surrealism module for Python
----------------------------


This module allows you to generate surreal sentences and error messages very easily from within your python programs.  


Many thanks go to Raven Black from www.ravenblack.net.  


This module is a derivative work (used with permission) from www.ravenblack.net.  


Credit also goes to Kevan Davis on whose work the surrealism generator at www.ravenblack.net is based on.


Installation
------------

If you have downloaded the source distribution, to install do the following at the commandline: 

::
   
   $ python setup.py install


If you can use and install Python Egg's, you can do:

::

   $ easy_install surrealism


<<<<<<< HEAD
And it will download the latest version from the Python Package Index.
=======
And it will download and install the latest version from the Python Package Index.

You can also do:

::

   $ pip install surrealism


And it will download and install the latest version from the Python Package Index.
>>>>>>> be76eb42a70bc6308f44e46d568c242fd742f921




Usage Examples
--------------

**Generate a surreal sentence**:

::

   >>> import surrealism
   >>> surr = surrealism.Surrealism()
   >>> sen = surr.getsentence()
   
   >>> Why did the Gallifreyan helmet hide apples behind the bright porridge-bowl?  Because it was being penetrated by the will-o'-the-wisp!
   

   
**Generate a surreal error message**:

::

   >>> import surrealism
   >>> surr = surrealism.Surrealism()
   >>> sen = surr.getfault()
   
   >>> jump-lead .c:147: sleepy error before 'stick insect' - 'salt crystal' undeclared.
   
   
Still to do:

<<<<<<< HEAD
- Add ability to read nested #RANDOM elements
- Add the ability to be able to re-use nouns and verbs in the same sentence rather than generating new ones.
- Add more sentences to the database.
=======
Please feel free to leave bug reports and feature requests on the github homepage at https://github.com/Morrolan/surrealism.

All comments are welcome!


Changelog
---------

0.4
---

Urgent bug fix to getfault where returned result was incomplete.
>>>>>>> be76eb42a70bc6308f44e46d568c242fd742f921
