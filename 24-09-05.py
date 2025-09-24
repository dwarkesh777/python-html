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
