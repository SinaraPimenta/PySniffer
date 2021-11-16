import json
import os

import scripts.plot_top10 as plot

arr = []
arr_py = []

def list_save_projects_libs(dirName, projects):
    for p in projects:
        project_path = dirName+'/'+p
        read_requirements(project_path)

    ext_libs,std_libs = count_libs()

    #Creating json file
    if 'my_repo' in dirName:
        with open('./returns/my_project/libs.json', 'w', encoding='utf-8') as f:
            json.dump(ext_libs, f, ensure_ascii=False, indent=4)

        with open('./returns/my_project/libs_Py.json', 'w', encoding='utf-8') as f:
            json.dump(std_libs, f, ensure_ascii=False, indent=4)
    else:
        with open('./returns/all_projects/libs.json', 'w', encoding='utf-8') as f:
            json.dump(ext_libs, f, ensure_ascii=False, indent=4)

        with open('./returns/all_projects/libs_Py.json', 'w', encoding='utf-8') as f:
            json.dump(std_libs, f, ensure_ascii=False, indent=4)

        #Plotting top 10
        plot.plotTop10(ext_libs,'Top 10 Libs Ext','Ext')
        plot.plotTop10(std_libs,'Top 10 Libs Std','Std')

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
        elif filename == ("packages_python.txt"):
            name = path+'/'+str(filename)
            with open(name) as infile:
                for line in infile:
                    lib = line.split('==')
                    lib_name = lib[0]
                    if lib_name != '\n':
                        lib_name = lib_name.replace('\n','')
                        arr_py.append(lib_name)

def count_libs():
    myDict = {}
    myDictPy = {}
    myDictReturn = []
    myDictPyReturn = []

    for lib in arr:
        if not lib:
            continue
        elif lib not in myDict.keys():
            myDict[lib] = 1
        else:
            myDict[lib] += 1
    for lib in myDict.keys():
        myDictReturn.append({"name":f"{lib}","amount":f"{myDict[lib]}"})

    for lib in arr_py:
        if not lib:
            continue
        elif lib not in myDictPy.keys():
            myDictPy[lib] = 1
        else:
            myDictPy[lib] += 1
    for lib in myDictPy.keys():
        myDictPyReturn.append({"name":f"{lib}","amount":f"{myDictPy[lib]}"})

    print(f'{"Lib":<34}' + "  Count")
    for k, v in myDict.items():
        print(f'{k:<34}' + "  " + str(v))
    print("Número de libs = " + str(len(myDict)))
    print('\n')
    print(f'{"Lib":<34}' + "  Count")
    for k, v in myDictPy.items():
        print(f'{k:<34}' + "  " + str(v))
    print("Número de libs python = " + str(len(myDictPy)))
    return myDictReturn,myDictPyReturn
