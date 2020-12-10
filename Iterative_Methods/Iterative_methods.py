# Name : Sagie Baram

import numpy as np

def square_matrix_generator(n):
    """
    Generating an n on n matrix based on user input.
    also generating a result column based on user input.
    n: size of square matrix.
    """
    matrix = np.zeros((n, n))  # initializing
    b = np.zeros(n)
    for row in range(0, n):
        for col in range(0, n):
            matrix[row][col] = int(input((f"Matrix[{row}],[{col}]: ")))
        b[row] = int(input(f"b[{row}] = "))
    return matrix, b

def swapRows(matrix, r1, r2):
    if len(np.shape(matrix)) == 1:
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
    else:
        matrix[[r1, r2], :] = matrix[[r2, r1], :]


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
    new_vars = []  # will append the new solutions to it.
    for col in range(0, size):
        holder = result[col]
        for row in range(0, size):
            if col != row:  # if not diagonal index
                holder -= matrix[col][row] * variables[row]
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
    var = list(variables)
    for col in range(0, size):
        holder = result[col]
        for row in range(0, size):
            if col != row:  # if not diagonal index
                holder -= matrix[col,row] * var[row]
                # calculating variables x**(val=0,1,2,3,...)
        var[col] = holder / matrix[col,col]
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
    2 | 0   4   2 |
      |___________|

    """

    def check_dominant_row(matrix):
        """
        checking if given matrix has dominant row.
        """
        # for each row 
        size = len(matrix)
        for i in range(0, size) :          
            sum_rows = 0
            for j in range(0, size) : 
                if i != j:
                    sum_rows += abs(matrix[i,j])      
            if (np.abs(matrix[i,i]) < sum_rows) : 
                return False
        return True 

    def check_valid_matrix(matrix, result, epsilon):
        """
        swapping rows with pivot if neccessary.
        """
        print(f"Given Matrix: \n{matrix}\n Given result column:\n{result}\n")
        check = False
        n = len(matrix)
        scale = np.zeros(n)
        for i in range(n):
            scale[i] = max(np.abs(matrix[i, :]))  # entering all max values in each row to scale.

        for k in range(0, n - 1):
            pivot = (np.argmax(np.abs(matrix[k:n, k]) / scale[k:n]) + k)  # Find row containing element with largest relative size
            if abs(matrix[pivot, k]) < epsilon:
                print( "Given Matrix is singular therefor can't use an iterative method\nExiting program.") 
                exit(1) # If row change is needed:
            if pivot != k:
                check = True
                print(f"Swapping row: {pivot} with row: {k}\n")
                # swapping k and pivot indexes in matrix, result(b) and max variable array.
                swapRows(result, k, pivot)  # result(b) swap
                swapRows(scale, k, pivot)  # max variable array swap
                swapRows(matrix, k, pivot)  # matrix swap

        if check is True:
            print(f"Rows were swapped to make the matrix coefficient\n")
            print(f"Given Matrix: {matrix}\n Given result column:{result}")

    def check_epsilon(epsilon, xr, xr_1):
        """
        Check_epsilon will check if the absolute value for each variable
        in solution substracted from the next solution is lower than the given
        epsilon, it will return false.
        """
        for x in range(0, len(xr)):
            if abs(xr_1[x] - xr[x]) < epsilon:
                return False
        return True

    count = 0  # Iteration count
    condition = True  # Will have check_epsilon result
    check_valid_matrix(matrix, result, epsilon)
    if check_dominant_row(matrix) is False:
        print("Given matrix isn't dominant\nExiting Program")
        exit(1)


    while condition:
        xr_1 = iterative_method(matrix, result, xr)
        x_3float = list(map(lambda y: "{:.3f}".format(y), xr_1))
        print(f"{count+1}\t{x_3float}")
        condition = check_epsilon(epsilon, xr, xr_1)
        xr = np.copy(xr_1)
        count += 1
    x_3float = list(map(lambda y: "{:.3f}".format(y), xr))
    print(f"Final solution:{x_3float}")


def main():
    # Data Input (from class)
    epsilon = 0.001  # tolerance
    x0 = np.array([0,0,0])

    # convergence = true
    conv_matrix = np.array([[3, -1, 1], [0, 1, -1], [1, 1, -2]])
    conv_result = np.array([4, -1, -3])

    # convergence = false
    no_conv_matrix = np.array([[4, 2, 0], [2, 10, 4], [0, 4, 5]])
    no_conv_result = np.array([2, 6, 5])

    print("Choose from sample data or create your own matrix:")
    print("1. Create my own")
    print("2. Use sample data (default)")
    selection = int(input("Enter selection: "))
    if selection == 1:
        size = int(input("Enter size (square matrix): "))
        matrix, result = square_matrix_generator(abs(size))
    else:
        print("Choose an example:")
        print("1. With no convergence")
        print("2. With convergence (default)")
        selection = int(input("Enter selection: "))
        if selection == 1:
            matrix, result = no_conv_matrix, no_conv_result
        else:
            matrix, result = conv_matrix, conv_result

    print("Choose an iterative method:")
    print("1. Jacobi method")
    print("2. Guassian Seidel method (default)")
    selection = int(input("Enter selection: "))
    if selection == 1:
        linear_system_iterative_method(jacobi_method, matrix, result, x0, epsilon)
    else:
        linear_system_iterative_method(guassian_seidel_method, matrix, result, x0, epsilon)

main()
