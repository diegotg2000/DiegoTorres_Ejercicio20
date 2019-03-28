import numpy as np

class Complejo:
    def __init__(self,x,y):
        self.real=x
        self.imaginario=y
        self.norma=np.sqrt(x**2+y**2)
    def conjugado(self):
        self.imaginario=-self.imaginario
    def calcula_norma(self):
        return self.norma
    def multiplicar(self, otro):
        a=self.real
        b=self.imaginario
        c=otro.real
        d=otro.imaginario
        return Complejo(a*c-b*d,b*c+a*d)
    def pow(self,n):
        p=self
        for i in range(n-1):
            p=p.multiplicar(self)
        return p
    def imprimir(self):
        x=self.real
        y=self.imaginario
        return(x,y)

    