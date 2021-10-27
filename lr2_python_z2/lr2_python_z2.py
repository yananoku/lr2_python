def sp (a = tuple (input('Введите число: ').split())):
    x = []
    y = []
    z = []
    i = 0
    for i in range(len(a)):
        if int(a[i]) %2==0: 
            x.append(a[i])
        if int(a[i]) %3==0:
            y.append(a[i])
        if int(a[i]) %5==0:
            z.append(a[i])
    print (x,y,z)

sp()