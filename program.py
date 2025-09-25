# pg1
x = int(input("enter a digit:"))
y=x*x
digits=0
while y>0:
        digits+=1
        y//10
        
div=digits//2

last=y%(10**div)
first=y//(10**div)

if x==last+first:
    print("num is KAPREKAR",x)
else:
    print("not")
#wrt find smallest number satisfied following condition
from given number if 1 remove the last digit and puting at the front at the number the number of form is 1.5 time old number
x=10 
found=False
while not found:
    d=x%10
    q=x//10
    
    t=q
    digits=0
    while t>0:
        digits+=1
        t//10
        
    if digits>0:
        y=d*(10**digits)+q
        
    if y==x*1.5:
        print("smallest is ",x)
        print("new number",y)
        found=True
    x+=1
