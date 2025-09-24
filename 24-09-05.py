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
