import logging
import sys

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)

output_file_handler = logging.FileHandler("output.log")
stdout_handler = logging.StreamHandler(sys.stdout)

a_logger.addHandler(output_file_handler)
a_logger.addHandler(stdout_handler)


def guassian_seidel_method(matrix, result, variables):
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
    var = variables.copy()
    for col in range(0, size):
        holder = result[col]
        for row in range(0, size):
            if col != row:  # if not diagonal index
                holder -= matrix[col][row] * var[row]
                # calculating variables x**(val=0,1,2,3,...)
        var[col] = holder / matrix[col][col]
        # divide by dominant diagonal
    return var  # returns the updated values.


def jacobi_method(matrix, result, variables):
    size = len(matrix)
    var = variables.copy()
    new_vars = []
    for col in range(0, size):
        holder = result[col]
        for row in range(0, size):
            if col != row:  # if not diagonal index
                holder -= matrix[col][row] * var[row]
                # calculating variables x**(val=0,1,2,3,...)
        new_vars.append(holder / matrix[col][col])
        # divide by dominant diagonal
    return new_vars  # returns the updated values.


def check_epsilon(epsilon, solution, next_solution):
    xr = [x for x in solution]
    xr_1 = [x for x in next_solution]
    check = True
    for x in range(0, len(xr)):
        if abs(xr_1[x] - xr[x]) < epsilon:
            check = False
    return check


# Data Input (from class)
# max_iterations = int(input("Enter maximum iterations: "))
xr = [0, 0, 0]  # guess

# convergence = false
matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
result = [2, 6, 5]

# convergence = true
matrixb = [[3, -1, 1], [0, 1, -1], [1, 1, -2]]
b = [4, -1, -3]

condition = True
epsilon = 0.0000001
count = 0


# while condition:
#     xr_copy = xr.copy()
#     xr_1 = guassian_seidel_method(matrix, result, xr)
#     x_formatted = list(map(lambda y: "{:.6f}".format(y), xr))
#     # a_logger.debug((f"{count+1}\t{x_formatted}"))  # print count and formatted values.
#     print(f"{count+1}\t{x_formatted}")
#     condition = check_epsilon(epsilon, xr, xr_1)
#     xr = xr_1
#     count += 1

while condition:
    xr_copy = xr.copy()
    xr_1 = jacobi_method(matrixb, b, xr)
    x_formatted = list(map(lambda y: "{:.6f}".format(y), xr))
    print(f"{count+1}\t{x_formatted}")
    # a_logger.debug((f"{count+1}\t{x_formatted}"))  # print count and formatted values.
    condition = check_epsilon(0.00000001, xr, xr_1)
    xr = xr_1
    count += 1
