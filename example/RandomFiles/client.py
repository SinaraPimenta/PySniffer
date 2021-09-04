# -*- coding: utf-8 -*-
"""
@author: Mari e Sinara
"""

import socket
#AF_INET: IPV4
#SOCK_DGRAM: socket UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
udp_host = socket.gethostname() #retorna o nome do host local
udp_port = 3000 #define a porta

msg = 'ola'
sock.sendto(bytes(msg,'utf -8'),(udp_host,udp_port)) #envio de mensagem automática para conectar com o server

#Client recebe as informções
#OBS: Para cada sock.sendto de um lado(server ou client) deve-se ter um sock.recv do outro(client ou server)
info = sock.recv(1024).decode() #sock.recvfrom = recebimento de mensagens e em seguida decodificação para logo após serem impressas
print(info)
info1= sock.recv(1024).decode()
print(info1)
info2= sock.recv(1024).decode()
print(info2)
info3= sock.recv(1024).decode()
print(info3)
encerrar= sock.recv(1024).decode()
print(encerrar)
opcao1 = input('Digite a opção desejada: ')
sock.sendto(opcao1.encode(),(udp_host,udp_port)) # sock.sendto = envio de mensagem para o server
print('\n')
#Client opta por inserir crédito

if opcao1 == '1':
    recarga = sock.recv(1024).decode()
    print(recarga)
    valor_desejado = input('')
    sock.sendto(bytes(valor_desejado,'utf-8'),(udp_host,udp_port))
    valor_adicionado= sock.recv(1024).decode()
    print(valor_adicionado)

#Client opta por conhecer planos
elif opcao1 == '2':
    info4 = sock.recv(1024).decode()
    print(info4)
    info5= sock.recv(1024).decode()
    print(info5)
    info6= sock.recv(1024).decode()
    print(info6)
    info7= sock.recv(1024).decode()
    print(info7)
    info8= sock.recv(1024).decode()
    print(info8)
    opcao2= input('Digite a opção desejada: ')
    sock.sendto(opcao2.encode(),(udp_host,udp_port))
    if opcao2 == '1':
        info8= sock.recv(1024).decode()
        print(info8)
    elif opcao2 == '2':
        info9= sock.recv(1024).decode()
        print(info9)
    elif opcao2 == '3':
        info10= sock.recv(1024).decode()
        print(info10)
    else:
        info11= sock.recv(1024).decode()
        print(info11)

#Client opta por falar com um atendente
elif opcao1 == '3':
    info12= sock.recv(1024).decode()
    print(info12)

#Client opta por finalizar o atendimento
elif opcao1 == '0':
    info13= sock.recv(1024).decode()
    print(info13)
    

#Client inseriu valor inválido
else:
    info14= sock.recv(1024).decode()
    print(info14)

sock.close()