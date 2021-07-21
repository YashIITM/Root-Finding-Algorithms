import matplotlib.pyplot as plt
def plot(N,f_x,color,number):
    plt.plot(N,f_x,color=color)
    plt.title(f"Plot for function %d" %number)
    plt.xlabel('Number of Iterations')
    plt.ylabel('f(x)')
    #plt.show()
