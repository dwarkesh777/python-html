for n in range(1, 30):
    temp= n

    while temp  != 1 #and temp != 4:
        r = s = 0
        while temp > 0:
            r = temp % 10
            s += r**2
            temp //= 10
        
        temp = s

    if temp == 1:
        print(n, end = " ")
