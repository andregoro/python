# from socket import *
# #import socket
# host=''
# port=5000
#
# sock=socket(AF_INET,SOCK_STREAM)
# sock.bind((host,port))
#
# sock.listen(5)
# conexao,endereço=sock.accept()
# while True:
#    data= conexao.recv(1024)
#
#    if not data:break
#
#    conexao.send(b'Eco=>'+ data)
# conexao.close()

'''
from socket import *

host,port='',50000

sock=socket(AF_INET,SOCK_STREAM)

sock.bind((host,port))


sock.listen(5)

while True:
    conexao, endereço = sock.accept()
    print('Server conectado por', endereço)
    data=conexao.recv(1024)#recebe
    #if not data: break

    conexao.send('respondido'.encode())

#conexao.close()
'''

# from socket import *
#
# host,port='',50050
#
# sock=socket(AF_INET,SOCK_STREAM)
#
# sock.bind((host,port))
#
# sock.listen(5)
#
# conexao,endereco=sock.accept()
#
# print("Servidor iniciado "+str(endereco))
# while True:
#     receber=conexao.recv(1024)
#     print(receber.decode())
#
#     #if not receber: break
#     conexao.send('repondido'.encode())
# from socket import *
#
# host,port='',50050
#
# sock=socket(AF_INET,SOCK_STREAM)
#
# sock.bind((host,port))
#
# sock.listen(5)
#
# conexao,endereço=sock.accept()
# print("servidor ",endereço)
# while True:
#     receber=conexao.recv(1020)
#
#     print(receber.decode())
#
#     envia=conexao.send('rebida'.encode())




#                                upd
# from socket import *
#
# # Cria host e port number
# host = ""
# port = 5000
#
# # Cria socket
# server = socket(AF_INET, SOCK_DGRAM)
#
# server.bind((host,port))
# # Indica que o servidor foi iniciado
# print("Servidor iniciado")
#
# # Bloco infinito do servidor
# while True:
#     # Recebe a data e o endereço da conexão
#     data, endereço = server.recvfrom(1024)
#     # Imprime as informações da conexão
#     print("Menssagem recebida de", str(endereço))
#     print("Recebemos do cliente:", str(data))
#
#     # Vamos mandar de volta a menssagem em eco
#     resposta = "Eco=>" + str(data)
#     server.sendto(data, endereço)
#
# # Fechamos o servidor
# server.close()

