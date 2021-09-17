def f(s):
    print('valor:',s)
    return s

def ff(s):
    if s%2==0:
        print('valor:',s)
        return s

vet=list(map(f,range(6)))
print(vet)
print('\n')
vet=list(filter(ff,range(6)))
print(vet)

funcao_geradora=(x for x in range(10) if x % 2==0)
print(list(funcao_geradora))

class itador(object):
    def __int__(self,com,fim):
        self.com=com
        self.fim=fim
    def __iter__(self):
        return self
    def __next__(self):
        if self.com < self.fim:
            self.com+=1
            return self.com**2
        else:
            raise StopIteration

class Quadrados3(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim
    def __iter__(self):
        return Quadrados_Iter(self, self.com, self.fim)

###########################################################

# 3 - Classe iteradora != iteravel
class Quadrados_Iter(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __next__(self):
        if self.com < self.fim:
            self.com += 1
            return self.com ** 2
        else:
            raise StopIteration

class Quadrados3(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim
    def __iter__(self):
        return Quadrados_Iter(self, self.com, self.fim)


#4 - Geradores
class Quadrados2(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim
    def __iter__(self):
        for i in range(self.com + 1, self.fim + 1):
            yield i**2

o=Quadrados3(0,7)
#print(list(o))
print(o)
#########################################################################

