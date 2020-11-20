def gaus_seidel(matrix, result, x_variables):
    """
        Gaus Seidel algorithm, is an iterative method used to solve a system of
        linear equations. Can be applied to any matrix with non-zero elements on the
        diagonals, convergence is ony guarenteed if the matrix is either strictly
        diagonally dominant (D), or symmetric and positive definite.

        Example:

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
        var_list - the variable column matrix (x)

    """

    size = len(matrix)
    for i in range(0, size):
        holder = result[i]
        for j in range(0, size):
            if i != j:  # if not diagonal index substract from result[i] * var
                holder -= matrix[i][j] * x_variables[j]
        x_variables[i] = holder / matrix[i][i]
    return x_variables


# xn_1 = lambda x, y, z: (b[0] - matrix[0][1] * y - matrix[0][2] * z) / matrix[0][0]
# yn_1 = lambda x, y, z: (b[1] - matrix[1][0] * x - matrix[1][2] * z) / matrix[1][1]
# zn_1 = lambda x, y, z: (b[2] - matrix[2][0] * x - matrix[2][1] * y) / matrix[2][2]


max_iteration = 25
x = [0, 0, 0]
# a = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]

matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
print(len(matrix))
b = [2, 6, 5]
# b = [4, 7, 3]
count = 0

print((f"\t Xn+1\t\t Yn+1\t\t Zn+1"))
x_init = list(map(lambda y: "{:.6f}".format(y), x))
print(f"{count}\t{x_init}")
for i in range(0, max_iteration):
    x = gaus_seidel(matrix, b, x)
    x_formatted = list(map(lambda y: "{:.6f}".format(y), x))
    print(f"{count+1}\t{x_formatted}")
    count += 1

# print("{0}\t{1}".format(count, x))


#     print(f"{count+1})\t|{xn:.6f}|\t|{yn:.6f}|\t|{zn:.6f}|")
# matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
# matrix = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
# b = [4, 7, 3]
# b = [2, 6, 5]

# 4X + 2Y = 2
# 2X + 10Y + 4Z = 6
# 4Y + 5Z = 5
#     ||
#    \  /
#     \/
#
#     0   1   2
#    ___________
# 0 | 4   2   0 |
#   |           |
# 1 | 2  10   4 |
#   |           |
# 2 | 0   4   5 |
#   |___________|
# x = [x][0]
# y = [x][1]
# z = [x][2]

#     0   1   2
#    ___________
# 0 | 1   0   0 |
#   |           |
# 1 | 0   1   0 |
#   |           |
# 2 | 0   0   1 |
#   |___________|


# xn_1 = lambda x, y, z: (b[0] - matrix[0][1] * y - matrix[0][2] * z) / matrix[0][0]
# yn_1 = lambda x, y, z: (b[1] - matrix[1][0] * x - matrix[1][2] * z) / matrix[1][1]
# zn_1 = lambda x, y, z: (b[2] - matrix[2][0] * x - matrix[2][1] * y) / matrix[2][2]

# x0, y0, z0, count = 0, 0, 0, 0
# xn, yn, zn = 0, 0, 0
# epsilon = 0.000000001
# condition = True

# print((f"\t Xn+1\t\t Yn+1\t\t Zn+1"))
# while condition:
#     print(f"{count+1})\t|{xn:.6f}|\t|{yn:.6f}|\t|{zn:.6f}|")
#     # GAUSSIAN METHOD
#     xn = xn_1(x0, y0, z0)
#     yn = yn_1(xn, y0, z0)
#     zn = zn_1(xn, yn, z0)
#     # vn = vn_1(xn, yn, zn, v0)
#     # gn = gn_1(xn, yn, zn, vn, g0)

#     # YAKOBI METHOD
#     # xn = xn_1(x0, y0, z0)
#     # yn = yn_1(x0, y0, z0)
#     # zn = zn_1(x0, y0, z0)
#     evaluated = abs(xn - x0)
#     count += 1
#     x0, y0, z0 = xn, yn, zn
#     condition = evaluated > epsilon
# print(f"\nSolution: Xn+1 = {xn:.6f}, Yn+1 = {yn:.6f}, Zn+1 = {zn:.6f}")
