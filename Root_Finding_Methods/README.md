<h1> Newton Raphson & Secant Methods </h1>

**Dependencies:**

	Requires python version >= 3.6.
	Requires numpy, sympy.
	Requires TableIt file to be in the same directory as methods.py file

- `pip install numpy`
- `pip install sympy`

**External TableIt class:**

	Used to display the output in a neat table.

**How to Use:**

	There are pre-defined values for intervals/initial guesses due to the assignment requirement.
	1.Enter a function in a pythonic syntax.

	Examples:

	f1 = x**3 - cos(x)
	f3 = x**3 - x**2 - 1
	f2 = exp(x) - 1
	f4 = 2 - 2*log(x)
	f5 = x**4 - 2*x**3 + 5

	2.The program will output Newton Raphson output -> Secant output iteratively.
	3.If there were no roots found in either of the functions
		the user can decrease step size to search deeper (can't go below tolerance).
	4.If no roots were found by searching deeper, it means the guess was not close enough.

**Please note:**

	Initial guess for newton is (a+b)/2.0 which may yield inaccurate guesses due to
	traversing between -100 to 100 in steps of 1.0.
	This was done due to the assignment requirements, will be fixed.

**Output example:**

	Initial values: (pre-defined)

	intervals : [-100,100]
	tolerance : 0.0001
	step : 1.0

	function : x**3 - cos(x)
	function derivative: 3*x**2 + sin(x)


	+-------------------------------------+
	| Newton Raphson root finding method: |
	+-------------------------------------+
	+-----------------------------------------------+
	| iteration | df(x)     | f(x)      | x         |
	+-----------+-----------+-----------+-----------+
	| 0 - init  | 1.22943   | -0.75258  | 0.5       |
	| 1         | 4.60723   | 0.93282   | 1.11214   |
	| 2         | 3.27182   | 0.13875   | 0.90967   |
	| 3         | 3.019     | 0.00539   | 0.86726   |
	| 4         | 3.00856   | 1e-05     | 0.86548   |
	| 5         | 3.00854   | 0.0       | 0.86547   |
	+-----------------------------------------------+
	It took 5 iterations to find root = 0.86547 in interval [0,1] using Newton Raphson method
	It took 0.0003462 to find the root

	+-----------------------------+
	| Secant root finding method: |
	+-----------------------------+
	+-----------------------------------------------+
	| iteration | xi        | xi+1      | f(xi)     |
	+-----------+-----------+-----------+-----------+
	| 0 - init  | 0.0       | 1.0       | -1.0      |
	| 1         | 1.0       | 0.68507   | 0.4597    |
	| 2         | 0.68507   | 0.84136   | -0.45285  |
	| 3         | 0.84136   | 0.87035   | -0.07088  |
	| 4         | 0.87035   | 0.86536   | 0.01475   |
	| 5         | 0.86536   | 0.86547   | -0.00035  |
	+-----------------------------------------------+
	It took 5 iterations to find root = 0.86547 in interval [0,1] using Secant method
	It took 0.0004313 to run Secant method
