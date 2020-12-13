<h1> Bisection Method </h1>

**Dependencies:**

	Requires python version >= 3.6.
	Requires numpy, sympy.
	Optional : matplotlib & jupyter server.

- `pip install numpy`
- `pip install sympy`
- `pip install matplotlib`

**External axes class:**

	used to display coertisan grid.

**How to Use:**

	1.Enter the polynomial virtue.
	2.Enter the coefficient for each of the variables in the polynomial.
	3.Enter a starting point and an ending point (inspection range).
	4.The program will compute the polynomial using bisection method.
	5.Result will be presented as output and graphically.
	   * Graph will be saved in ./images
	   * Output will display both roots from function and derived function.

	If you have jupyter server you can view the graph after running the code.
	On the top and bottom of the bisection.py file you can click run Above/Below next to the #%% signs.

**Output Example:**

	x**4 + x**3 - 3x**2
	inspection range: [-3,2]
	x0 = -2.303
	x1 = 1.303
	x2 = 0.000
![Example](images/example.png)
