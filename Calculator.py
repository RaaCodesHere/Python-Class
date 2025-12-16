print("---------Calculator---------")
print("Chose an option")
print("1. Calculator")
print("2. Odd Even Checker")
print("Exit")

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
    print("Exiting the program.")
    exit()
    
