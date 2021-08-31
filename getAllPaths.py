import os
from fnmatch import fnmatch

def getAllPaths(dirName, pattern):
    pathList = []
    for path, subdirs, files in os.walk(dirName):
        for name in files:
            if fnmatch(name, pattern):
               pathList.append(os.path.join(path, name))
    return pathList

