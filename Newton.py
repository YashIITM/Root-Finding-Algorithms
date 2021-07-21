import numpy as np
import matplotlib.pyplot as plt
from tictoc import *
from plot import plot
#from RFA import newton
def newton(f,fp,x0,TOL,NMAX):
    #INPUT : f , fp , x0 , TOL , NMAX
    # f : function / polynomial
    # fp : derivative of f
    # x0 : initial guess
    # TOL : tolerance value
    # NMAX : maximum number of iterations

    #Approximates root using Newton's Method
    #Recursive Program

    #Print Header
    print('--------------------------------------------------------------------------')
    print('iter \t\t xi \t\t   correction \t\t   rdiff        ')
    print('--------------------------------------------------------------------------')
    # initiate values for  iteration loop:
    rdiff = 1
    xi = x0
    counter = 0
    while rdiff > TOL and counter < NMAX:
        # get the number of necessary iterations at that particular x0
        # compute relative difference
        rdiff = np.abs(f(xi)/fp(xi)/xi)
        # next xi:
        x1 = xi - f(xi)/fp(xi)
        N.append(counter+1)
        f_x.append(f(x1))
        # print iteration data:
        print('%i \t %15.12f \t %15.12f \t %15.12f' % (counter+1, x1, np.abs(f(xi)/fp(xi)),  rdiff))
        # prepare for the next iteration:
        xi = x1
        counter += 1
        if counter == NMAX:
            print("MAX NUMBER OF ITERATIONS REACHED!")
            print('Approximaiton to the Root after max iterations is : ' , x1)        
            exit()
    
    print('------------------------------------------------------------------------')
    print('Root Found: ', x1)

f1 = lambda x: x**3 - 3*(x**2) - x + 9
f1p = lambda x: 3*(x**2) - 6*x -1
f2 = lambda x: np.exp(x)*(x**3 - 3*(x**2) - x + 9)
f2p = lambda x:  np.exp(x)*((x**3 - 3*(x**2) - x + 9)+(3*(x**2) - 6*x -1))
f3 = lambda x: x**3 - 2*x + 2
f3p = lambda x: 3*(x**2) - 2
x01 = -2
x02 = 5


N = []
f_x = []
tic()
newton(f3,f3p,0,1.e-10,1000)
toc()
plot(N,f_x,'b',3)
plt.show()

N = []
f_x = []
tic()
newton(f1,f1p,x01,1.e-10,1000)
toc()
plot(N,f_x,'b',1)

N = []
f_x = []
tic()
newton(f1,f1p,x02,1.e-10,1000)
toc()
plot(N,f_x,'r',1)
plt.legend(['x01 = -2','x02 = +5'])
plt.show()

N = []
f_x = []
tic()
newton(f2,f2p,x01,1.e-10,1000)
toc()
plot(N,f_x,'b',2)

N = []
f_x = []
tic()
newton(f2,f2p,x02,1.e-10,1000)
toc()
plot(N,f_x,'r',2)
plt.legend(['x01 = -2','x02 = +5'])
plt.show()    














