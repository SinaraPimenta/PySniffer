import app.download_repos as repos
import app.get_all_paths as paths
import app.list_libs as list
import app.dict_to_json as jsonFile
import app.plot_top10 as plot
import os

mode = 'SAMPLE'

if mode == 'SAMPLE': #Statistics about projects from github
    dir = 'C:/Users/mariana.helena/Documents/pythonprojects' #alterar para ./downloaded_repos
    #Cloning repos
    #repos.gets_repos()

    #Counting files and getting projects list
    projects_dict,total = paths.get_projects(dir)
    projects = projects_dict.keys()

    #Using pipreqs
    for p in projects:
        path = dir + '/' + p
        os.system(f'pipreqs {path} --force') 

    #Reading requirements file and generating list
    ext_libs = list.list_projects_libs(dir, projects)

    #Creating json file
    jsonFile.module_amount(ext_libs)

    #Plotting top 10
    plot.plotTop10(ext_libs)

elif mode == 'MYPROJECT': #Statistics about my project
    dir = 'C:/Users/mariana.helena/Documents/pythonprojects/Projeto_C214_Armazem_MS-main'

    #Counting files
    total = paths.count_files(dir)

    #Using pipreqs
    os.system(f'pipreqs {dir} --force') 

    #Reading requirements file and generating list
    ext_libs = list.list_libs(dir)
    print(ext_libs)

