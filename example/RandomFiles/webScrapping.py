from bs4 import BeautifulSoup
import sys
sys.path.append('src/main/controller/exception')
import exception
import requests

def cotacaoCafe(self,tipo,classificacao_bebida):
    try:
        html = requests.get("http://cccmg.com.br/cotacao-do-cafe/").content
        soup = BeautifulSoup(html, 'html.parser')
        tabela = soup.find('table', attrs={'class':'tabela-resultados'})
        linhas = tabela.find_all('td')
        achou = False
        preco = 0
        for i in linhas:
            if achou==True:
                preco=i.text
                preco=preco.replace(',','.')
                preco=float(preco.replace('R$ ',''))
                break
            if classificacao_bebida in i.text and tipo in i.text:
                achou = True
        return preco
    except:
        raise exception.RequestException




    