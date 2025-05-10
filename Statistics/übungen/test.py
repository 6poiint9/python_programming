#result = 0

#print("Please enter the first number")

n1 = int(input("Please enter the first number: "))

choice = input("Enter the operator + - / * : ")  

n2 = int(input("Please enter the second number: "))


if choice == '+':
    print("you chose addition!\n")
    result = n1 + n2
    print(result)
elif choice == '-':
    print("subtraction!\n")
    result = n1 - n2
    print(result)
elif choice == '/':
    print("division")
    result = n1 / n2
    print(float(result))
elif choice == '*':
    print("multiplication")
    result = n1 * n2
    print(float(result))
else:
    print("invalid operator")



