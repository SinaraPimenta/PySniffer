import ast
import json

from get_all_paths import get_all_own_modules, get_all_paths
from stdlib_list import stdlib_list

libraries = stdlib_list("3.9")
own_modules_list = []
own_packages_list = []
own_folders_list = []
std_modules_dict = dict([])
own_modules_dict = dict([])
modules_dict = dict([])

def get_imports(path,mainpath):
    with open(path) as fh:
       root = ast.parse(fh.read(), path)
    for node in ast.iter_child_nodes(root):
        get_import_node(node)

    key_list = list(std_modules_dict.keys())
    std_modules_list = []
    for k in key_list:
        module_json = {"name": k, "attributes": std_modules_dict[k]}
        std_modules_list.append(module_json)
    std_modules_json = json.dumps(std_modules_list)
    std_final_json = {"dir": path.removeprefix(mainpath), "modules": std_modules_json}

    key_list = list(modules_dict.keys())
    modules_list = []
    for k in key_list:
        module_json = {"name": k, "attributes": modules_dict[k]}
        modules_list.append(module_json)
    modules_json = json.dumps(modules_list)
    final_json = {"dir": path.removeprefix(mainpath), "modules": modules_json}

    key_list = list(own_modules_dict.keys())
    own_modules_list = []
    for k in key_list:
        module_json = {"name": k, "attributes": own_modules_dict[k]}
        own_modules_list.append(module_json)
    own_modules_json = json.dumps(own_modules_list)
    own_final_json = {"dir": path.removeprefix(mainpath), "modules": own_modules_json}
    return std_final_json, final_json, own_final_json

def get_import_node(node):
    if isinstance(node, ast.Import):
        module = []
        for n in node.names:
            moduleName = str(n.name)
            if moduleName in libraries:
                std_modules_dict[moduleName] = []
            elif moduleName in own_modules_list or moduleName in own_packages_list or moduleName in own_folders_list:
                own_modules_dict[moduleName] = []
            else:
                modules_dict[moduleName] = []
    elif isinstance(node, ast.ImportFrom):
        module = node.module
        moduleName = str(module)
        attr = []
        for n in node.names:
            if moduleName in libraries:
                if (moduleName in std_modules_dict):
                    attr = std_modules_dict[moduleName]
                attr.append(n.name)
                std_modules_dict[moduleName] = attr
            elif moduleName in own_modules_list or moduleName in own_packages_list or moduleName in own_folders_list:
                if (moduleName in own_modules_dict):
                    attr = own_modules_dict[moduleName]
                attr.append(n.name)
                own_modules_dict[moduleName] = attr
            elif moduleName == 'None':
                moduleName = n.name
                own_modules_dict[moduleName] = []
            else:
                if (moduleName in modules_dict):
                    attr = modules_dict[moduleName]
                attr.append(n.name)
                modules_dict[moduleName] = attr
            attr = []
    elif (isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef) or isinstance(node, ast.ClassDef)):
        for n in ast.iter_child_nodes(node):
            get_import_node(n)

def get_modules(mainpath):
    global own_modules_list, own_packages_list, own_folders_list
    own_modules_list, own_packages_list, own_folders_list  = get_all_own_modules(mainpath)
    res = get_all_paths(mainpath)
    modules = []
    std_modules = []
    own_modules = []
    for i in res:
        modules_dict.clear()
        std_modules_dict.clear()
        own_modules_dict.clear()
        stdList, list, ownlist = get_imports(i, mainpath)
        modules.append(list)
        std_modules.append(stdList)
        own_modules.append(ownlist)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(modules, f, ensure_ascii=False, indent=4)
    with open('std_data.json', 'w', encoding='utf-8') as f:
        json.dump(std_modules, f, ensure_ascii=False, indent=4)
    with open('own_data.json', 'w', encoding='utf-8') as f:
        json.dump(own_modules, f, ensure_ascii=False, indent=4)

#get_modules('C:/Users/mariana.helena/Documents/python projects/bedevere-master')
get_modules('C:/Users/mariana.helena/Documents/python projects/Projeto_C214_Armazem_MS-main')
#get_modules('C:/Users/mariana.helena/Documents/python projects/cherry-picker-main')
