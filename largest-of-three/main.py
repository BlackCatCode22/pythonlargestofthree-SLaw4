num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
total = num1 + num2 + num3
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
print("The largest of the three numbers is:", largest)
print("The total of the three numbers is:", total)
