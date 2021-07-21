import numpy as np

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
    
def newton(f,fp,x0,TOL,NMAX):
    #INPUT : f , fp , x0 , TOL , NMAX
    # f : function / polynomial
    # fp : derivative of f
    # x0 : initial guess
    # TOL : tolerance value
    # NMAX : maximum number of iterations

    #Approximates root using Newton's Method
    #Recursive Program

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

