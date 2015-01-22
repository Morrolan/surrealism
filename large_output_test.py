__author__ = 'morrolan'

import platform

import surrealism


new_file = '/vagrant/results/large_output_{0}.txt'.format(platform.python_version())

with open(new_file, 'w') as _file:

    counter = 0
    while counter <= 1000:

        s = surrealism.getsentence()
        _string = str(s) + "\n"
        _file.writelines(_string)
        counter += 1

    _sep = "\n\n\n\n\n\n\n\n\n\n\n\n"
    _file.writelines(_sep)

    counter = 0
    while counter <= 100:

        s = surrealism.getfault()
        _string = str(s) + "\n"
        _file.writelines(_string)
        counter += 1

    _file.close()

print("\nLarge output test:  COMPLETE\n")