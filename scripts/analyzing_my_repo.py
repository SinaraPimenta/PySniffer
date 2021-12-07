import json

from logs import log


def analyzing_libraries(dir1='./returns/my_project/libs.json' , dir2='./returns/all_projects/libs.json', 
dir3='./returns/my_project/libs_Py.json', dir4='./returns/all_projects/libs_Py.json'):
    ################## EXTERNAL LIBRARIES #################################
    #My project
    with open(dir1, 'r', encoding='utf8') as f:
        json_data = json.load(f)

    my_libs = set()
    for lib in json_data:
        my_libs.add(lib['name'])

    #All Projects
    with open(dir2, 'r', encoding='utf8') as f:
        json_data = json.load(f)
    all_libs = set()
    for lib in json_data:
        all_libs.add(lib['name'])

    if my_libs.intersection(all_libs) != set():
        print(f'\nExternal libraries also used by the github projects that were analyzed: \n{my_libs.intersection(all_libs)}')
    else:
        print('\n Not exists external libraries also used by the github projects that were analyzed!')

    if my_libs.difference(all_libs) != set():
        print(f'\nExternal libraries not used by the github projects that were analyzed: \n{my_libs.difference(all_libs)}')
    else:
        print('\nNot exists external libraries not used by the github projects that were analyzed!')

    ################## STANDARD LIBRARIES #################################
    #My project
    with open(dir3, 'r', encoding='utf8') as f:
        json_data_Py = json.load(f)

    my_libs_Py = set()
    for lib in json_data_Py:
        my_libs_Py.add(lib['name'])

    #All Projects
    with open(dir4, 'r', encoding='utf8') as f:
        json_data_Py = json.load(f)
    all_libs_Py = set()
    for lib in json_data_Py:
        all_libs_Py.add(lib['name'])

    if my_libs_Py.intersection(all_libs_Py) != set():
        print(f'\nStandard libraries also used by the github projects that were analyzed: \n{my_libs_Py.intersection(all_libs_Py)}')
    else:
        print('\nNot exists standard libraries also used by the github projects that were analyzed!')

    if my_libs_Py.difference(all_libs_Py) != set():
        print(f'\nStandard libraries not used by the github projects that were analyzed: \n{my_libs_Py.difference(all_libs_Py)}')
    else:
        print('\nNot exists standard libraries not used by the github projects that were analyzed!\n')

    return my_libs_Py.intersection(all_libs_Py), my_libs_Py.difference(all_libs_Py), my_libs.intersection(all_libs), my_libs.difference(all_libs)
