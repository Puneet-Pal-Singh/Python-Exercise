# Print a pattern
a = int(input("Enter number of rows, to print a Pattern:"))
b = bool(int(input("Please add 0 for False Pattern or 1 for True Pattern:")))

def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1
star(a, b)


#Output

This program prints Pattern
Enter number of rows, to print a Pattern:5
Please add 0 for False Pattern or 1 for True Pattern:1
*
**
***
****
*****

