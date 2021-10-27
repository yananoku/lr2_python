def numb (n = int (input('Enter a number: '))):
    rev = 0
    otr = 0
    if n<0: 
        otr += 1
        n*=-1
    while n > 0:
        rem = n % 10      
        rev = rev * 10 + rem
        n = n//10
    if otr !=0:
        print (rev*-1)
    else:
        print (rev)

numb ()