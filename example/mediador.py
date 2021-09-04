from __future__ import annotations
from abc import ABC
import sys
sys.path.append('src/main/model')
import sacaCafe
import cafeicultor
sys.path.append('src/main/controller')
import bancoDeDados

class MediadorInterface(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    def notify(self, sender: object, event: str, colecao: str, indice:int, login:str) -> None:
        pass

class MediadorDoCafeicultor(MediadorInterface):
    def __init__(self,colecao:str, bd: bancoDeDados.BancoDeDados, cafe: sacaCafe.SacaDeCafe = None, indice="",login="") -> None:
        self._bd = bd
        self._bd.mediator = self
        self._cafe = cafe
        if cafe:
            self._cafe.mediator = self
        self._colecao = colecao
        self._indice = indice
        self._login = login

    def notify(self, sender: object, event: str) -> None:
        if event == "Buscar":
            return self._bd.buscarSacasDeCafe(self._login,self._colecao)
        elif event == "Cadastrar":
            self._bd.cadastrarSacasDeCafe(self._cafe,self._colecao)
            self._bd.adicionarNalistaCafe(self._cafe)
        elif event == "Editar":
            self._bd.alterarSacaDeCafe(self._cafe,self._colecao)
            self._bd.substituiCafe(self._cafe)
        elif event == "Excluir":
            id = self._cafe.idGet()
            indice = self._cafe.indiceGet()
            self._bd.deletarSacaDeCafe(id,self._colecao)
            self._bd.removerDalistaCafe(indice)
        elif event == "Vender":
            self._bd.venderSacaDeCafe(self._cafe,self._colecao)
            self._bd.substituiCafe(self._cafe) 
        elif event == "Get":
            return self._bd.getCafe(self._indice)
        elif event == "Consultar":
            return self._bd.buscaNoBD(self._login,self._colecao)

class MediadorDoAdministrador(MediadorInterface):
    def __init__(self,colecao:str, bd: bancoDeDados.BancoDeDados, cafeicultor: cafeicultor.Cafeicultor = None,indice="")->None:
        self._bd = bd
        self._bd.mediator = self
        self._cafeicultor = cafeicultor
        if cafeicultor:
            self._cafeicultor.mediator = self
        self._colecao = colecao
        self._indice = indice

    def notify(self, sender: object, event: str) -> None:
        if event == "Buscar":
            return self._bd.buscarCafeicultores(self._colecao)
        elif event == "Cadastrar":
            self._bd.cadastrarCafeicultor(self._cafeicultor,self._colecao)
            self._bd.adicionarNalistaCafeicultor(self._cafeicultor)
        elif event == "Editar":
            self._bd.alterarDadosDoCafeicultor(self._cafeicultor,self._colecao)
            self._bd.substituiCafeicultor(self._indice,self._cafeicultor)
        elif event == "Excluir":
            self._bd.deletarCafeicultor(self._cafeicultor.loginGet(),self._colecao)
            self._bd.removerDalistaCafeicultor(self._indice)
        elif event == "Get":
            return self._bd.getCafeicultor(self._indice)
        
        

