import concurrent.futures
import os

import requests
from bs4 import BeautifulSoup
from git import Repo
from logs import log


def download_repos(link):
    #Clonando os repos
    resp = link.get("href")
    dir = (resp.split("/"))[-1]
    path = os.path.join("./downloaded_repos", dir)
    os.mkdir(path)
    log("i",f"Clonando repositorio {dir}....")
    Repo.clone_from(f'https://github.com/{resp}', f'./downloaded_repos/{dir}')


def gets_repos():
    url = "https://github.com/orgs/python/repositories?language=&q=&sort=stargazers&type="

    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    #Pegando os links dos repos
    links = soup.find_all("a",attrs={"itemprop":"name codeRepository"})
    log("i","Iniciando download dos repositorios ....")
    lts = links[-3:-1]
    for repo in lts:
        download_repos(repo)
    log("i","Download realizado com sucesso!")


if __name__ == "__main__":
    gets_repos()
