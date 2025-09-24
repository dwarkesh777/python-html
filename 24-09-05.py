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
