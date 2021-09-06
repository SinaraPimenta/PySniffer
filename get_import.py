import ast, json

modules_dict = dict([])

def get_imports(path):
    with open(path) as fh:        
       root = ast.parse(fh.read(), path) #obtem o código fonte do caminho especificado

    for node in ast.iter_child_nodes(root): #percorre os nós (Import,ImportFrom,ClassDef, FunctionDef, Assign, Expr, etc)
        if isinstance(node, ast.Import):
            module = []
            for n in node.names:
                modules_dict[ str(n.name)] = []
        elif isinstance(node, ast.ImportFrom):  
            module = node.module
            attr = []
            for n in node.names:
                if (str(module) in modules_dict):
                    attr = modules_dict[ str(module)]           
                attr.append(n.name)
                modules_dict[ str(module)] = attr
                attr = []
        else:
            continue

    key_list = list(modules_dict.keys())
    modules_list = []
    for k in key_list:
        module__json = {"name": k, "attributes": modules_dict[k]}
        modules_list.append(module__json)

    modules_json = json.dumps(modules_list)

    final__json = {"dir": path, "modules": modules_json}
    
    print(final__json)
    return final__json

get_imports("./example/example.py")



