import os

#   CONCATENANDO REQUIREMENTS E GERANDO LISTA

fileList = []
with open('rawList.txt', 'w') as outfile:
    for filename in os.listdir("files"):           
        if filename.startswith("requirements"):     
            with open("files/"+str(filename)) as infile:
                for line in infile:
                    outfile.write(line + "\n")      


#   ARRUMANDO A LISTA DE LIBS

with open('rawList.txt') as infile, open('lista.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue               
        outfile.write(line)                         
os.remove('rawList.txt')


with open('lista.txt') as l:
    libList = l.readlines()

libList = [x.strip() for x in libList] 



#   CRIANDO DICIONARIO

myDict = {}
for lib in libList:
    if not lib:                     
        continue
    elif lib not in myDict.keys():  
        myDict[lib] = 1
    else:                           
        myDict[lib] += 1


print(f'{"Lib":<34}' + "  Count")
for k, v in myDict.items():
    print(f'{k:<34}' + "  " + str(v))
print("Número de libs = " + str(len(myDict)))