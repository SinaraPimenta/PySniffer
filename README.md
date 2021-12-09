#  PySniffer 🕵
<p align="center">
<img src="https://github.com/Mariana-Helena/PySniffer-Web-Application/blob/main/src/assets/img/YellowLogo.png" height="150" width="150" >
</p>

[PySniffer](https://github.com/SinaraPimenta/PySniffer) is a tool to analyze Open-Source Python projects hosted on GitHub, looking for the modules used (from the Standard Library as well as from external libraries), in order to generate statistics about the usage of Python modules. 


The project was made for the Undergraduate Thesis on Computer Engineering of Instituto Nacional de Telecomunicações (INATEL).

 ### 🎯 Application Goal
The goal of the tool is to extract the most used modules in Python projects hosted on GitHub. Afterwards we can compare this empirically obtained list with the information posted on blogs and websites about which Python modules/libraries are the most popular or which are the most used.
In addition, the tool is intended to allow the comparison of any* Python project hosted on GitHub with the collected results.
This comparison is very interesting, once the developer can check and to question if the used packages are the best for a given task.  

*Currently, the tool can only process projects written in Python 3. And these projects cannot contain syntax or indentation errors.
In addition to these criteria, there is a restriction regardingthe search for modules. If the developer uses the module name in some file or folder, the module is disregarded by the [pipreqs](https://github.com/bndr/pipreqs) tool. Because the name of the modules themselves are the names of the .py scripts. 

 ### 📊 Results
<p align="center">
<img src="https://github.com/SinaraPimenta/PySniffer/blob/main/returns/all_projects/Top%2010%20Libs%20Ext.png" height="450"  >
</p>

<p align="center">
<img src="https://github.com/SinaraPimenta/PySniffer/blob/main/returns/all_projects/Top%2010%20Libs%20Std.png" height="450" >
</p>



### 🚀 Starting
 To get a copy of the project in order to run/test it, clone the repository into a folder on your machine:

```
git clone https://github.com/SinaraPimenta/PySniffer.git
```

### 📋 Pre-Requisites
- python3

### 🔧 Installing dependencies

 It is recommended to install the dependencies inside a virtualenv.
 
 ```
virtualenv venv 
``` 
 To install the project dependencies it's necessary, after activate virtualenv, to type the command in terminal:

```
python setup.py develop 
```

### 👩‍💻 Running the project
For project execution, type:

```
python cmd/cli/main.py [OPTIONS] COMMAND [ARGS]
```

### 💻 Functionalities

- download_repos: mode responsible for downloading the [selected repositories](https://github.com/SinaraPimenta/PySniffer/blob/main/download_repos.sh) from GitHub;
```
python cmd/cli/main.py download_repos
```

- analysing_repos: obtains which modules are the most used in the downloaded projects;
```
python cmd/cli/main.py analyzing_repos
```

- analysing_my_project: compares the used modules from a given GitHub repository with the results obtained in the previous mode.
```
python cmd/cli/main.py analyzing_my_project --link https://github.com/{user}/{repository}.git
```


## ✒️ Authors
* **Luana Gribel Ito** - [Luana](https://github.com/luanagribel)
* **Mariana Helena Inês Moreira** - [Mariana](https://github.com/Mariana-Helena)
* **Sarah Brandão** - [Sarah](https://github.com/SarahBrandao)
* **Sinara Pimenta Medeiros** - [Sinara](https://github.com/SinaraPimenta)

## 👨‍🏫 Advisor
* **Phyllipe de Souza Lima Francisco** - [Phyl](https://github.com/phillima)



⌨️ with ❤️ by Luana, Mariana, Sarah e Sinara 😊


