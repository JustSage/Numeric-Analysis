# Sagie Baram

import numpy as np
import math,warnings,TableIt
from sympy import diff, sympify,lambdify,symbols
from time import time 

# to ignore lambdify/sympify warnings.
warnings.filterwarnings("ignore")

def input_equation():
    """
    input_equation uses sympy to convert a pythonic input string into a lambda function.
    it also converts the derivative of the given function and converts it to a lambda function.
    
    the input must be done in a pythonic manner.

    Sample functions:
    f1 = x**3 - cos(x)
    f3 = x**3 - x**2 - 1
    f2 = exp(x) - 1
    f4 = 2 - 2*log(x)
    f5 = x**4 - 2*x**3 + 5

    make sure to use * if x has coefficient or ** for x power.

    :return lambdify(x,f): returns a lambda function of the function recieved as user input.
    :return lambdify(x,df): returns a lambda function of the derivative of the function above.
    """
    x = symbols('x') # counts x as a symbol
    user_input = input("Enter equation: ")
    f = sympify(user_input) # manifulpating equation to a symbol
    df = diff(f) # deriving the function
    print(f"Function derivative: {df}\n")

    # returns the equation and it's derived versions as lambdas.
    return lambdify(x,f), lambdify(x,df)

def newton_raphson(f,df,a,b,tol=0.0001):
    """
    The newton raphson method is a root-finding algorithm that which produces
    successively better approximations to the roots (or zeroes) of a real-valued function.

    This version of the newton raphson method  starts with a single-variable function f
    defined for a real variable x, the function's derivative df, and an initial guess x0 for a root of f.

    If the function satisfies sufficient assumptions and the initial guess is close, 
    then x1 = x0 - f(x0)/df(x0) until sufficiently precise value is reached.

    It has the best convergance rate out of all the root finding methods as it's quadratic (2)
    The issues with this method are that sometimes the derivative will take a long time to compute,
    and if you don't assume the right area (to find the root), the method can diverge or overshoot.

    :param f: given function.
    :param df: derivative of given function.
    :param a: starting inverval.
    :param b: end invterval.
    :param tol: tolerance (epsilon), function converges to tolerance.
    :param max_iter: maximum iterations, if passed the secant method diverges.

    :return x: the returned root.
    :return count: the amount of iterations to find xr.
    """
    table = [["iteration","df(x)","f(x)","x"]]
    count = 0

    x = (a+b)/2.0 
    nr = f(x) / df(x) 

    table.append([str(count) + " - init",round(df(x),5),round(f(x),5),round(x,5)])

    while abs(nr) >= tol or math.isclose(f(x),0.0,abs_tol=tol) is False:
        # newton method iteration
        nr = f(x)/df(x) 
        x -= nr

        count += 1  
        table.append([count,round(df(x),5),round(f(x),5),round(x,5)])

    # print the results in a table
    TableIt.printTable(table,useFieldNames=True,color=(26,156,171))
    return x,count

def secant_method(f,a,b,tol=0.0001,max_iter=100):
    """
    The secant method is a root-finding algorithm that uses a 
    succession of roots of secant lines to better approximate a root of a function f.

    The iterates xr of the secant method converge to a root of f if the initial
    values x0 and x1 are sufficiently close to the root.
    It's convergence is roughly equals to 1.618, the golden ratio.

    The secant method does not always converge, and is not always bracketed,
    but comaring to the newton method, it can handle functions that are not easily derived,
    saving processing time.
    
    :param f: given function
    :param a: initial guess (interval)
    :param b: second guess (interval)
    :param tol: tolerance (epsilon), function converges to tolerance.
    :param max_iter: maximum iterations, if passed the secant method diverges.

    :return xr: the returned root
    :return count: the amount of iterations to find xr.
    """
    table = [["iteration","xi","xi+1","f(xi)"]]
    count = 0 
    x0, x1 = a,b

    table.append([str(count) + " - init",round(x0,5),round(x1,5),round(f(x0),5)])

    while count < max_iter:
        # secant method iteration
        xr = x1 - f(x1)* ((x1 - x0)/(f(x1) - f(x0))) 
        if abs(xr - x1) < tol: break 
        else:
            x0, x1 = x1, xr
            count+=1 
            table.append([count,round(x0,5),round(x1,5),round(f(x0),5)])
    else:
        print(f"Secant method diverges after {max_iter}") 
        return None
    # print the results in a table
    TableIt.printTable(table,useFieldNames=True,color=(26,156,171))

    return xr,count
 

def main():
    # default values
    a,b = -100, 100
    step = 1.0 
    tol = 0.0001
    print(f"Intervals [a,b]: [{a},{b}]")
    print(f"Tolerance : 0.0001")
    f,df = input_equation()
    
    cyan = (51,255,255)

    nr_count = 0
    s_count = 0
    x = a

    # with this approach we iterate over a set range of intervals and perform
    # both root finding methods. this is not a common approach for these particular
    # methods as it could miss roots, that can be found easily if a user-made guess
    # is passed to the functions.
    
    # sometimes if you search "deeper", as in decrease step size, 
    # you can find some of the missing roots.

    # the loop will try to find roots in newton, than secant, show how much time
    # both methods ran to find the root, and print the process in a nice table view.

    while True:
        for x in np.arange(a,b,step):
            if f(x)*f(x+step) < 0:
                TableIt.printTable([["Newton Raphson root finding method:"]],color=cyan)
                start_time = time()
                root, newton_iter = newton_raphson(f,df,x,x+step)
                end_time = time()
                print(f"It took {newton_iter} iterations to find root = {root:.5} in interval [{int(x)},{int(x+step)}] using Newton Raphson method")
                print(f"It took {round(end_time - start_time,7)} to find the root\n")
                nr_count += 1
                TableIt.printTable([["Secant root finding method:"]],color=cyan)
                start_time = time()
                try:
                    root, secant_iter = secant_method(f,x,x+step)
                    s_count += 1
                    print(f"It took {secant_iter} iterations to find root = {root:.5} in interval [{int(x)},{int(x+step)}] using Secant method")                   
                except: ValueError(None)
                finally: 
                    end_time = time()
                    print(f"It took {round(end_time - start_time,7)} to run Secant method\n")
                
        if s_count == 0 or nr_count == 0:
            print(f"Search deeper?\n1.Yes\n2.No")
            select = int(input("Enter selection: "))
            if select == 1 and step > tol:
                print(f"Changing step to {step/10}")
                step /= 10
            else:
                if nr_count == 0:
                    print(f"No roots found for intervals [{a},{b}] with step: {step} using Newton Raphson")
                if s_count == 0:
                    print(f"No roots found for intervals [{a},{b}] with step: {step} using Secant")
                break
        else: break

if __name__ == '__main__':
    main()

# will improve this implementation, but this meets the assignment requirement.
    