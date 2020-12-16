#%%
## module bisection
import axes
import numpy as np
import matplotlib.pyplot as plt
from math import isclose,log
from sympy import diff, symbols, lambdify

def bisection(f,a,b,tol,max_iter):
    """
    :variable: f - a polynomial function
    :variable: a - range of inspection starting point
    :variable: b - range of inspection ending point
    :variable: tol - tolerance given (epsilon)
    :variable: max_iter - amount of iterations the algorithm is still efficient.
    
    :return: mid - a suspicious root.

    The bisection method is a root-finding method that applies to any continuous
    functions for which one knows two values with opposite signs.
    The method consists of repeatedly bisecting the interval 
    defined by these values and then selecting the subinterval in which the function changes sign,
    and therefore must contain a root.
    """
    xl, xr, count = a, b, 0
    while np.abs(xr-xl) >= tol:
        mid = (xl+xr)/2.0
        if f(xl)*f(mid) > 0: xl = mid
        else: xr = mid
        count += 1 
    if(count > max_iter):
        print("Bisection method is not efficient for this function")
        print(f"{count} > {max_iter}")
    return mid

def find_derivative(func):
    """
    :variable: func - function given to derive.
    :return: ftag - derived function.
    
    This function uses sympy library to convert the function into it's derivative function 
    and creating a lambda function using lambdify for the derivative function.
    """
    x = symbols("x") # manipulates x into a symbol
    ftag = diff(func(x),x) # differential of x
    ftag = lambdify(x, ftag) # turns into lambda
    return ftag


def find_roots(f,a,b,step=0.1,tol=0.0001):
    """
    :variable: f - a polynomial function
    :variable: a - range of inspection starting point
    :variable: b - range of inspection ending point
    :variable: step - segments between range values (0.1 by default)
    :variable: tol - tolerance given (epsilon 0.0001 by default)

    :return: roots - list of roots which differs from a root of f(x) = 0 by less than tol.

    find_roots uses the bisection method to find polynomial roots of given function. It breaks the range of inspection into segments and performs the bisection method until it finds all roots.
    It also searchs for roots in the derivative of the function.
    """
    index = 0
    x = a 
    roots = []
    max_iter = -1 * (log(tol/(b-a))/log(2))
    fd = find_derivative(f)

    # searching for roots in given function.
    for x in np.arange(a,b + step,step): 
        if f(x) * f(x+step) < 0:
            root = bisection(f,x,x+step,tol,max_iter)
            roots.append(root)
            print(f"x{index} = {root:.3f}")
            index += 1
            # searching for roots in derived function.
        if fd(x) * fd(x+step) < 0:
            root = bisection(fd,x, x+step, tol, max_iter)
            if isclose(f(root), 0.0, abs_tol=tol):
                # root can be -0.e (still 0)
                roots.append(root)
                print(f"x{index} = {root:.3f} (from derived function)")
                index += 1 

    return roots #returns a list of roots


def create_graph(f, roots):
    """
    :variable: f - polynomial function
    :variable: roots - a list of roots from the given function.

    create_graph uses matplotlib.pyplot to visualise the graph of the given function and represent it's roots.
    """
    # creates a cartesian coordinate system.
    x = np.linspace(-11,11,1000)
    cartesian_coordinate_system = axes.Axes(xlim=(-11,11),ylim=(-11,11),figsize=(15,15))

    # labels for point mark
    xs = np.array(roots)
    ys = np.zeros(len(xs))

    # draw coertisan grid
    cartesian_coordinate_system.draw()
    plt.plot(x,f(x)) # draw function
    plt.plot(xs,ys, "ro", marker='o') # draw roots
    plt.title("Graph view:")

    # info on the lower right side.
    plt.legend([f'F(x):{f}'], loc='lower right')
    plt.grid(True) 

    # annotate labels to roots
    for x,y in zip(xs,ys):
        label = "{:.2f}".format(x)
        plt.annotate(label, # this is the text
                    (x,y), # this is the point to label
                    textcoords='offset pixels', # how to position the text
                    xytext=(0,0), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
    plt.savefig('images/function.png', bbox_inches='tight')

def main():
    p = int(input("Enter polynomial virtue (p): "))
    k = p
    construct = []
    print(f"Create a polynomial function of virtue {p}:\n")
    while k >= 0:
        if k != 0:
            construct.append(int(input(f"Enter coefficient of X**{k}:")))
        else:
            construct.append(int(input(f"Enter a free number: ")))
        k -= 1
    print(f"Enter range of inspection:\n")

    start_point = float(input("Starting point: "))
    end_point = float(input("Ending point: "))


    f = np.poly1d(construct) # constructs a function
    print(f"Function of virtue {p}\n\n{f}")
    print(f"\nInspection Range: [{start_point},{end_point}]\n")
    create_graph(f,find_roots(f, start_point, end_point))

if __name__ == "__main__":
    main()
    

#%%