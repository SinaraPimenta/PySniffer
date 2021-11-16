import json

from logs import log


def analyzing_libraries():
    #My project
    with open('./returns/my_project/libs.json', 'r', encoding='utf8') as f:
        json_data = json.load(f)

    my_libs = set()
    for lib in json_data:
        my_libs.add(lib['name'])

    #All Projects
    with open('./returns/all_projects/libs.json', 'r', encoding='utf8') as f:
        json_data = json.load(f)
    all_libs = set()
    for lib in json_data:
        all_libs.add(lib['name'])

    log('i',f'External libraries also used by the github projects that were analyzed: {my_libs.intersection(all_libs)}')
    log('i',f'External libraries not used by the github projects that were analyzed: {my_libs.difference(all_libs)}')

    #My project
    with open('./returns/my_project/libs_Py.json', 'r', encoding='utf8') as f:
        json_data_Py = json.load(f)

    my_libs_Py = set()
    for lib in json_data_Py:
        my_libs_Py.add(lib['name'])

    #All Projects
    with open('./returns/all_projects/libs_Py.json', 'r', encoding='utf8') as f:
        json_data_Py = json.load(f)
    all_libs_Py = set()
    for lib in json_data_Py:
        all_libs_Py.add(lib['name'])

    log('i',f'Python libraries also used by the github projects that were analyzed: {my_libs_Py.intersection(all_libs_Py)}')
    log('i',f'Python libraries not used by the github projects that were analyzed: {my_libs_Py.difference(all_libs_Py)}')