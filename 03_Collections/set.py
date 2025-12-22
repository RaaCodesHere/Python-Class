name = {"ram","shyam","hari"}


#Adding single data to set
# name.add("Bikash")

#Adding multiple data to set
# name.update({"Ritesh","Sangeet","Sita"})
# name.update(["Ritesh","Sangeet","Sita"])
# name.update(("Ritesh","Sangeet","Sita"))

# Removing data from set
# name.remove("hari")
# name.discard("ram")
# name.pop()
# name.clear()
# del name


print(name)


# Join operations in set using Union
# name = {"ram","shyam","hari"}
# age = {25,34,49,45, "ram"}
# salary = {20000,50000,70000, 25}
# new_set = name.union(age,salary)
# new_set = name | age | salary

# Join operation using Intersection
# name = {"ram","shyam","hari", 34}
# age = {25,34,49,45, "ram"}
# new_set = name.intersection(age)
# new_set = name & age
# print(new_set)


name = {"ram","shyam","hari", 34}
age = {25,34,49,45, "ram"}
# new_set = age.difference(name)
# new_set = name - age
# print(new_set)
result = age.isdisjoint(age)
print(result)