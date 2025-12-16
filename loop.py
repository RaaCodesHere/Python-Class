# ========== FOR LOOP ==========
print("Simple For Loop:")
for i in range(5):  # range(5) gives 0,1,2,3,4
    print(i)  # prints numbers from 0 to 4

print("\n")


print("For Loop with range(start, end):")
for i in range(1, 6):  # starts from 1, goes up to 5 (6 is not included)
    print(f"Number: {i}")

print("\n")


# ========== NESTED FOR LOOP ==========
print("Nested For Loop - Star Pattern:")
for i in range(1, 6):  # outer loop runs 5 times
    for j in range(i):  # inner loop runs i times
        print("*", end="")  # end="" prevents moving to new line
    print()  # moves to next line after inner loop finishes

# What happens:
# i=1: inner loop runs 1 time -> *
# i=2: inner loop runs 2 times -> **
# i=3: inner loop runs 3 times -> ***
# i=4: inner loop runs 4 times -> ****
# i=5: inner loop runs 5 times -> *****

print("\n")


# ========== WHILE LOOP ==========
# While loop keeps running as long as the condition is True
print("Simple While Loop:")
count = 1
while count <= 5:  # runs while count is less than or equal to 5
    print(f"Count is: {count}")
    count += 1  # same as count = count + 1, increases count by 1

print("\n")


# ========== NESTED WHILE LOOP ==========
print("Nested While Loop - Multiplication Table:")
i = 1
while i <= 3:  # outer loop runs 3 times
    j = 1
    while j <= 3:  # inner loop runs 3 times for each outer loop
        print(f"{i} x {j} = {i*j}", end="  ")
        j += 1
    print()  # new line after inner loop completes
    i += 1

print("\n")
