import logging
import sys

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)

output_file_handler = logging.FileHandler("output.log")
stdout_handler = logging.StreamHandler(sys.stdout)

a_logger.addHandler(output_file_handler)
a_logger.addHandler(stdout_handler)


def linear_system_iterative_method(matrix, result, x_variables):
    """
        linear_system_iterative_method is an iterative method used to solve a system of
        linear equations. Can be applied to any matrix with non-zero elements
        on the diagonals, convergence is ony guarenteed if the matrix is either
        strictly diagonally dominant (D), or symmetric and positive definite.

        Analytic Example:

        4X + 2Y = 2          ===>  Xr+1 = (2-2*Y-0*Z)/4
        2X + 10Y + 4Z = 6    ===>  Yr+1 = (6-2*X - 4*Z)/10
        4Y + 5Z = 5          ===>  Zr+1 = (5-0*X-4*Y)/5

        0   1   2
       ___________
    0 | 4   2   0 |
      |           |
    1 | 2  10   4 |
      |           |
    2 | 0   4   5 |
      |___________|

        matrix - assuming it's an N*N matrix (A)
        result - the result column matrix (b)
        x_variables - the variable column matrix (x)
    """
    size = len(matrix)
    for col in range(0, size):
        holder = result[col]
        for row in range(0, size):
            if col != row:  # if not diagonal index
                holder -= matrix[col][row] * x_variables[row]
                # calculating variables x**(val=0,1,2,3,...)
        x_variables[col] = holder / matrix[col][col]
        # divide by dominant diagonal
    return x_variables  # returns the updated values.


def check_epsilon(epsilon, solution, next_solution):
    xr = solution[0]
    xr_1 = next_solution[0]
    check = abs(xr_1 - xr)
    return check < epsilon


# Data Input (from class)

max_iterations = int(input("Enter maximum iterations: "))
x = [0, 0, 0]  # guess

# convergence = false
matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
result = [2, 6, 5]

# convergence = true
matrixb = [[3, -1, 1], [0, 1, -1], [1, 1, -2]]
b = [4, -1, -3]

condition = True
count = 0

print((f"\t Xn+1\t\t Yn+1\t\t Zn+1"))  # test data got 3 variables to iterate
x_init = list(map(lambda y: "{:.6f}".format(y), x))  # maps 6 decimals after .
print(f"{count}\t{x_init}")

while condition:
    # for i in range(0, max_iterations):
    solution = linear_system_iterative_method(matrixb, b, x)
    x_formatted = list(map(lambda y: "{:.6f}".format(y), x))
    # a_logger.debug((f"{count+1}\t{x_formatted}"))  # print count and formatted values.
    print(f"{count+1}\t{x_formatted}")  # print count and formatted values.
    condition = check_epsilon(0.001, x, solution)
    count += 1
    x = solution
