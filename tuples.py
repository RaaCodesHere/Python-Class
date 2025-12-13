# name = ("ram", "shyam", "hari", "ram")
# name.remove("mohan") #cannot change the value of tuple
# name.append("Sita")
# new_name = list(name)
# new_name.append("Sita")
# new_name2 = tuple(new_name)
# print(new_name2)

# new_name = list(name)
# new_name.remove("ram")
# new_name2 = tuple(new_name)
# print(new_name2)


# surname = ("gupta", "sharma", "verma", "gupta")
# name = name + surname
# print(name)

# name = ("ram", "shyam", "hari", "ram")
# surname = ("gupta","adhikari")
# del surname
# print(name)
# # print(surname)

# email = ("aaditya@gmail.com","anish@gmail.com","ashim@gmail.com") 
# (aaditya,anish,ashim) = email  #unpacking values from tuples
# print(aaditya)
# print(anish)
# print(ashim)

email = ("aaditya@gmail.com","anish@gmail.com","ashim@gmail.com", "meghan@gmail.com","rojit@gmail.com") 
(aaditya,anish,*ashim) = email  #unpacking values from tuples(using astrick *)
print(aaditya)
print(anish)
print(ashim)


"""
Lists vs Tuples:
List: 
ordered, changeable, allows duplicate members., syntax [], methods are available, accessing the value is slow, data are not secured as compared to tuples
Tuple:
ordered, unchangeable, allows duplicate members. syntax (), methods are not available, accessing the value is fast, data are secured here than list
Set:
unordered, unchangeable, doesn't allow duplicate members, syntax {}, methods are available only for adding or removing data, 
Dictionary: 
ordered/unordered , changeable, doesn't allow duplicate members,  syntax = {}, methods are available 
"""