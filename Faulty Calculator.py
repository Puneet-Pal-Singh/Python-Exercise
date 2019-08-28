"""
Faulty-Calculator
This Program will execute wrong answers to some specific calculations.

For Example - 45*3 =555 ,56+9 =77, 56/6 =4
Design a calculator which will correctly solve all the problems except the following ones:
45*3 =555 ,56+9 =77, 56/6 =4
The program should take operators and two numbers as input from user and then return the result.
"""


  #answer
print("---Calculator---")
print("Menu:")
print(" 1.Addition:\n 2.Subtraction: \n 3.Multiply: \n 4.Divide:")
print("Enter your values to perform calculations:")
print("Variable 1:")
var1 = int(input())
print("Variable 2:")
var2 = int(input())
print("Enter your choice of calculation:")
choice = int(input())


if var1 == 45 or var1 == 3 and var2 == 3 or var2 == 45 and choice == 3:
     print("The answer is 555")

elif var1 == 56 or var1 == 9 and var2== 9 or var2 == 56 and choice == 1:
     print("The answer is 77")

elif var1 == 56 or var1 == 6 and var2 == 6 or var2 == 56 and choice == 4:
     print("The answer is 4")

elif choice == 1:
     print("Addition is:",var1 + var2)

elif choice == 2:
     print("Subtraction is:",var1 - var2)

elif choice == 3:
     print("Multiplication is:",var1* var2)

elif choice == 4:
     print("Division is:",var1 / var2)

else :
    print("Wrong choice")
