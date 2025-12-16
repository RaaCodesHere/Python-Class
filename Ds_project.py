student_details = []
while True:
    print("Student Management System")
    print("Your availabe options:")
    print("1. Add Student") # id, name, marks
    print("2. View Students")
    print("3. Passed Students")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1" :
        std_id = input("Enter student ID :")
        std_name = input("Enter your name :")
        std_marks = int(input("Enter student marks :"))
        student = {
            
            "id" : std_id, 
            "name" : std_name, 
            "marks" : std_marks
        }
        student_details.append(student)
        print("Student added successfully!")

    elif choice == "2":
        print("Student Details:")
        for i in student_details:
            print(i["id"], i["name"], i["marks"])
            
    elif choice == "3":
        print("Passed Students:")
        for i in student_details :
            if i["marks"] >= 40 :
                print(i["name"],"=",  i["marks"])
    
    elif choice == "4":
        print("System exit successfully!")   
        break