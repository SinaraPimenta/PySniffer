import ast
from collections import namedtuple

Import = namedtuple("Import", ["module", "name", "alias"])

def get_imports(path):
    with open(path) as fh:        
       root = ast.parse(fh.read(), path) #obtem o código fonte do caminho especificado

    for node in ast.iter_child_nodes(root): #percorre os nós (Import,ImportFrom,ClassDef, FunctionDef, Assign, Expr, etc)
        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):  
            module = node.module.split('.')
        else:
            continue

        for n in node.names:
            yield Import(module, n.name.split('.'), n.asname)

#for imp in get_imports("./test.py"): 
    #print(imp)
