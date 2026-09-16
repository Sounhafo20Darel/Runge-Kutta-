from math import *
from numpy import *
import matplotlib.pyplot as plt
print('approximation de la solution d une edo via la methode de runge kutta d ordre 3')
def phi(t,x):
    Q=(-x/(t*log(t)))+1/log(t)
    return Q
def f(t):
    f=t/log(t)
    return f
n=int(input('veuillez entrer le nombre de point à approximer n'))
a=float(input('veullez entrer la borne inferieure de l intervalle DIFFERENT DE 1 a'))
b=float(input('veullez entrer la borne superieure de l intervalle b'))
yo=a/log(a)
T=zeros(n)
h=(b-a)/(n-1)
for i in range(n):
    T[i]=a+i*h

y=zeros(n)
K1=zeros(n)
K2=zeros(n)
K3=zeros(n)
y[0]=yo
K1[0]=phi(T[0],y[0])
K2[0]=phi(T[0]+(7/10)*h,y[0]+(7/10)*h*K1[0])
K3[0]=phi(T[0]+(1/5)*h,y[0]+(-43/35)*h*K1[0]+(7/10)*h*K2[0])
for i in range(n-1):
    y[i+1]=y[i]+h*((1/6)*K1[i]+(2/3)*K2[i]+(1/6)*K3[i])
    K1[i+1]=phi(T[i],y[i])
    K2[i+1]=phi(T[i]+(7/10)*h,y[i]+(7/10)*h*K1[i+1])
    K3[i+1]=phi(T[i]+(1/5)*h,y[i]+(-43/35)*h*K1[i+1]+(7/10)*h*K2[i+1])

w=zeros(n)
for i in range(n):
    w[i]=f(T[i])

plt.figure()
plt.plot(T,y)
plt.plot(T,w)
plt.show()

