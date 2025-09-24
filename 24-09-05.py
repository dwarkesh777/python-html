## FUNCTIONS,SCOPING AND ABSTRACTION
## WHY FUNCTIONS?
- reusability
- compact and easy code to understand
- modularity
## definding function
def greet():
    print("hello world")
## calling function
greet()
## function specification
- it include function name,parameters(if any) , and return type.
- ideally ,it mean include docstring
def add(x,y): # parameter
    """
    this function adds two number.
    
    parameter :
    - x(int):the first number
    - y(int):the second number
    
    return
    int: the sum of two number x and y
    """
    result = x+y
    print(f"sum is:",result) 
## calling function
add(1,20) ## 1 and 20 are the argument
## 1.No parameter and No return type
def printline():
    s = input("enter the name = ")
    print(s)
printline()
## 2.with parameter and No return type
def printline(s):
        print(s)
        
m = input("enter the name = ")

printline(m)
## 3.with parameter and with return type
def printline(s):
        print(s)
        
m = input("enter the name = ")
t=printline(m)
print(t)
## 4.No parameter and with return type
def printline():
    m = input("enter the name = ")
    return m
        
t=printline()
print(t)
## wrt function evenodd to check whether given no is even or odd
def evenodd():
    s=int(input("enter number"))
    if s%2==0:
        print("even number",s)
    else:
        print("odd number",s)
evenodd()
## returning multiple values
def sumsub(x,y):
    sum=x+y
    sub=x-y
    return sum,sub
sumsub(8,9)

x,y=sumsub(8,9)
print(x)
print(y)

## defind a function  a calculator that return addition,sub,multi,divison and **
def calc(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    expo=x**y
    div=x//y
    return sum,mul,expo,sub,div
calc(4,5)
## function parameter and argument 
- a parameter is a variable name listed in the function parenthesis
- an argument is the value passed through the parameter when you call the function
## default argument
def square(x=20):
    return x*x
print(square())# default
print(square(10))
## positional argument
- the number of argument and position of argument must be matched.
- if we changed the order ,the result may changed.
- if we change the number of argument , we will get error
def sub(x,y):
    return x-y
print(sub(100,200))
print(sub(200,100))
# print(sub(100,200,300))
## keyword Argument
- we can pass the argument values by keyword name . the order does not matter.
- we can use postional and keyword argument simultaneously.
- the strict order is first positional and the keyword argument 
def wish(name,msg):
    print("hello",name,msg)
wish(name='python',msg="how are you?")
wish(msg="how are you?",name='python')
## second case
wish("c++","goodmorning")
## third case
wish("c++",msg="goodmorning")

wish(name="go","good afternoon")
## variable length argument
def sum(*n):
    total=0
    for i in n :
        total+=i
    print("the sum is",total)
    sum(10)
    sum(10,20)
    sum(10,20,30)
## global and variables
x = 5
def fun():
    x=100
    print(x)
    fun()
x = 5
def fun():
    global x
    x=100
    print(x)
    fun()
    print(x)
## python seraches through yhe scope using following rule
- lebg-
- local
- enclosed
- globle
- bultin
## wrt to take a number input from the user and check whether it is with in range by definding a function name numberrange
def numberrange():
    x=int(input("enter number"))
    if x>=0 and x<=100:
        print("your number in range",x)
    else:
        print("your number is out of range",x)
numberrange()
## task
- input:123456
- output:623451
case:1
def task():
    num =input("enter num:")
    listn= list(num)
    listn[0],listn[-1]=listn[-1],listn[0]
    print(listn)
task()
case:2
x = input('enter any num : ')  
print(x[-1] + x[1:(len(x)-1)] +x[0])
case:3
# swap first and last
def swap(number):
    #find num of digit
    numdigit=0
    temp=number
    while temp>0:
        temp//=10
        numdigit+=1
    #handle one digit
    if numdigit<=1:
        return number
    #extract first and last
    f=number//(10**(numdigit-1))
    l=number%10
    #remove first and last digit
    numwithout=(number%(10**(numdigit-1)))//10
    #swaped number
    swapnum=l*(10**(numdigit-1))+ numwithout*10+f
    return swapnum
num=int(input("enter num"))
swap(num)
