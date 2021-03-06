""" test models in the distribution

"""
import os
import sys
import unittest
from fnmatch import fnmatch
import opensim as om
root = os.getcwd()
pattern = "*.osim"

osimpaths = list()
modelNames = list()

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            osimpaths.append(os.path.join(path, name))
            modelNames.append(name)

for i in range(len(osimpaths)):
    print("\n\n\n" + 80 * "=" + "\nLoading model '%s'" % osimpaths[i] + "\n" + 80 * "-")
    # Without this next line, the print above does not necessarily
    # precede OpenSim's output.
    sys.stdout.flush()
    try:
        model = om.Model(osimpaths[i])
        s = model.initSystem()
    except Exception as e:
        print("Oops, Model '%s' failed:\n%s" % (modelNames[i], e.message))
        sys.exit(1)
        
print("All models loaded successfully.")


