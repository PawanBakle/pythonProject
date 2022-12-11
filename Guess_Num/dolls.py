for i in range(int(input())):
    n=int(input())
    l=[]

    for i in range(n):
        k=(int(input()))

        if k not in l:
            l.append(k)
        else:
            l.remove(k)
    print(l[0])