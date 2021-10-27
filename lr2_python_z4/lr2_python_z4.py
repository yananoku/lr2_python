def  niut (a, n):
    if a<0 and n % 2==0:
        return "Отрицательное число и четная степень"
    appr = a/n
    while True:
        x = 1/n * ((n-1)*appr + a/appr**(n-1))
        if abs(appr - x)<0.00001:
            return x
        appr = x

a = int(input("Введите число: "))
n = int(input("Введите степень корня: "))
print (niut(a,n))
            


