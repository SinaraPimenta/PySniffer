import os
from fnmatch import fnmatch

pattern = "*.py"

def count_files(dirName):
    count = 0
    for path, subdirs, files in os.walk(dirName):
        for name in files:
            if fnmatch(name, pattern):
               count += 1
    return count

def get_projects(dirName):
    total = 0
    projects_dict = dict([])
    projects = os.listdir(dirName)
    for p in projects:
        project_path = dirName+'/'+p
        count = count_files(project_path)
        total += count
        projects_dict[p] = count
    return projects_dict, total



