import json
import os
import sys

import click
import scripts.get_all_paths as paths
import scripts.plot_top10 as plot
from logs import log
from scripts import list_libs
from scripts.analyzing_my_repo import analyzing_libraries

sys.path.append('.')


@click.group()
@click.version_option()
def pysniffer():
    """
    ###########      PySniffer      ###########
    """

@pysniffer.command("download_repos")
def download_git_repos():
    """Download GitHub projects"""
    download = "sh download_repos.sh"
    os.system(download)


@pysniffer.command("run_all_tool")
def run_all_tool():
    """Run tool in all projects"""
    download = "sh download_repos.sh"
    os.system(download)
    run_tool = "python cmd/cli/main.py analyzing_repos"
    os.system(run_tool)


@pysniffer.command("analyzing_repos")
def analyzing_git_repos():
    """Generate projects statistics"""
    dir = './downloaded_repos/all_repos'

    print("##################################################################")
    print("              PySniffer - Generate Projects Statistics            ")
    print("##################################################################")

    #Counting files and getting projects list
    projects_dict = paths.get_projects(dir)
    projects = projects_dict.keys()

    #Using pipreqs
    for p in projects:
        path = dir + '/' + p
        os.system(f'python pipreqs/pipreqs.py {path} --force')

    #Reading requirements file, generating list and save in a Json
    list_libs.list_save_projects_libs(dir, projects)

    log('i','Returns were generated in returns/all_projects')


@pysniffer.command("analyzing_my_project")
@click.option('--link',
              type=click.STRING,
              help="What is your project's github link?")
def analyzing_my_project(link:str):
    """Generate statistics for my project"""
    dir = './downloaded_repos/my_repo'
    print("##################################################################")
    print("              PySniffer - Generate My Project Statistics          ")
    print("##################################################################")

    #download repo
    #download = f"git -C {dir} clone {link} "
    #os.system(download)
    #Counting files and getting projects list
    projects_dict = paths.get_projects(dir)
    projects = projects_dict.keys()

    #Using pipreqs
    for p in projects:
        path = dir + '/' + p
        os.system(f'python pipreqs/pipreqs.py {path} --force')

    #Reading requirements file, generating list and save in a Json
    list_libs.list_save_projects_libs(dir, projects)


    #ANALIZAR SE AS BIBLIOTECAS DO PROJETO SE ENCONTRAM ENTRE AS MAIS USADAS
    #OFERECER RETORNO AO USUARIO DAS LIBS QUE APERECE E AS QUE NAO APARECEM ENTRE AS MAIS UTILIZADAS (DATAFRAME)



if __name__ == "__main__":
    #pysniffer()
    analyzing_libraries()
