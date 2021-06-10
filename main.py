from os import sep


input1= input("Please enter \"A\" having length 10 character : ")

print("A" in input1)
if (len(input1)==10 and ("A" in input1)):
   print("input string is correct")
else:
     print("input is not in correct format")

print(input1.upper())