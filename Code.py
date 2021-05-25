def main():
    total = int(input("enter total number of list: "))
    intype = input("Choose type: ")
    action  = input("enter an action: ")
    l = [] # l is the main list
    for i in range(total):
        if intype == "int":
            y = int(input())
            l.append(y)
        else:
            y = float(input())
            l.append(y)
    l.sort()
    print(l)
    print(end="\n")

    if action == "jadval":
        jadval(l,total,intype)
    elif action == "charak":
        charak()


def jadval(l,total,intype):
    from math import log , ceil , floor , pow
    z = []
    lf = []
    # calculating decimal number
    if intype == "int":
        f = 0.5
        dec = 0
    else:
        for i in l:
            z.append(str(i))
        for j in z:
            y = j.split(".")
            lf.append(len(y[-1]))
        lf.sort()
        dec = lf[-1]
        f = (1 /(10 ** dec)) / 2
    xmin = l[0] - f
    xmax = l[-1] + f
    # calculating R L K xmax xmin
    R = round(xmax - xmin,dec + 2)
    k = ceil(1 + (3.32 * log(total,10)))
    L = R / k
    X = 0
    for i in l: # average
        X += i
    if intype == "int":
        if L - floor(L) < 0.5:
            L = round(L)
        else:
            L = ceil(L)
    else:
        L = round(L,dec)
    first_element = xmin
    lis = []
    fi_list = []
    counter = 0
    Fi = 0
    gi = 0
    for i in range(k): # printing row elements
        print("[",round(first_element,dec+1),",",round(first_element + L,dec+1),")",end=" | ")
        presenter = (round(first_element,dec+1)+round(first_element + L,dec+1)) / 2
        print("Xi =",round(presenter,dec+2),end=" | ")
        [lis.append(i) for i in l if round(first_element, dec + 1) <= i < round(first_element + L, dec + 1)]
        print("fi =", len(lis), end=" | ")
        print("ri =", round(len(lis) / total,dec+2),end=" | ")
        fi_list.append(len(lis))  # for access to fi
        Fi += fi_list[counter]
        print("Fi =",Fi,end=" | ")
        counter += 1
        gi += len(lis)/total
        print("gi =",round(gi,dec+2),end=" | ")
        print("(xi-X) =",round(round(presenter,dec+2)-round(X/total,2),2),end=" | ")
        print("(xi-X)**2 =",round(pow(round(round(presenter,dec+2)-round(X/total,2),2),2),2))
        lis.clear()
        first_element = first_element + L
        print(end="\n")
    # printing calculated information
    print("xmin =" , xmin , ", xmax =" ,format(xmax,".2f") , ", R = xmax - xmin =" , R , ", K =1+3.32logn =" , k , ", L = R/K =" , L ,", X =",round(X/total,2),end=" ")
    mod(l)
    med(l)




def mod(l): #most repeated element of a list
    maximum = 0
    mod_list = []
    for i in l:
        counter = l.count(i)
        if counter > l.count(maximum):
            maximum = i
        else:
            maximum = maximum
    [mod_list.append(j) for j in l if l.count(j) >= l.count(maximum)]
    print(", mod =",set(mod_list),end=" ")

def med(l): # The middle element or elements
    n = len(l)
    from math import floor
    if n % 2 == 0:
        y = (n/2) - 1
        med = (l[int(n/2)] + l[int(y)]) / 2
    else:
        med = l[floor(n/2)]
    print(", med =",med)





main()



def charak():
    pass
