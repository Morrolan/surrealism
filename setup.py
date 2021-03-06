
#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as file_desc:
    long_desc = file_desc.read()

setup(name='surrealism',
      version='1.1.0',
      # packages = find_packages(),
      #packages=["surrealism"],
      author='Ian Havelock',
      author_email='ian@morrolan.com',
      url='http://morrolan.github.io/surrealism',
      license='GNU General Public License (GPL)',
      description='Surreal sentence and error message generator.',
      long_description=long_desc,
      platforms=['Windows', 'Unix', 'OS X'],
      download_url="https://pypi.python.org/pypi/surrealism/",
      keywords=["surreal", "surrealism", "error message", "fault"],
      classifiers=
      [
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
	  'Development Status :: 5 - Production/Stable',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Other Audience',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Topic :: Education',
          'Topic :: Communications',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      install_requires=['setuptools'],
      package_data={'surrealism': ['surrealism.sqlite']},
      zip_safe=False,
      )
