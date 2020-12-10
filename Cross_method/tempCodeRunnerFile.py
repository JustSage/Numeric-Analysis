 for x in np.arange(-3.0,2.0 + step,step):
        if f(x) * f(x+step) < 0:
            root = bisection(derive_func(f), x, x+step, tol)
            print(f"x{index} = {root}")