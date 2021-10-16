import json
import os

import app.download_repos as repos
import app.get_all_paths as paths
import app.list_libs as list
import app.plot_top10 as plot


def main():
    mode = 'SAMPLE'

    if mode == 'SAMPLE': #Statistics about projects from github
        dir = './example' #alterar para ./downloaded_repos
        #Cloning repos
        #repos.gets_repos()

        #Counting files and getting projects list
        projects_dict,total = paths.get_projects(dir)
        projects = projects_dict.keys()

        #Creating json file
        with open('./returns/files.json', 'w', encoding='utf-8') as f:
            json.dump(projects_dict, f, ensure_ascii=False, indent=4)

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
        plot.plotTop10(ext_libs,'Top 10 Libs Ext')
        plot.plotTop10(std_libs,'Top 10 Libs Std')

    elif mode == 'MYPROJECT': #Statistics about my project
        dir = 'C:/Users/mariana.helena/Documents/pythonprojects/Projeto_C214_Armazem_MS-main'

        #Counting files
        total = paths.count_files(dir)

        #Using pipreqs
        os.system(f'pipreqs {dir} --force')

        #Reading requirements file and generating list
        ext_libs = list.list_libs(dir)
        print(ext_libs)


if __name__ == "__main__":
    main()