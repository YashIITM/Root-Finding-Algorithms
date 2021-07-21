import numpy as np
import matplotlib.pyplot as plt
from tictoc import *
from plot import plot
#from RFA import secant

def secant(f,x0,x1,TOL,NMAX):
    #INPUT : f , x0 , x1 , TOL , NMAX
    # f : function / polynomial
    # x0 : first initial point/guess
    # x1 : second initial point/guess
    # TOL : tolerance value
    # NMAX : maximum number of iterations

    #Approximates root using Secant Method

    #Print Header
    print('--------------------------------------------------------------------------')
    print("iter \t\t\t x2 \t\t\t\t f(x2)")
    print('--------------------------------------------------------------------------')
    
    for i in range(NMAX):
        if f(x0) == f(x1):
            print('DIVIDE BY ZERO ENCOUNTERED!')
            exit()
        #improved guess
        x2 = x0 - (x1-x0)*f(x0)/(f(x1)-f(x0))
        N.append(1+i)
        f_x.append(f(x2))
        #print values after each iteration step
        print("%d \t\t %15.12f \t\t %15.12f" %(1+i,x2,f(x2)))
        x0 = x1
        x1 = x2

        #executing the required precision
        if abs(f(x2)) < TOL:
            print('--------------------------------------------------------------------------')
            print('Root Found : ',x2)
            break
    #limiting number of iterations
    if i == NMAX -1:
        print("MAX NUMBER OF ITERATIONS REACHED!")
        print('Approximaiton to the Root after max iterations is : '+str(c))        
        exit()






f1 = lambda x: x**3 - 3*(x**2) - x + 9
f2 = lambda x: np.exp(x)*(x**3 - 3*(x**2) - x + 9)
x0 = -2
x1 = 5




N=[]
f_x=[]
tic()
secant(f1,x0,x1,1.e-10,1000)
toc()
plot(N,f_x,'b',1)

N=[]
f_x=[]
tic()
secant(f1,x0-0.5,x1+0.5,1.e-10,1000)
toc()
plot(N,f_x,'r',1)
plt.legend(['(x0,x1)=(-2,2)','(x0,x1)=(-2.5,5.5)'])
plt.show()

N=[]
f_x=[]
tic()
secant(f2,x0,x1,1.e-10,1000)
toc()
plot(N,f_x,'b',2)

N=[]
f_x=[]
tic()
secant(f2,x0-0.5,x1+0.5,1.e-10,1000)
toc()
plot(N,f_x,'r',2)
plt.legend(['(x0,x1)=(-2,2)','(x0,x1)=(-2.5,5.5)'])
plt.show()

