# num1 = 5
# num2 = 10
# num3 = 15

num1 = int(input("Enter first number: "))  #Input function takes input from user and int converts it to integer
num2 = int(input("Enter second number: "))  #If there is no int function then it will take input as string
num3 = int(input("Enter third number: "))


conv1 = float(num1)  #Converting integer to float
conv2 = float(num2)    #Converting integer to float
conv3 = float(num3)  #Converting integer to float


print(type(conv1))  #Checking the type of variable after conversion5


sum_result = num1 + num2 + num3 #if there was no int function above then it would put the numbers together as strings
print("Sum result is", sum_result)


sub_result = num3 - num2 -num1 #Subtraction of three numbers
print("Subtraction result is", sub_result)