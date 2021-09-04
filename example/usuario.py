class Usuario(object):
    __nome: str
    __login: str
    __senha: str

    def __init__(self, nome="",login="", senha=""):
        self.__nome = nome
        self.__login = login
        self.__senha = senha
    
    def setNome(self,nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome
    
    def getLogin(self):
        return self.__login
    
    def getSenha(self):
        return self.__senha