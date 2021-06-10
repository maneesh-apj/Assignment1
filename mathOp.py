x=int(input("Enter first number : "))

y= int(input("Enter second number : "))

print("Enter", "1 to Add", "2 to Subtract", "3 to devide", sep="\n")

##op=int(input("enter 1 to Add", "2 to Subtract", "3 to devide",sep="\n")) within int function it is not working
op=int(input("Enter number : "))

if op==1:
    print(x+y)
elif op==2:
    print(x-y)
elif op==3:
    if y==0:
        print(0)
    else:
        print(x/y)
else:
    print("Enter value is not valid")