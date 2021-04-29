n = int(input())
x = input()


def getandsort(n, x):
    ly = []
    if x == "gosaste":
        for i in range(1, n + 1):
            y = int(input())
            ly.append(y)
    else:
        for i in range(1, n + 1):
            y = float(input())
            ly.append(y)
    ly.sort()
    print(ly)
    if x == "gosaste":
        loopingintlist(ly, n)
    else:
        loopingfloatlist(ly, n)


def loopingintlist(ly, tedad):
    counter = 0
    l = 0
    while True:
        if counter < len(ly):
            z = ly.count(ly[counter])
            l += z
            print("fi =", z, end=" ")
            print("ri =", z / tedad, end=" ")
            print("Fi =", l, end=" ")
            print("gi =", l / tedad)
            counter += z
        else:
            break


def loopingfloatlist(ly, n):
    from math import log,ceil,floor
    for i in ly:
        if round(i) != i:  #They are decimal numbers
            xmax = ly[-1] + 0.05
            xmin = ly[0] - 0.05
            break
        else:
            xmax = ly[-1] + 0.5
            xmin = ly[0] - 0.5
            break
    k = 1 + (3.32 * log(n, 10))
    R = xmax - xmin
    l = R / ceil(k)
    print("xmin =", xmin)
    print("xmax =", xmax)
    print("R =", R)  #Range
    print("k =", ceil(k))  #strata number
    if l - floor(l) < 0.5:
        l = floor(l)
    else:
        l = ceil(l)
    print("L =",l)
    for i in range(ceil(k)):
        z = xmin + l
        print("[",xmin,",",z,")") #strata
        xmin=z
    counter = 0
    for i in ly: #Average
        counter += i
    print("Xaverage =",counter/n)

print(getandsort(n=n, x=x))
