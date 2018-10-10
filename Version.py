# A tuple containing the five components of the version number: major, minor, micro, releaselevel, and serial.
#All values except releaselevel are integers; the release level is 'alpha', 'beta', 'candidate', or 'final'
#The version_info value corresponding to the Python version 2.0 is (2, 0, 0, 'final', 0)
#The components can also be accessed by name, so sys.version_info[0] is equivalent to sys.version_info.major and so on.

#Note : 'sys' module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

import sys
print("Python version")
print (sys.version)
print ("Version info.")
print (sys.version_info)