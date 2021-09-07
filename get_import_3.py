import ast
import json
from get_all_paths import get_all_paths 
from stdlib_list import stdlib_list

libraries = stdlib_list("3.9")
std_modules_dict = dict([])
modules_dict = dict([])

def get_imports(path,mainpath):
    #print(path)
    with open(path) as fh:        
       root = ast.parse(fh.read(), path) #obtem o código fonte do caminho especificado

    for node in ast.iter_child_nodes(root): #percorre os nós (Import,ImportFrom,ClassDef, FunctionDef, Assign, Expr, etc)
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
    
    #print(final_json)
    
    return std_final_json, final_json

def get_import_node(node):   
    if isinstance(node, ast.Import):     
        module = []       
        for n in node.names:
            #print("Module:", n.name)
            moduleName = str(n.name)
            if moduleName in libraries:
                std_modules_dict[moduleName] = []
            else:
                modules_dict[moduleName] = []
    elif isinstance(node, ast.ImportFrom):  
        module = node.module
        moduleName = str(module)
        attr = []
        for n in node.names:
            #print("Module:",module, " Attribute:", n.name)
            if moduleName in libraries:
                if (moduleName in std_modules_dict):
                    attr = std_modules_dict[moduleName]           
                attr.append(n.name)
                std_modules_dict[moduleName] = attr
            else:
                if (moduleName in modules_dict):
                    attr = modules_dict[moduleName]           
                attr.append(n.name)
                modules_dict[moduleName] = attr
            attr = []

    elif (isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef) or isinstance(node, ast.ClassDef)): #se for uma função ou classe
        for n in ast.iter_child_nodes(node):  #é necessário verificar os nós dentro 
            get_import_node(n)

def get_modules(mainpath):
    res = get_all_paths(mainpath, "*.py")
    modules = []
    std_modules = []
    for i in res:
        modules_dict.clear()
        std_modules_dict.clear()
        stdList, list = get_imports(i, mainpath)
        modules.append(list)
        std_modules.append(stdList)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(modules, f, ensure_ascii=False, indent=4)
    with open('std_data.json', 'w', encoding='utf-8') as f:
        json.dump(std_modules, f, ensure_ascii=False, indent=4)

get_modules('C:/Users/mariana.helena/Documents/python projects/cherry-picker-main')
