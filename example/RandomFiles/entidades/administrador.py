import sys
sys.path.append('src/main/classes')
import usuario
sys.path.append('src/main/entidades')
import bancoDeDados

class Administrador(usuario.Usuario):
    __indice:int
    
    def __init__(self,  nome="",login="", senha="", indice=-1):
        super().__init__(nome, login,senha)
        self.__indice = indice
    
    def indiceSet(self,indice):
        self.__indice = indice
    
    def indiceGet(self):
        return self.__indice

    def buscarCafeicultores(self,mediador):
        return mediador.notify(self, "Buscar")
    
    def cadastrarCafeicultor(self,mediador):
        mediador.notify(self,"Cadastrar")
    
    def editarCafeicultor(self,mediador):
        mediador.notify(self,"Editar")
    
    def excluirCafeicultor(self,mediador):
        mediador.notify(self,"Excluir")
    
    def getCafeicultor(self,mediador):
        return mediador.notify(self,"Get")
    