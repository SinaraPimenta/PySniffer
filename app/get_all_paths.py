import os
from fnmatch import fnmatch

pattern = "*.py"

def get_all_paths(dirName):
    pathList = []
    for path, subdirs, files in os.walk(dirName):
        for name in files:
            if fnmatch(name, pattern):
               pathList.append(os.path.join(path, name))
    return pathList

def get_all_own_modules(dirName):
    moduleList = []
    packageList = []
    folderList = []
    for path, subdirs, files in os.walk(dirName):
        for name in files:
            if fnmatch(name, pattern):

                moduleName = os.path.join(path, name).removeprefix(path + "\\")
                moduleName = moduleName.removesuffix(pattern.removeprefix("*"))
                if (moduleName not in moduleList):
                    moduleList.append(moduleName)

                packageName = os.path.join(path, name).removeprefix(dirName + "\\")
                packageName = packageName.removesuffix(pattern.removeprefix("*"))
                packageName = packageName.replace("\\", ".")
                if (packageName not in packageList):
                    packageList.append(packageName)

                folderName = path.removeprefix(dirName + "\\")
                if (folderName != dirName):
                    folderName = folderName.replace("\\", ".")
                    if (folderName not in folderList):
                        folderList.append(folderName)


    return moduleList, packageList, folderList


#get_all_own_modules('C:/Users/mariana.helena/Documents/python projects/bedevere-master')
#get_all_own_modules('C:/Users/mariana.helena/Documents/python projects/Projeto_C214_Armazem_MS-main')
