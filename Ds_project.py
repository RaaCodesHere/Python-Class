# ============================================================================
# STUDENT MANAGEMENT SYSTEM
# ============================================================================
# This program manages student records with multiple subjects' marks
# Features: Add students, view records, filter by pass/fail, calculate averages
# ============================================================================

# Data structures initialization
student_details = []  # List to store all student dictionaries
student_id_lists = set()  # Set to store unique student IDs for O(1) lookup
marks_tuples = ("Maths", "Science", "English", "Nepali", "Social_Studies")  # Fixed subject names

while True:
    # Display menu
    print("Student Management System")
    print("Your availabe options:")
    print("1. Add Student\n2. View Students\n3. Passed Students\n4. Failed Students\n5. Class Average \n6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    # ====== CHOICE 1: ADD STUDENT ======
    if choice == 1 :
        std_id = input("Enter student ID :")
        
        # Check for duplicate ID - prevents data integrity issues
        if std_id in student_id_lists:
            print("Student ID already exists! Please use a different ID.")
            continue
        else:
            # Add ID to set and collect student information
            student_id_lists.add(std_id)
            std_name = input("Enter your name :")
            
            # Collect marks for each subject in order
            marks = []
            for sub in marks_tuples:
                mark = int(input(f"Enter marks for {sub} : "))
                marks.append(mark)
            
            # Create student dictionary with all details
            student = {
                "id" : std_id, 
                "name" : std_name, 
                "marks" : marks  # List of 5 marks [Maths, Science, English, Nepali, Social_Studies]
            }
            student_details.append(student)
            print("Student added successfully!")
    
    # ====== CHOICE 2: VIEW ALL STUDENTS ======
    elif choice == 2:
        print("Student Details:")
        print("ID\t Name\t Marks")
        # Display each student's ID, name, and all 5 subject marks
        for i in student_details:
            print(i["id"], "\t", i["name"], "\t", i["marks"])
            
    # ====== CHOICE 3: DISPLAY PASSED STUDENTS ======
    elif choice == 3:
        print("Passed Students:")
        print("Name")
        # A student PASSES only if they score >= 40 in ALL 5 subjects
        for i in student_details :
            count = 0  # Counter to track subjects with marks >= 40
            for mark in i["marks"]:
                if mark >= 40:
                    count = count + 1
            # Only print if passed in all 5 subjects
            if count == 5:
                print(i["name"])
            
    # ====== CHOICE 4: DISPLAY FAILED STUDENTS ======
    elif choice == 4:
        print("Failed Students:")
        print("Name")
        # A student FAILS if they score < 40 in at least one subject
        for i in student_details :
            count = 0  # Counter to track subjects with marks >= 40
            for mark in i["marks"]:
                if mark >= 40:
                    count = count + 1
            # Print if failed in any subject (count != 5)
            if count != 5:
                print(i["name"])

    # ====== CHOICE 5: CALCULATE CLASS AVERAGE ======
    elif choice == 5:
        if not student_details :
            print("No data available")
        else:
            # Calculate total marks across all students and all subjects
            total_marks = 0
            total_subject = 0
            for i in student_details:
                # sum(i["marks"]) adds all 5 marks for each student
                total_marks = total_marks + sum(i["marks"])
                # Each student has 5 subjects
                total_subject = total_subject + len(i["marks"])
            # Average = Total marks / Total number of marks (students * 5)
            average = total_marks / total_subject
            print(f"Average is {average}")
            
    # ====== CHOICE 6: EXIT SYSTEM ======
    elif choice == 6:
        print("System exit successfully!")   
        break