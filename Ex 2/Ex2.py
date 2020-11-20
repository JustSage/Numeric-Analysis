# Ex2 - Monday Oct 19, 2020
# Name: Sagie Baram, ID: 205591829
# Name: Eden Mozes, ID: 315997049


def machinePercisionFinder(epsilon):
    while (1 + epsilon) != 1:
        prev_eps = epsilon
        epsilon = epsilon / 2
    print("Machine Percision is \u03B5 : ", prev_eps)


machinePercisionFinder(0.5)
