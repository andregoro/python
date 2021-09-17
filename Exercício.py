import struct
import os
"""
Crie um programa para o governo, onde é possível armazenar o nome
de uma Pessoa, R.G. e CPF 
dados num formato de bytes
12.345.678-9
123.456.789/10
"""
# arquivo=open("st.dec",'wb')
# for i in range(3):
#     nome = str(input("nome"))
#     tam=len(nome)
#     e=struct.unpack(str(tam)+'s',nome.encode())
#     arquivo.writelines(e)
# arquivo.close()

"""
def som(i):
  return i+i

arquivo=open("st.dec",'rb')

lis=[ x for x in range(5)]
c=list((x for x in range(10) if x%2==0))
print(c)
print(lis)
ma=list(map((lambda x:x**2),range(3)))
fi=list(filter((lambda x:x%3==0),range(10)))
f=[1,2,3,4,5]
soma=sum(f)
print(ma)
print(fi)
print(soma)
"""

"""
def soma(*args):
  z=1
  for i in args:
    yield i+10

for i in soma(1,3,4,5,6,6):
      print(i)
# lista=[i + y for i in range(9) for y in range(8)  if i%2==0 and y%3==0]
# print(lista)
# dd=list((x for x in range(9) if x > 4 and x < 8))
# print(dd)
# print("soma ",sum(lista))
# s=[1,2,3,4,5,6,7]
# ss=list(map(som,s))
# print(ss)
# print("map ",list(map(som,s)))
print("filter ",list(map((lambda x: x),filter(soma,[1,2,3,4,5,6]))))
#os.system("cls")

"""

def func(z,*args):
  z=1
  for i in args:
    yield i+10


for i in func(1,3,4):
    print(i)
#for j in func(1):
#  print(j)