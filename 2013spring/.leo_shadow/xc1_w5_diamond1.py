#@+leo-ver=4-thin
#@+node:portable_leo.20131025221745.3023:@shadow c1_w5_diamond1.py
#@@language python


def 菱形(n):
    數列1 = [x+n for x in range(0, n)]
    數列2 = list(range(n, 0, -1))
    數列3 = zip(數列1, 數列2)
    for i in 數列3:
        for j in range(2*n):
            if j == i[0] or j == i[1]:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    數列4 = [x for x in range(2, n+1)]
    數列5 = [x+n-2 for x in range(n, 0, -1)]
    數列6 = zip(數列4, 數列5)
    for i in 數列6:
        for j in range(2*n):
            if j == i[0] or j == i[1]:
                print("*", end="")
            else:
                print(" ", end="")
        print()

n = 20
菱形(n)
#@-node:portable_leo.20131025221745.3023:@shadow c1_w5_diamond1.py
#@-leo
