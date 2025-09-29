def upside(digit):
    if digit==0 :
        return 0
    elif digit==1:
        return 1
    elif digit==6:
        return 6
    elif digit==9:
        return 9
    elif digit==8:
        return 8
    else :
        return -1
def isupside(num):
    orginal =num
    flip=0
    while num>0:
        digit=num%10
        flipdigit=upside(digit)
        if flipdigit == -1:
            return False
        flip =flip*10+flipdigit
        num//=10
    return flip==orginal
for num in range(1,1001):
    if isupside(num):
        print(num)
