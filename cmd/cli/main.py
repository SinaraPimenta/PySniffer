import json
import os
import sys
sys.path.append('.')
import app.get_all_paths as paths
import app.list_libs as list
import app.plot_top10 as plot
import click


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
def download_git_repos():
    """Run tool in all projects"""
    print("aqui")
    download = "sh download_repos.sh"
    os.system(download)
    #run_tool = "python cmd/cli/main.py analyzing_repos"
    #os.system(run_tool)


@pysniffer.command("analyzing_repos")
def analyzing_git_repos():
    """Generate projects statistics"""
    dir = './downloaded_repos'

    print("##################################################################")
    print("              PySniffer - Generate Projects Statistics            ")
    print("##################################################################")

    #Counting files and getting projects list
    projects_dict,total = paths.get_projects(dir)
    projects = projects_dict.keys()
    projectsReturn = []
    for p in projects:
        projectsReturn.append({"project_name":f"{p}","amount_of_pyfiles":f"{projects_dict[p]}"})
    with open('./returns/files.json', 'w', encoding='utf-8') as f:
        json.dump(projectsReturn, f, ensure_ascii=False, indent=4)

    #Using pipreqs
    for p in projects:
        path = dir + '/' + p
        os.system(f'python pipreqs/pipreqs.py {path} --force')

    #Reading requirements file and generating list
    ext_libs,std_libs = list.list_projects_libs(dir, projects)

    #Creating json file
    with open('./returns/libs.json', 'w', encoding='utf-8') as f:
       json.dump(ext_libs, f, ensure_ascii=False, indent=4)

    with open('./returns/libs_Py.json', 'w', encoding='utf-8') as f:
       json.dump(std_libs, f, ensure_ascii=False, indent=4)

    #Plotting top 10
    plot.plotTop10(ext_libs,'Top 10 Libs Ext','Ext')
    plot.plotTop10(std_libs,'Top 10 Libs Std','Std')

@pysniffer.command("analyzing_my_project")
@click.option('--dir',
              type=click.STRING,
              help='What is the directory of your project?')
def analyzing_my_project(dir:str):
    """Generate statistics for my project"""

    print("##################################################################")
    print("              PySniffer - Generate My Project Statistics          ")
    print("##################################################################")

    #Counting files and getting projects list
    projects_dict,total = paths.get_projects(dir)
    projects = projects_dict.keys()
    projectsReturn = []
    for p in projects:
        projectsReturn.append({"project_name":f"{p}","amount_of_pyfiles":f"{projects_dict[p]}"})
    with open('./returns/files.json', 'w', encoding='utf-8') as f:
        json.dump(projectsReturn, f, ensure_ascii=False, indent=4)        

    #Using pipreqs
    for p in projects:
        path = dir + '/' + p
        os.system(f'python pipreqs/pipreqs.py {path} --force')

    #Reading requirements file and generating list
    ext_libs,std_libs = list.list_projects_libs(dir, projects)

    #Creating json file
    with open('./returns_my_project/libs.json', 'w', encoding='utf-8') as f:
       json.dump(ext_libs, f, ensure_ascii=False, indent=4)

    with open('./returns_my_project/libs_Py.json', 'w', encoding='utf-8') as f:
       json.dump(std_libs, f, ensure_ascii=False, indent=4)


    #ANALIZAR SE AS BIBLIOTECAS DO PROJETO SE ENCONTRAM ENTRE AS MAIS USADAS
    #OFERECER RETORNO AO USUARIO DAS LIBS QUE APERECE E AS QUE NAO APARECEM ENTRE AS MAIS UTILIZADAS (DATAFRAME)

    #


if __name__ == "__main__":
    pysniffer()
