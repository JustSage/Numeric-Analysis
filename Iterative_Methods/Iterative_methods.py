# Name : Sagie Baram


def square_matrix_generator(n):
    """
    Generating an n on n matrix based on user input.
    also generating a result column based on user input.
    n: size of square matrix.
    """
    matrix = [[0 for i in range(n)] for j in range(n)]
    result = [0 for i in range(n)]
    row, col = 0, 0
    for row in range(0, n):
        for col in range(0, n):
            print(f"Index {row},{col}:")
            matrix[row][col] = int(input())
        print(f"enter to row {row} in result column: ")
        result[row] = int(input())

    return matrix, result


def check_dominant_diagonal(matrix):
    """
    Check_dominant_diagonal will check if a given matrix has a dominant
    diagonal and return the result.
    """
    matrix_A = matrix.copy()  # Not changing referenced matrix.
    dominant = True
    for i in range(len(matrix_A)):
        row_sum = 0
        for j in range(len(matrix_A)):
            row_sum += abs(matrix_A[i][j])  # sums row.
        row_sum -= abs(matrix_A[i][i])  # excluding diagonal.
        if abs(matrix_A[i][i]) < abs(row_sum):
            # if the value on diagonal is lower than the row sum excluding it.
            # it is not dominant other wise it is.
            dominant = False
            break

    return dominant


def jacobi_method(matrix, result, variables):
    """
    Jacobi iterative method will iterate over each row in the matrix
    and will calculate it's variables to provide a new solution.

    Will not use the next solution therefore may cause additional iterations.
    matrix - assuming diagonally dominant.
    result - the result colum of the matrix (b)
    variables - the variable column (x)
    """
    size = len(matrix)
    var = variables.copy()
    new_vars = []  # will append the new solutions to it.
    for col in range(0, size):
        holder = result[col]
        for row in range(0, size):
            if col != row:  # if not diagonal index
                holder -= matrix[col][row] * var[row]
                # calculating variables x**(val=0,1,2,3,...)
        new_vars.append(holder / matrix[col][col])
    # not updating yr+1/zr+1 with xr+1 etc
    # divide by dominant diagonal
    return new_vars  # returns the updated values.


def guassian_seidel_method(matrix, result, variables):
    """
    Guassian-seidel iterative method will iterate over each row in the matrix
    and will calculate it's variables to provide a new solution.
    It will use the next solution of any non 0 variable from that row.

    Will deliver the result with less iterations than Jacobi iterative method.

    matrix - assuming diagonally dominant.
    result - the result colum of the matrix (b)
    variables - the variable column (x)
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
        # updating yr+1/zr+1 with xr+1 etc
        # divide by dominant diagonal
    return var  # returns the updated values.


def linear_system_iterative_method(iterative_method, matrix, result, xr, epsilon):
    """
      linear_system_iterative_method is an iterative method used to solve a system of
      linear equations. Can be applied to any matrix with non-zero elements
      on the diagonals, convergence is only guarenteed if the matrix is either
      strictly diagonally dominant (D), or symmetric and positive definite.
      this function will check if the given matrix is diagonally dominant.

      Analytic example using Jacobi iterative method:

      4X + 2Y = 2          ===>  Xr+1 = (2-2*Yr-0*Zr)/4
      2X + 10Y + 4Z = 6    ===>  Yr+1 = (6-2*Xr - 4*Zr)/10
      4Y + 5Z = 5          ===>  Zr+1 = (5-0*Xr-4*Yr)/5

      Using Guassian-seidel iterative method:

      4X + 2Y = 2       ===> Xr+1 = (2-2*Yr-0*Zr)/4
      2X + 10Y + 4Z = 6 ===> Yr+1 =(6-2*Xr+1 - 4*Zr)/10
      4Y + 5Z = 5       ===> Zr+1 = (5-0*Xr+1 - 4*Yr+1)/5

        0   1   2
       ___________
    0 | 4   2   0 |
      |           |
    1 | 2  10   4 |
      |           |
    2 | 0   4   5 |
      |___________|

    """

    def check_epsilon(epsilon, solution, next_solution):
        """
        Check_epsilon will check if the absolute value for each variable
        in solution substracted from the next solution is lower than the given
        epsilon, it will return false.
        """
        xr = [x for x in solution]
        xr_1 = [x for x in next_solution]
        check = True
        for x in range(0, len(xr)):
            if abs(xr_1[x] - xr[x]) < epsilon:
                check = False
        return check

    count = 0
    if check_dominant_diagonal(matrix) == True:
        condition = True
    else:
        condition = False
        print("Given matrix is not diagonally dominant")

    while condition:
        xr_1 = iterative_method(matrix, result, xr)
        x_formatted = list(map(lambda y: "{:.6f}".format(y), xr_1))

        print(f"{count+1}\t{x_formatted}")
        condition = check_epsilon(epsilon, xr, xr_1)
        xr = xr_1
        count += 1


def main():
    # Data Input (from class)
    xr = [0, 0, 0]  # guess

    epsilon = 0.0000001

    # convergence = true
    matrixb = [[3, -1, 1], [0, 1, -1], [1, 1, -2]]
    b = [4, -1, -3]

    # convergence = false
    matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    result = [2, 6, 5]

    print("\nResults for matrix with convergence using Jacobi")
    linear_system_iterative_method(jacobi_method, matrixb, b, xr, epsilon)
    print("\nResults for matrix with convergence using Guassian-Seidel")
    linear_system_iterative_method(guassian_seidel_method, matrixb, b, xr, epsilon)
    print("\nResults for matrix without convergence using Jacobi")
    linear_system_iterative_method(jacobi_method, matrix, result, xr, epsilon)
    print("\nResults for matrix without convergence using Guassian-Seidel")
    linear_system_iterative_method(guassian_seidel_method, matrix, result, xr, epsilon)


main()
