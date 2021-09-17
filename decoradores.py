"""
def decorador(func):
    def modificador():
        print("andregoro")
    return modificador

def decorador2(func):
    def modificador2():
        print("andregoro")
    return modificador2

@decorador2
@decorador
def a():
    print("original")

#a()

def tags(tags):
    def decorador(func):
        def modificador():
             print("tags "+tags)
        return modificador
    return decorador

@tags('TEST')
def a():
    print("original")

#a()
def fabrica(tags):
    if tags == "n":
        def numero(func):
            def mostra():
                print(123456)
            return mostra
        return numero
    else:
        def string(func):
            def mostra():
                print("nome")
            return mostra
        return string

@fabrica('s')
def sand():
    print("s")

sand()
"""
"""

class tracer:
    def __init__(self, func):
        self.cont = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.cont += 1
        print('Chamade de número %s a %s' % (self.cont, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


spam(1,2,3)

print("Vamos estudar agora decoradores de métodos")
print("e decoradores de classes.")

input()

print("Decoradores de métodos funcionam assim como")
print("decoradores de classe, dessa forma basta criar")
print("uma função decoradora e aplica-la a um método")
print("usando a sintaxe do @")

input()

print("Alguns decoradores de método populares apresentaremos")
print("agora. São eles @staticmethod, @classmethod, @override e @property")

input()

print("@staticmethod indica que o dado método é estatico")
print("logo deverá ser chamado usando a classe e não uma")
print("instância da classe, assim a instância não")
print("deve ser passada como argumento. Por exemplo: ")


class A(object):
    @staticmethod
    def method(*argv):
        return argv


a = A()

print("a.method([1,2,3,4]) = ", a.method([1, 2, 3, 4]))
print("Sem o @staticmethod")


class A(object):
    def method(*argv):
        return argv


a = A()
print("a.method([1,2,3,4]) = ", a.method([1, 2, 3, 4]))

input()

print("@classmethod, ao inves da instância ser passada")
print("como argumento para o método, a classe será passada")


class A(object):
    @classmethod
    def method(*argv):
        return argv


a = A()

print("a.method([1,2,3,4]) =", a.method([1, 2, 3, 4]))

input()

print("@override não é um decorador pré construido em python")
print("entretanto é um 'decorador' bastante popular em outras")
print("em outras linguagens, especialmente Java. Podemos escrever")
print("uma receita de bolo simples para esse decorador como sendo:")

input()


def overrides(interface_class):
    def overrider(method):
        assert (method.__name__ in dir(interface_class))
        return method

    return overrider


input()

print("A única coisa que o @override faz é previnir")
print("erros de digitação ao criar um método de uma classe")
print("filha que irá sobrepor o método da classe pai.")

input()


class Pai(object):
    def meu_metodo(self):
        print('Ola Mundo!')


class Filha(Pai):
    @overrides(Pai)
    def meu_metodo(self):
        print('Ola Marte!')


try:
    class Erro(Pai):
        @overrides(Pai)
        def mei_metodo(self):
            print('ops!')
except AssertionError:
    print("Pegamos erro")

input()

print("Um decorador importante refere-se as propriedades")
print("Veja no exemplo que por meio dos decoradores substituimos")
print("A linha de criação da propriedade e ainda todos os métodos")
print("possuem os mesmos nomes")


class Pessoa:
    def __init__(self, prim_nome, ult_nome):
        self.prim_nome = prim_nome
        self.ult_nome = ult_nome

    @property
    def nome(self):
        return '%s, %s' % (self.ult_nome, self.prim_nome)

    @nome.setter
    def nome(self, valor):
        self.prim_nome = valor

    @nome.deleter
    def nome(self):
        del self.prim_nome
        del self.ult_nome


p = Pessoa('Luis', 'Rodrigo')
print(p.nome)
p.nome = 'Alchin, Martin'
print(p.nome)
del p.nome

input()

print("Podemos criar decoradores de classes, isto é")
print("decoradores que irão mudar todo o funcionamento")
print("de uma dada classe")

input()

print("No exemplo abaixo vemos o decorador 'singleton' que")
print("faz com que apenas uma instância de classe possa ser")
print("criada")

instancias = {}


def singleton(umaClasse):
    def onCall(*args, **kwargs):
        print("onCall foi chamado agora!!")
        if umaClasse not in instancias:
            instancias[umaClasse] = umaClasse(*args, **kwargs)
        return instancias[umaClasse]

    return onCall


@singleton
class Pessoa:
    def __init__(self, nome, horas, ganho):
        self.nome = nome
        self.horas = horas
        self.ganho = ganho

    def paga(self):
        return self.horas * self.ganho


bob = Pessoa('Bob', 40, 10)
print(bob.nome, bob.paga())
sue = Pessoa('Sue', 50, 20)
print(sue.nome, sue.paga())

input()

print("Uma classe decoradora por outro lado")
print("consiste numa classe que irá decorar a outra")
print("logo a classe decoradora deverá receber uma")
print("classe como argumento")

input()

print("Por exemplo, suponhamos que se queira acompanhar os métodos")
print("usados por uma determinada classe. Iremos criar uma classe")
print("decoradora Trace que permitira acompanhar a execução de")
print("uma classe decorada por ela")

input()


class Tracer:
    def __init__(self, umaClasse):
        print("Construtor foi chamado!!")
        self.umaClasse = umaClasse

    def __call__(self, *args):
        print("Chamamos o método __call__")
        self.wrapped = self.umaClasse(*args)
        return self

    def __getattr__(self, atrnome):
        print('Trace: ' + atrnome)
        return getattr(self.wrapped, atrnome)


@Tracer  # Chama o construtor de Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)


print("Vamos começar o teste...")
s = Spam()  # Chama o Call de Tracer
s.display()

input()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""

"""
import sys
p={'numer':'numero','string':'string'}
print("%(numer)s e %(string)s "%p)

templete='{0} {1} {2}'
print(templete.format('andre',"joao",'jose'))
template = '{numero}, {porco} e {comida}'

template.format(numero=1, porco='presunto', comida='ovos')
print(templete)

print('{0:10} = {1:10}'.format('spam', 123.4567), '{0:>10} = {1:<10}'.format('spam', 123.4567),
      '{0.platform:>10} = {1[tipo]:<10}'.format(sys, dict(tipo='laptop')), sep = "\n")
"""
import csv
"""
file=open('test.csv','w')
escrita=csv.writer(file)
escrita.writerow(('Nome','Idade','Sexo'))
escrita.writerow(('Andre',17,'M'))
escrita.writerow(('Andrei',14,'M'))
escrita.writerow(('Andreia',19,'F'))
file.close()
"""
# file=open('test.csv','r')
# reade=csv.reader(file)
# #print(open('test.csv','r').read())
# for d in reade:
# #    print(d)
# file.close()

class Quadrados(object):
    def __init__(self, coms, fims):
        self.coms = coms
        self.fims = fims

    def __iter__(self):
        return self

    def __next__(self):
        if self.coms < self.fims:
            self.coms +=1
            return self.coms ** 2
        else:
            raise StopIteration

class Quadrados2(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim
    def __iter__(self):
        for i in range(self.com+1,self.fim+1):
            yield i ** 2

    # def __next__(self):
    #     if self.com < self.fim:
    #         self.com += 1
    #         return self.com ** 2
    #     else:
    #         raise StopIteration

# dd=Quadrados(0, 5)
# d2=Quadrados2(0,9)
# for d in d2:
#     print(d)
# for d in dd:
#     print(d)

# Echo server program
# import socket
#
# HOST = ''                 # Symbolic name meaning all available interfaces
# PORT = 50007              # Arbitrary non-privileged port
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(1)
# conn, addr = s.accept()
# print('Connected by', addr)
# while 1:
#     data = conn.recv(1024)
#     r=input()
#     if not data: break
#     conn.sendall(data)
# conn.close()


# import json
# nome={'Nome':'andre'}
# datas=json.dumps(nome)
# #print(datas)
# with open('Json.json','wb') as nomes:
#    nomes.write(datas.encode())
#
# with open('Json.json','ab') as nomes:
#     o=json.dumps([1,2,3,4,5])
#     nomes.write(b'\n'+o.encode())
#     o=json.loads(b'{"tel":10193028}'.decode())
#     #nomes.write(o)
#
# with open('Json.json','rb') as nomes:
#     print(nomes.read().decode())

# import pickle
#
# with open('arquivo.pck','wb') as aqv:
#     aqv.write(pickle.dumps("andre".encode()))
# with open('arquivo.pck','rb') as aqv:
#     p=aqv.readline()
#     print(pickle.loads(p))

# import shelve
#
# with shelve.open('shelve.db') as date:
#     date['lista']=[1,3,4]
# with shelve.open('shelve.db',writeback=True) as date:
#     date['lista'].append(5)
#     print(date['lista'])

# #set
# s=set('andrea')
# s.add(2)
# s2=set('andre jo')
# s.update(s2)
# print(s.pop())
# print(s2 & s)
# print(s - s2)
# print(s ^ s2)

# from collections import namedtuple
# nome=namedtuple('Nome','andre jo')
# nome.andre='manerao'
# print(nome.andre)
# Ponto=namedtuple('Point',['x','y'])
# ponto=Ponto(10,19)
# print(ponto.x)
#
# from collections import OrderedDict
# d=OrderedDict([(6,'6'),(7,'7'),(8,'8')])
# print(d[6])
# letra=OrderedDict.fromkeys('abcdef')
# for i,k in enumerate(letra.keys(),1):
#         letra[k]=str(i)
# print(letra)
# letra.move_to_end('a')
# print(letra)
#
# from heapq import *
# pilha=[]
# heappush(pilha,10)
# print(pilha)
# heappop(pilha)
#
# pilha=[5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
# print(pilha)
# heapify(pilha)
# print(pilha)
# heapreplace(pilha,0)
# print(pilha)
#
# from collections import defaultdict
# cont=defaultdict(int)
# cont['andre']=10
# print(cont)
# print(cont.get('andre'))
#
# from collections import deque
# dique=deque('abcdefg')
# print(dique)
# dique.append('aa')
# print(dique)
# dique.appendleft('ZZ')
# print(dique)
# print(dique.pop())
# dique.extend('123456')
# print(dique)
# dique.rotate(-1)
# print(dique)


# #############
# def func(fun):
#     def fun():
#         print('adus')
#     return fun
#
# @func
# def funcao():
#     print('ola')
#
# funcao()
#
# def tags(tag):
#     def fun(fun):
#         def ret():
#             print('tiririca '+tag)
#         return ret
#     return fun
#
# @tags('jood')
# def funcao2():
#     print('andre')
# funcao2()


# class A(object):
#     @staticmethod
#     def method(*args):
#         return args
#
# a=A()
# print(a.method([1,2,3,4,5]))
#
# def overrides(interface_class):
#     def overrider(method):
#         assert(method.__name__ in dir(interface_class))
#         return method
#     return overrider
#
# class Pai(object):
#     def meu_metodo(self):
#         print('Ola Mundo!')
#
# class Filha(Pai):
#     @overrides(Pai)
#     def meu_metodo(self):
#         print('Ola Marte!')
#
# class Pessoa:
#     def __init__(self, prim_nome, ult_nome):
#         self.prim_nome = prim_nome
#         self.ult_nome = ult_nome
#
#     @property
#     def nome(self):
#         return '%s, %s' % (self.ult_nome, self.prim_nome)
#
#     @nome.setter
#     def nome(self, valor):
#         self.prim_nome = valor
#
#     @nome.deleter
#     def nome(self):
#         del self.prim_nome
#         del self.ult_nome
#
#
# p = Pessoa('Luis', 'Rodrigo')
# print(p.nome)
# p.nome = 'Alchin, Martin'
# print(p.nome)
# del p.nome
# print(""""33333333333333333333333333333333""")
#
# class Tracer:
#     def __init__(self, umaClasse):
#         print("Construtor foi chamado!!")
#         self.umaClasse = umaClasse
#
#     def __call__(self, *args):
#         print("Chamamos o método __call__")
#         self.wrapped = self.umaClasse(*args)
#         return self
#
#     def __getattr__(self, atrnome):
#         print('Trace: ' + atrnome)
#         return getattr(self.wrapped, atrnome)
#
#
# @Tracer  # Chama o construtor de Tracer
# class Spam:
#     def display(self):
#         print('Spam!' * 8)
#
#
# print("Vamos começar o teste...")
# s = Spam()  # Chama o Call de Tracer
# s.display()

#parte IX
# import os
# print(os.getcwd())
# print(os.chdir('..'))
# print(os.getcwd())
# print(os.system('cd C:\\Users\\andregoro\\PycharmProjects\\untitled'))
# print(os.getcwd())
# if __name__ == "__main__":
#     for (root,dirs,files) in os.walk('untitled'):
#         print('Caminho--> '+str(root))
#         print('Diretorios--> '+str(dirs))
#         print('Arquivos--> '+str(files))
#         print('--------------------------------')
#parte X
# import sys,subprocess
# subprocess.call(['dir'],shell=True)
# #subprocess.call(['FOR /L %G IN (1,1,4) DO echo %G'],shell=True)
# subprocess.call(['cd'],shell=True)
# subprocess.check_call(['cd..|cd'],shell=True)
#
# p=subprocess.Popen('python escreve.py',stdout=subprocess.PIPE,shell=True)
# print(p.communicate())
# print("///////////////////////////////////////////////")
# pp=subprocess.Popen('python ler.py', stdin=subprocess.PIPE,shell=True)
# print(pp.communicate(b'40'))

#parte XI
import subprocess
p=subprocess.Popen('python parteXI.py 2',stdout=subprocess.PIPE,shell=True)
print(p.communicate())



