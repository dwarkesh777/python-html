 ## wrt to determind if a number is odd or even 

a = int(input("enter the digit"))
if a%2==0:
    print("digit is even")
if a%2!=0:
    print("digit is odd")

## wrt a program the odd number from 1 to 10

for i in range (1,10):
    if i%2==0:
        print(i)

a = int(input("enter the number"))
for i in range(1,11):
    print(a*i)

## wrt to ask a user input 10 number and print the avg of number
sum=0
for i in range (1,11):
    a=int(input("enter the num: "))
    sum+=a
print(sum/10)

## wrt to cheack a given number prime or nor
a = int(input("enter the number"))
c = 0
for i in range(2,a):
    if a%2==0:
        c=1
        
if c==1:
        print("yes")
else:
        print("no")


num=int(input("enter the number"))
temp=num
sum=0
while temp!=0:
    count = temp%10
    sum=sum+count*count*count
    temp=temp//10

if sum==temp:
    print("yes")

a,b=0,1
for i in range(10):
    print(a , end=" ")
    a,b=b,a+b

for i in range(1,200):
    if i%7 ==2 and i%5 ==2 and i%6==3 :
        print(i)



total_heads = 10
total_legs = 26

legs_per_sheep = 4
legs_per_hen = 2

for num_sheep in range(total_heads + 1):
    num_hen = total_heads - num_sheep
    
    current_legs = (num_sheep * legs_per_sheep) + (num_hen * legs_per_hen)
    
    if current_legs == total_legs:
        print(f"Number of sheep: {num_sheep}")
        print(f"Number of hen: {num_hen}")
        break 


## wrt to find smallest positive number divisible by number from 1 to 10
for i in range(true)
    if i%1==0 and i%2==0 and i%3==0 and i%4==0 and i%5==0 and i%6==0 and i%7==0 and i%8==0 and i%9==0 and i%10==0:
        print(i)
        break

## wrt to find integer posotive solution to the eqaution  $x^2 - 2y^2=1$ find x and y  in 1 to 100

for i in range(1,101):
    for j in range(1,101):
        if i**2-2*j**2==1:
            print(f"x={i} , y={j}")


## wrt to ask user for an hour beetween ask enter am or pm and also ask them how many hour in to the futer to go print the hour am or pm 
a=int(input("enter the hour"))
type = input("enter the type(am or pm)")
b = int(input("enter future to go"))




current_hour = int(input("Enter an hour (1-12): "))
am_pm = input("Enter 'am' or 'pm': ")
hours_to_add = int(input("How many hours into the future? "))

if am_pm == 'pm' and current_hour != 12:
    current_hour += 12
elif am_pm == 'am' and current_hour == 12: 
    current_hour = 0

new_hour_24 = (current_hour + hours_to_add) % 24

if new_hour_24 == 0:  
    final_hour = 12
    final_am_pm = 'am'
elif new_hour_24 == 12:
    final_hour = 12
    final_am_pm = 'pm'
elif new_hour_24 > 12:
    final_hour = new_hour_24 - 12
    final_am_pm = 'pm'
else:
    final_hour = new_hour_24
    final_am_pm = 'am'

print(f"The hour in the future will be: {final_hour} {final_am_pm}")

hour = int(input("Enter an hour (1-12): "))
ap = input("Enter 'am' or 'pm': ")
fhours= int(input("How many hours into the future? "))
for i in range (0,fhours):
    hour+=1
    if hour>12:
        hour=1
    if hour==12:
        if ap=="am":
            ap="pm"
        else:
            ap="am"
print(hour,ap)

