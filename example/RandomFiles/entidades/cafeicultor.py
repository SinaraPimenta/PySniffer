import sys
sys.path.append('src/main/classes')
import usuario

class Cafeicultor(usuario.Usuario):
    __telefone: str
    __cpf: str
    __cidade: str
    __endereco: str
    __agencia_bancaria: str
    __numero_da_conta: str
    __nome_do_banco: str

    def __init__(self, nome="",login="",senha="",telefone="", cpf="", cidade="", endereco="",nome_do_banco="", agencia_bancaria="",numero_da_conta=""):
        super().__init__(nome, login,senha)
        self.__telefone = telefone
        self.__cpf = cpf
        self.__cidade = cidade
        self.__endereco = endereco
        self.__agencia_bancaria = agencia_bancaria
        self.__numero_da_conta = numero_da_conta
        self.__nome_do_banco = nome_do_banco
    
    def nomeGet(self):
        return super().getNome()
    
    def nomeSet(self,nome):
        super().setNome(nome)
    
    def loginGet(self):
        return super().getLogin()
    
    def senhaGet(self):
        return super().getSenha()
    
    def telefoneGet(self):
        return self.__telefone
    
    def telefoneSet(self,telefone):
        self.__telefone = telefone

    def cpfGet(self):
        return self.__cpf

    def cidadeGet(self):
        return self.__cidade
    
    def cidadeSet(self,cidade):
        self.__cidade = cidade

    def enderecoGet(self):
        return self.__endereco
    
    def enderecoSet(self,endereco):
        self.__endereco = endereco
    
    def agenciaGet(self):
        return self.__agencia_bancaria
    
    def agenciaSet(self,agencia):
        self.__agencia_bancaria = agencia

    def contaGet(self):
        return self.__numero_da_conta

    def contaSet(self,conta):
        self.__numero_da_conta = conta
    
    def bancoGet(self):
        return self.__nome_do_banco
    
    def bancoSet(self,banco):
        self.__nome_do_banco = banco

    def atualizaCafeicultor(self,nome:str,telefone:str,endereco:str,cidade:str,banco:str,agencia:str,conta:str):
        self.nomeSet(nome)
        self.telefoneSet(telefone)
        self.enderecoSet(endereco)
        self.cidadeSet(cidade)
        self.bancoSet(banco)
        self.agenciaSet(agencia)
        self.contaSet(conta)

    def buscarCafe(self,mediador):
        return mediador.notify(self, "Buscar")

    def cadastrarCafe(self,mediador):
        mediador.notify(self, "Cadastrar")

    def editarCafe(self,mediador):
        mediador.notify(self,"Editar")

    def excluirCafe(self,mediador):
        mediador.notify(self,"Excluir")
    
    def venderCafe(self,mediador):
        mediador.notify(self,"Vender")
    
    def getCafe(self,mediador):
        return mediador.notify(self, "Get")

    def consultaBd(self,mediador):
        return mediador.notify(self, "Consultar")
    
