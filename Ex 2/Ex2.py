# Machine Precision :
# Computer numbers (floating point numbers) are a finite subset of rational numbers.
# There is a smallest positive computer number ε so that 1+ε > 1.

# Berkeley : https://math.berkeley.edu/~mgu/MA128AFall2017/MA128ALectureWeek2.pdf

def machinePercisionFinder(epsilon):
    while (1 + epsilon) != 1:
        prev_eps = epsilon
        epsilon = epsilon / 2
    print("Machine Percision is \u03B5 : ", prev_eps)


machinePercisionFinder(0.000005)
