__author__ = 'morrolan'

import platform
import surrealism



new_file = '/vagrant/results/large_output_{0}.txt'.format(platform.python_version())

with open(new_file, 'w') as _file:

    count = 0
    #_file.writelines("GETSENTENCE()\n".encode('utf-8'))
    while count <= 1000:

        s = surrealism.getsentence()
        _string = str(s) + "\n"
        _file.writelines(_string)
        count += 1

    #_file.writelines("\n\n")
    #_file.writelines("GETFAULT()\n")

    count = 0

    while count <= 100:

        _string = str(s) + "\n"
        _file.writelines(_string)
        count += 1

    _file.close()

print("COMPLETE")