car = {

    

    "brand" : "toyota",

    "color" : ["black","white","red"],

    "model" : 2025,

    "price" : 2000000

    
}

car.update({"brand":"tesla", "model" : 2026})
car.update({"enginetype": "electric"})

print(car)

# Removing data from dictionary:

# using the pop() method to remove the specific item from dictionary

# car.pop("color")

#using popitem() method to remove the last inserted item from dictionary

# car.popitem()

# using del keyword to remove specific item from dictionary

# del car

# del car["model"]

# car.clear()

# for i in car:

#     print(i)

# for i in car:

#     print(car[i])

# for i in car.keys():

#     print(i)

# for i in car.values():

#     print(i)

# for i,j in car.items():

#     print(i,j)

# print(car)

# Nested Dictionary

 

# car1 = {  "brand" : "toyota",  "color" : "black",  "model" : 2025,  "price" : 2000000 }

# car2 = {  "brand" : "tesla",  "color" : "white",  "model" : 2026,  "price" : 3000000 }

# car3 = {  "brand" : "bmw",  "color" : "red",  "model" : 2027,  "price" : 4000000 }

# cars = {

#     "car1st": car1,

#     "car2nd": car2,

#     "car3rd": car3

# }

# print(cars)

 

cars = {

    "car1": {  "brand" : "toyota",  "color" : "black",  "model" : 2025,  "price" : 2000000 },

    "car2": {  "brand" : "tesla",  "color" : "white",  "model" : 2026,  "price" : 3000000 },

    "car3": {  "brand" : "bmw",  "color" : "red",  "model" : 2027,  "price" : 4000000 }

}

print(cars)


print(cars["car3"]["brand"])

print(cars["car3"]["color"])
