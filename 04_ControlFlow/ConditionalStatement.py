# #conditional statement
# #if statement    if
# #else statement  else
# #else if statement    elif



# # age = int(input("Please enter your age: "))

# # if age >= 18:
# #     print("You can vote.")
# # else:
# #     print("You cannot vote.")


# # num = int(input("Enter a number: "))

# # if num % 2 == 0:
# #     print(f"{num} is an even number.")
# # else:
# #     print("Its odd number.")
    
    

# #nested if-else


# # number = -21
# # if number >= 0:
    
# #     if number % 2 == 0:
# #         print("Postive even number")
# #     else:
# #         print("Positive odd number")
        
# # else:
# #     print("Negative number")
    

# marks = int(input("Enter your marks: "))
# if marks >= 80:
#     print("A+ grade")
# elif marks >= 70:
#     print("A grade")
# elif marks >= 60:
#     print("B grade")
# else:
#     print("Fail")
    
    
# # Lo    gical operators -> and, or, not
# percentage = 50
# if percentage >= 90 and percentage <= 100:  #and operator -> and operator ko dubai patti side ko conditions satisfy hunu parxa
#     print("A+ grade")   
# elif percentage  >= 80 and percentage < 90:
#     print("A grade")   
# elif percentage >= 70 and percentage < 80:
#     print("B+ grade")   
# elif percentage >= 60 and percentage < 70:
#     print("B grade")
# else:
#     print("Fail")
# #  or -> Or operator kunai auta conditions satisfy bhayo bhane hunxa
# age = int(input("Enter your age:"))
# if age > 18 or age == 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")
    
    
num = int(input("Enter a number: "))

if num == 0:
    print("Number is zero.")

elif+ num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")
else:
    print(f"{num} is a negative number.")