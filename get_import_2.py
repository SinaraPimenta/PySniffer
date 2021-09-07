import ast
import json
from get_all_paths import get_all_paths 

modules_dict = dict([])

def get_imports(path,mainpath):
    print(path)
    with open(path) as fh:        
       root = ast.parse(fh.read(), path) #obtem o código fonte do caminho especificado

    for node in ast.iter_child_nodes(root): #percorre os nós (Import,ImportFrom,ClassDef, FunctionDef, Assign, Expr, etc)
        get_import_node(node)
    key_list = list(modules_dict.keys())
    modules_list = []
    for k in key_list:
        module_json = {"name": k, "attributes": modules_dict[k]}
        modules_list.append(module_json)

    modules_json = json.dumps(modules_list)
    #print(json.loads(modules_json)[0]['name']) #module name
    #print(json.loads(modules_json)[14]['attributes'])  #module attributes

    final_json = {"dir": path.removeprefix(mainpath), "modules": modules_json}
    
    print(final_json)
    
    return final_json

def get_import_node(node):   
    if isinstance(node, ast.Import):     
        module = []       
        for n in node.names:
            #print("Module:", n.name)
            modules_dict[ str(n.name)] = []
    elif isinstance(node, ast.ImportFrom):  
        module = node.module
        attr = []
        for n in node.names:
            #print("Module:",module, " Attribute:", n.name)
            if (str(module) in modules_dict):
                attr = modules_dict[ str(module)]           
            attr.append(n.name)
            modules_dict[ str(module)] = attr
            attr = []

    elif (isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef) or isinstance(node, ast.ClassDef)): #se for uma função ou classe
        for n in ast.iter_child_nodes(node):  #é necessário verificar os nós dentro 
            get_import_node(n)

def get_modules(mainpath):
    res = get_all_paths(mainpath, "*.py")
    modules = []
    for i in res:
        modules_dict.clear()
        modules.append(get_imports(i, mainpath))
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(modules, f, ensure_ascii=False, indent=4)

get_modules('C:/Users/mariana.helena/Documents/python projects/cherry-picker-main')