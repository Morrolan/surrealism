__author__ = 'morrolan'

import platform
import surrealism

count = 0

new_file = '/vagrant/results/large_output_{0}.txt'.format(platform.python_version())

with open(new_file, 'wb') as _file:

    _file.writelines("GETSENTENCE()\n")
    while count <= 1000:

        s = surrealism.getsentence()
        _file.writelines(s + "\n")
        count += 1

    _file.writelines("\n\n")
    _file.writelines("GETFAULT()\n")

    while count <= 100:

        s = surrealism.getfault()
        _file.writelines(s + "\n")
        count += 1

    _file.close()

print("COMPLETE")