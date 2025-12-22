print("\n")
print("\n")

from datetime import datetime


cur_hour = datetime.now().hour
if cur_hour < 12:
    greet = "Good Morning"
elif cur_hour < 18:
    greet = "Good Afternoon"
else:
    greet = "Good Evening"
print(greet + " User!")

while True:
    print("---------Calculator---------")
    print("Chose an option")
    print("1. Calculator")
    print("2. Odd Even Checker")
    print("3. Factor Finder")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        operation = input("Enter operation (1/2/3/4): ")
        
        if operation == '1':
            sum = num1 + num2
            print(f"The sum of {num1} and {num2} is {sum}")
        if operation == '2':
            difference = num1 - num2
            print(f"The difference between {num1} and {num2} is {difference}")
        if operation == '3':
            product = num1 * num2
            print(f"The product of {num1} and {num2} is {product}")
        if operation == '4':
            if num2 != 0:
                quotient = num1 / num2
                print(f"The quotient of {num1} divided by {num2} is {quotient}")
            else:
                print("Error: Division by zero is not allowed.")

    if choice == '2':
        number = int(input("Enter a number: ")) 
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    if choice == '3':
        n = int(input("Enter a number: "))
        # Lambda function to check if number is non-negative
        is_non_negative = lambda x: x >= 0
        if not is_non_negative(n):
            print("Please enter a Positive Number.")
        else:
            # Recursive function to calculate factorial
            def fact(x):
                if x <= 1:
                    return 1
                return x * fact(x - 1)
            print(f"Factorial of {n} is {fact(n)}")
    
    if choice == '4':
        print("Thank You! Exiting the program.")
        break

