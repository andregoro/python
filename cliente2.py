# from socket import *
# host,port='localhost',5000
#
# sock=socket(AF_INET,SOCK_STREAM)
#
# sock.connect((host,port))
#
# #conexao=sock.accept()
# #print(endereço)
# while True:
#     o=input()
#     sock.send(b'123456789')#envio
#     data=sock.recv(1024)#recebimento
#     print(data)
# sock.close()


# from socket import *
#
# host,port='localhost',50000
#
# sock=socket(AF_INET,SOCK_STREAM)
#
# sock.connect((host,port))
#
# #conexao=sock.accept()
# o=str(input())
# sock.send(o.encode())
# data=sock.recv(1024)
# data=data.decode()
#
# print(data)
# sock.close()
######################################
# from socket import *
#
# host,port='localhost',50050
#
# sock=socket(AF_INET,SOCK_STREAM)
#
# sock.connect((host,port))
# conexao=sock
# while True:
#     envia=input(str("Digite a informaçao:"))
#     conexao.send(envia.encode())
#     receber=conexao.recv(1024)
#     print('Eco=>'+receber.decode())

# from socket import *
# host,port='localhost',50050
#
# sock=socket(AF_INET,SOCK_STREAM)
#
# sock.connect_ex((host,port))
#
# #print("servidor "+sock)
# while True:
#     enviar=str(input("enviar:")).encode()
#
#     if not enviar: break
#
#     sock.send(enviar)
#     receber=sock.recv(1024)
#     print('Mensagem '+receber.decode())

#               udp
# from socket import *
#
#
# def main():
#     # Cria host e port number
#     host = "localhost"
#     port = 5000
#
#     # O servidor será um par endereço e port
#     server = (host, port)
#
#     # Criamos o socket
#     conexão = socket(AF_INET, SOCK_DGRAM)
#     conexão.bind((host, port))
#
#     # Vamos mandar menssagem enquanto a menssagem for diferente de sair (s)
#     msg = input("-> ")
#     while msg != 's':
#         # Mandamos a menssagem através da conexão
#         conexão.sendto(msg.encode(), server)
#
#         # Recebemos uma respota do servidor
#         data = conexão.recvfrom(1024)
#
#         # Imprimimos a menssagem recebida
#         print("Recebida ->", str(data))
#
#         # Podemos mandar mais menssagens
#         msg = input("-> ")
#
#     # Fechamos a conexão
#     conexão.close()
#
#
# if __name__ == '__main__':
#     main()
from socket import*

host,port='localhost',5020
server=((host,port))

sockudp=socket(AF_INET,SOCK_DGRAM)

while True:
