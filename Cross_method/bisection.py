#%%
## module bisection
import axes
import numpy as np
import matplotlib.pyplot as plt
import sympy
import math
def f2(x): return x**4 + x**3 -3*x**2

def bisection (f,a,b,tol):
    xl, xr, count = a, b, 0
    while np.abs(xl - xr) >= tol:
        mid = (xl+xr)/2.0
        if f(xl)*f(mid) > 0: xl = mid
        else: xr = mid
        count += 1 
    return mid

def find_derivative(func):
    x = sympy.symbols("x") # manipulates x into a symbol
    ftag = sympy.diff(func(x),x) # differential of x
    ftag = sympy.lambdify(x, ftag) # turns into lambda
    return ftag

def find_roots(f,a,b,step=0.1,tol=1e-10):
    index = 0
    x = a 
    result = []

    # searching for roots in given function.
    for x in np.arange(a,b + step,step): 
        if f(x) * f(x+step) < 0:
            root = bisection(f,x,b,tol)
            result.append(root)
            print(f"x{index} = {root}")
            index += 1

    # searching for roots in derived function.
    fd = find_derivative(f)
    for x in np.arange(a, b + step,step):
        if fd(x) * fd(x+step) < 0:
            root = bisection(fd, x, x+step, tol)
            # result.append(root)
            # if root close to 0 or 0
            if math.isclose(f(root), 0.0, abs_tol=tol):
                print(f"x{index} = {0}")
                result.append(0) # append 0 instead of the near 0 number.
                index += 1
    # result = np.array([roots], dtype='f')
    return result

a,b = -3.0,2.0
tol = 1e-10
step = 0.1
result = find_roots(f2,a,b,step,tol)
print(result)

# set environment
x = np.linspace(-11,11,1000)
cartesian_coordinate_system = axes.Axes(xlim=(-11,11),ylim=(-11,11),figsize=(15,15))

# labels for point mark
xs = np.array(result)
ys = np.zeros(len(xs))

# draw coertisan grid
cartesian_coordinate_system.draw()
plt.plot(x,f2(x)) # draw function
plt.plot(xs,ys, "ro", marker='P') # draw roots
plt.title("Graph view:")
# info on the lower right side.
plt.legend(['F(x) = x**4 + x**3 - 3x**2'], loc='lower right')
plt.grid(True) 
# mplcursors.cursor().connect('pick root', result)

for x,y in zip(xs,ys):
    label = "{:.2f}".format(x)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords='offset pixels', # how to position the text
                 xytext=(0,0), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
# %%
