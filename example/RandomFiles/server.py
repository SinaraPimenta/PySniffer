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
sock.bind((udp_host,udp_port)) #para estabelecer a conexão 
print('Servidor pronto.')
while True:
    #Conectando com o client e enviando as mensagens
    inicio, endereco = sock.recvfrom(1024)
    print('Conectando com o cliente e enviando mensagens.....')
    msg = 'Olá! Bem vindo ao atendimento online da MS Soluções Tecnológicas'
    sock.sendto(bytes(msg,'utf -8'),endereco) # sock.sendto = envio de mensagens
    msg1 = 'Clique 1 para recarga'
    sock.sendto(bytes(msg1,'utf -8'),endereco)
    msg2 = 'Clique 2 para consultar planos'
    sock.sendto(bytes(msg2,'utf -8'),endereco)
    msg3 = 'Clique 3 para falar com o atendente'
    sock.sendto(bytes(msg3,'utf -8'),endereco)
    encerrar = 'Clique 0 para encerrar o atendimento'
    sock.sendto(bytes(encerrar,'utf -8'),endereco)
    #Recebimento da opção escolhida
    data,adress = sock.recvfrom(1024) # sock.recvfrom = recebimento de mensagens 
    data = data.decode('utf -8') # decodificação da informação recebida, para ser analisada

    #Client opta por colocar crédito
    if data == '1':
        print('Opção de recarga selecionada.')
        msg4 = ('Digite o valor de recarga')
        sock.sendto(bytes(msg4,'utf -8'),endereco)
        valor,adress = sock.recvfrom(1024)
        valor = valor.decode('utf -8')
        print('O crédito foi adicionado com sucesso.')
        msg5 = f'Crédito de {valor} reais adicionado!'
        sock.sendto(bytes(msg5,'utf -8'),endereco)

    #Client opta por conhecer os planos
    elif data == '2':
        print('Opção de plano selecionada.')
        msg6 = 'Escolha qual plano deseja conhecer'
        sock.sendto(bytes(msg6,'utf -8'),endereco)
        msg7 = '1 - Plano Redes Sociais'
        sock.sendto(bytes(msg7,'utf -8'),endereco)
        msg8 = '2 - Plano Ligações Ilimitadas'
        sock.sendto(bytes(msg8,'utf -8'),endereco)
        msg9 = '3 - Plano Home Office'
        sock.sendto(bytes(msg9,'utf -8'),endereco)
        msg10 = '4 - Plano Universitário'
        sock.sendto(bytes(msg10,'utf -8'),endereco)
        #Recebimento da opção escolhida
        valor,adress = sock.recvfrom(1024)
        valor = valor.decode('utf -8')
        #Análise da opção escolhida pelo client
        if valor == '1':
            print('Plano 1 selecionado.')
            msg11 = 'Uso do Whatsapp, Facebook e Instagram sem descontar do seu pacote de dados'
            sock.sendto(bytes(msg11,'utf -8'),endereco)
        elif valor == '2':
            print('Plano 2 selecionado.')
            msg12 = 'Ligações ilimitadas para qualquer operadora do mesmo estado.'
            sock.sendto(bytes(msg12,'utf -8'),endereco)
        elif valor == '3':
            print('Plano 3 selecionado.')
            msg13 = 'Principais plataformas de videochamada sem descontar do seu pacote de dados'
            sock.sendto(bytes(msg13,'utf -8'),endereco)
        elif '4':
            print('Plano 4 selecionado.')
            msg14 = '20 por cento de desconto para universidades associadas'
            sock.sendto(bytes(msg14,'utf -8'),endereco)
        else:
            print('Cliente inseriu valor inválido.')
            msg15 = 'Valor inválido.'
            sock.sendto(bytes(msg15,'utf -8'),endereco)

    #Client opta por falar com um atendente
    elif data == '3':
        print('Opção para falar com atendente selecionada.')
        msg16 = 'Transferindo para o atendente......'
        sock.sendto(bytes(msg16,'utf -8'),endereco)
    
    #Client opta por encerrar o atendimento
    elif data == '0':
        print('Encerramento do atendimento.....')
        msg17 = 'Atendimento sendo encerrado, agradecemos o contato......'
        sock.sendto(bytes(msg17,'utf -8'),endereco)
        break      
    
    #Client inseriu valor errado
    else:
        print('Cliente inseriu valor inválido.')
        msg18 = 'Valor inválido.'
        sock.sendto(bytes(msg18,'utf -8'),endereco)
        print('Atendimento encerrado.')
    
        
        
        