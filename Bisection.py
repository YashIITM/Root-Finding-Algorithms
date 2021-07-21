import numpy as np
import matplotlib.pyplot as plt
from tictoc import *
from plot import plot
#from RFA import bisection

def bisection(f,a,b,TOL,NMAX):
    # THIS FUNCTION PRINTS THE a,b,c VALUES FOR EACH ITERATION:
    
    #Approximates root using Bisection Method
    #In an interval[a,b] with a tolerance TOL
    #|f(c)| < TOL, where m is the midpoint
    

    #INPUT : f , a , b , TOL , NMAX
    # f : function / polynomial
    # a : interval start
    # b : interval end
    # TOL : tolerance value
    # NMAX : maximum number of iterations


    #Print Table Header:
    print('--------------------------------------------------------------------------')
    print('iter \t\t a \t\t b \t\t c \t\t f(c)        ')
    print('--------------------------------------------------------------------------')
    #satisfy the conditions needed to apply the Bisection Method:
    if np.sign(f(a)) == np.sign(f(b)):
        print("No root found in the given interval!")
        exit()
        
    for i in range(NMAX):
        #Compute Midpoint
        c = (a+b)/2
        #print line for the table:
        N.append(1+i)
        f_x.append(f(c))
        print(str(1+i)+'\t% 15.12f\t% 15.12f\t% 15.12f\t% 15.12f\t' %(a, b, c, f(c)))
        #Check stopping condition:
        if np.abs(f(c)) < TOL:
            print('------------------------------------------------------------------------')
            print('Root Found: '+str(c))
            break
        #Implement Recursion:
        elif np.sign(f(a)) == np.sign(f(c)):
            #Improvement on a
            a = c
        elif np.sign(f(b)) == np.sign(f(c)):
            #Improvement on b
            b = c
        
    if i == NMAX -1:
        print("MAX NUMBER OF ITERATIONS REACHED!")
        print('Approximaiton to the Root after max iterations is : '+str(c))        
        exit()
f1 = lambda x: x**3 - 3*(x**2) - x + 9
f2 = lambda x: np.exp(x)*(x**3 - 3*(x**2) - x + 9)
a1 = -5
b1 = 0
a2 = -2.5
b2 = 1


N=[]
f_x=[]
tic()
bisection(f1,a1,b1,1.e-10,1000)
toc()
plot(N,f_x,'b',1)
    
N=[]
f_x=[]
tic()
bisection(f1,a2,b2,1.e-10,1000)
toc()
plot(N,f_x,'r',1)
plt.legend(['(a1,b1)=(-5,0)','(a2,b2)=(-2.5,1)'])
plt.show()

N=[]
f_x=[]
tic()
bisection(f2,a1,b1,1.e-10,1000)
toc()
plot(N,f_x,'b',2)
    
N=[]
f_x=[]
tic()
bisection(f2,a2,b2,1.e-10,1000)
toc()
plot(N,f_x,'r',2)
plt.legend(['(a1,b1)=(-5,0)','(a2,b2)=(-2.5,1)'])
plt.show()
