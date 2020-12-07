import numpy as np

def f(x):
    return x**3 + 5*x**2 + 5

def make_my_day(f,a,b,c,d,n):
    """
    integral between -1 and 1 of f(x) = w0*f(x0) + w1*f(x1)
    :return: The value of the integral 

    """
    # change the x and y values to fit an integral between -1 and 1 
    g = lambda x: (d+c)/2 + (d-c)*x/2
    h = lambda y: (a+b)/2 + (a-b)*y/2

    # the legendre polynomial
    xs, cs = np.polynomial.legendre.leggauss(2)
    # the outer integral over x
    def inner_f(y):
        sum = 0
        for i in range(n):
            sum+= cs[i]*f(g(xs[i]),y)
        return sum

    # the outer integral over y
    sum = 0
    for i in range(n):
        sum += cs[i] * inner_f(h(xs[i])) 
    return sum