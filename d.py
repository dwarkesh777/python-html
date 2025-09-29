for  i in range (1,10000):
    sum=0
    mult=1
    s=i
    while s>0:
        d=s%10
        sum=sum+d
        mult=mult*d
        s=s//10
    temp=sum+mult
    if i==temp:
        print(i)