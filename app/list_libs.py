import os

arr = []

def list_projects_libs(dirName, projects):    
    for p in projects:
        project_path = dirName+'/'+p
        read_requirements(project_path)
    return count_libs()

def list_libs(dirName):    
    read_requirements(dirName)
    return arr

def read_requirements(path):
    for filename in os.listdir(path):      
        if filename == ("requirements.txt"):   
            name = path+'/'+str(filename)
            with open(name) as infile:
                for line in infile:
                    lib = line.split('==')
                    lib_name = lib[0]
                    if lib_name != '\n':
                        arr.append(lib_name)

def count_libs():
    myDict = {}
    for lib in arr:
        if not lib:                     
            continue
        elif lib not in myDict.keys():  
            myDict[lib] = 1
        else:                           
            myDict[lib] += 1
    print(f'{"Lib":<34}' + "  Count")
    for k, v in myDict.items():
        print(f'{k:<34}' + "  " + str(v))
    print("Número de libs = " + str(len(myDict)))
    return myDict