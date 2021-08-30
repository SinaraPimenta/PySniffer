import ast

def findDecorators(node):  #getDecorators inside a function
    res={}
    res[node.name] = [ast.dump(e) for e in node.decorator_list]
    print(res)

def getFunctionNode(node):
    if (isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef)): #se for uma função 
        findDecorators(node) #busca os nomes dos decorators associados a ela
    elif isinstance(node, ast.ClassDef): #se for uma classe
        findDecorators(node) #busca os nome dos decorators associados a ela
        for n in ast.iter_child_nodes(node):  #e, é necessário verificar os nós dentro dela
            getFunctionNode(n)


def get_decorators(path):
    with open(path) as fh:        
       root = ast.parse(fh.read(), path) #obtem o código fonte do caminho especificado
    for node in ast.iter_child_nodes(root): #percorre os nós (Import,ImportFrom,ClassDef, FunctionDef, Assign, Expr, etc)
        getFunctionNode(node) #vasculha os nós filhos até encontrar um nó que seja uma função

FILE_PATH = './test.py'
get_decorators(FILE_PATH)


