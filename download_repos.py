from git import Repo
import requests
from bs4 import BeautifulSoup
import os

def download_repos(links:list):
    #Clonando os repos
    for link in links:
        print(link)
        resp = link.get("href")
        dir = (resp.split("/"))[-1]
        path = os.path.join("./downloaded_repos", dir)
        os.mkdir(path)
        Repo.clone_from(f'https://github.com/{resp}', f'./downloaded_repos/{dir}')


def get_links_repos():
    url = "https://github.com/orgs/python/repositories?language=&q=&sort=stargazers&type="

    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    #Pegando os links dos repos
    links = soup.find_all("a",attrs={"itemprop":"name codeRepository"})
    return links


if __name__ == "__main__":
    links = get_links_repos()
    download_repos(os.link)