import sys
sys.path.append('src/main/classes')
import administrador 
import cafeicultor 
import unittest
from unittest import TestCase
import pymongo
sys.path.append('src/main/entidades')
import mediador
import bancoDeDados

class AdministradorTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        #Configuração do BD:
        cls.cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
        cls.db = cls.cliente["ArmazemMS"] 
        cls.colecao = "Teste_Usuarios"
        cls.db.Teste_Usuarios.delete_many({}) #limpar a coleção antes de fazer os testes
        #Objetos:
        cls.a = administrador.Administrador("Admin","admin@inatel.br","Admin#2020")
        cls.c = cafeicultor.Cafeicultor("Joao","joao123@gmail.com","teste123","3534-9965","15923678941","Itamogi","Sítio A","Banco do Brasil","8218-X","895-9")
        cls.b = bancoDeDados.BancoDeDados()

    def test_buscarCafeicultorBdVazio(self):
        #Buscar cafeicultor/Resposta:
        m = mediador.MediadorDoAdministrador(self.colecao,self.b)
        resposta = self.a.buscarCafeicultores(m)
        #Valor esperado:
        esperado = '<table class="table" id="tabela"><thead><tr><th scope="col">#</th><th scope="col">Cafeicultor</th><th scope="col">Telefone</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody></tbody></table>'
        #Comparação:
        self.assertEqual(esperado,resposta)
    
    def test_buscarCafeicultor(self):
        #Cadastrar cafeicultor:
        m = mediador.MediadorDoAdministrador(self.colecao,self.b,self.c)
        self.a.cadastrarCafeicultor(m) 
        #Buscar cafeicultor/Resposta:
        m1 = mediador.MediadorDoAdministrador(self.colecao,self.b)
        resposta = self.a.buscarCafeicultores(m1)
        #Valor esperado: 
        esperado='<table class="table" id="tabela"><thead><tr><th scope="col">#</th><th scope="col">Cafeicultor</th><th scope="col">Telefone</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody><tr><th scope="row">0</th><td class="nome">Joao</td><td >3534-9965</td><td><button type="button" class="btn btn-primary" id="verCafeicultor" onclick="verCafeicultor(0)">Ver</button></td><td><button type="button" class="btn btn-primary" id="editarCafeicultor" onclick="editarCafeicultor(0)">Editar</button></td> </tr></tbody></table>'
        #Comparação:
        self.assertEqual(esperado,resposta)
        #Excluir cafeicultor:
        m2 = mediador.MediadorDoAdministrador(self.colecao,self.b,self.c,indice=0)
        self.c.excluirCafe(m2)
    
    def test_cadastrarCafeicultor(self):
        #Cadastrar cafeicultor:
        m = mediador.MediadorDoAdministrador(self.colecao,self.b,self.c)
        self.a.cadastrarCafeicultor(m)
        #Obter cafeicultor/Resposta:
        m2 = mediador.MediadorDoAdministrador(self.colecao,self.b,indice=0)
        resposta = self.a.getCafeicultor(m2)
        #Comparações:
        self.assertEqual("Joao",resposta.nomeGet()) 
        self.assertEqual("joao123@gmail.com",resposta.loginGet())
        self.assertEqual("teste123",resposta.senhaGet()) 
        self.assertEqual("3534-9965",resposta.telefoneGet())
        self.assertEqual("15923678941",resposta.cpfGet())
        self.assertEqual("Itamogi",resposta.cidadeGet())
        self.assertEqual("Sítio A",resposta.enderecoGet())
        self.assertEqual("Banco do Brasil",resposta.bancoGet()) 
        self.assertEqual("8218-X",resposta.agenciaGet()) 
        self.assertEqual("895-9",resposta.contaGet()) 
        #Excluir cafeicultor:
        m3 = mediador.MediadorDoAdministrador(self.colecao,self.b,self.c,indice=0)
        self.c.excluirCafe(m3) 
    
    def test_editarCafeicultor(self):
        #Cadastrar cafeicultor:
        m = mediador.MediadorDoAdministrador(self.colecao,self.b,self.c)
        self.a.cadastrarCafeicultor(m) 
        #Novo cafeicultor:
        self.cafeicultorAlterado = cafeicultor.Cafeicultor("Joao Pedro","joao123@gmail.com","teste123","3534-9965","15923678941","Pouso Alegre","Sítio A","Bradesco","8156-0","1234-9")
        #Editar cafeicultor:
        m2= mediador.MediadorDoAdministrador(self.colecao,self.b,self.cafeicultorAlterado,indice=0)
        self.a.editarCafeicultor(m2)
        #Obter cafeicultor/Resposta:
        m3 = mediador.MediadorDoAdministrador(self.colecao,self.b,indice=0)
        resposta = self.a.getCafeicultor(m3)
        #Comparações:
        self.assertEqual("Joao Pedro",resposta.nomeGet()) 
        self.assertEqual("joao123@gmail.com",resposta.loginGet())
        self.assertEqual("teste123",resposta.senhaGet()) 
        self.assertEqual("3534-9965",resposta.telefoneGet())
        self.assertEqual("15923678941",resposta.cpfGet())
        self.assertEqual("Pouso Alegre",resposta.cidadeGet())
        self.assertEqual("Sítio A",resposta.enderecoGet())
        self.assertEqual("Bradesco",resposta.bancoGet()) 
        self.assertEqual("8156-0",resposta.agenciaGet()) 
        self.assertEqual("1234-9",resposta.contaGet()) 
        #Excluir cafeicultor:
        m5 = mediador.MediadorDoAdministrador(self.colecao,self.b,self.c,indice=0)
        self.a.excluirCafeicultor(m5) 
    
    def test_excluirCafeicultor(self):
        #Cadastrar cafeicultor:
        m = mediador.MediadorDoAdministrador(self.colecao,self.b,self.c)
        self.a.cadastrarCafeicultor(m)
        #Excluir cafeicultor:
        m2 = mediador.MediadorDoAdministrador(self.colecao,self.b,self.c,indice=0)
        self.a.excluirCafeicultor(m2)
        #Obter cafeicultor:
        m3 = mediador.MediadorDoAdministrador(self.colecao,self.b,indice=0) 
        with self.assertRaises(IndexError):
            self.a.getCafeicultor(m3)
    
    
if __name__ == "__main__":
    unittest.main()







