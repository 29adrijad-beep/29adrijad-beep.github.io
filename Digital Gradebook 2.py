import time

subjects = ['Math', 'Science', 'Social Science', 'English', 'Hindi']

while True:
    name = input(f"Enter your name:\n")
    if name.replace(" ", "").isalpha():  # Allows spaces in the name
        print(f"Welcome to DIGIGRADE......\n")
        time.sleep(1)
        print(f"{name}, we welcome you to this online platform where you can access student grades by their name, student ID, and have a space to add your feedback based on the student's grade in each subject.\n")
        time.sleep(1)

        while True:
            grade = input(f"Enter the grade you want to choose:\nThe format of the grade is only accepted as numbers and not as Grade 9 or grade 9 or Grade9 or grade9\n")

            if grade.isdigit():
                class_grade = int(grade)
                if 1 <= class_grade <= 12:
                    print(f"{class_grade} is accepted")
                    student_name = input(f"Enter the student name:\n")
                    if student_name.replace(" ", "").isalpha():  # Allows spaces in the student name
                        student_id = input(f"Enter the student ID:\n")
                        total = 0  # Reset total for each student
                        for i in subjects:
                            while True:
                                sub = input(f"Enter the grade for {i}: ")
                                if sub.isdigit():
                                    total += int(sub)
                                    break
                                else:
                                    print("Please enter a valid number for the grade.")
                        print(f"Average: {(total) / (len(subjects))}")
                        break  # Exit the inner loop after processing one student
                    else:
                        print("Kindly enter a valid name once again.")
                else:
                    print("Please enter a valid grade (1-12).")
            else:
                print("Sorry, wrong grade. Please enter a number.")
        break  # Exit the outer loop after processing one student

    else:
        print("Please enter a valid name.\nThe format of the name should either be in uppercase or lowercase but not in integer.\nExample: Audrey is accepted, audrey is accepted, but 1213 is not accepted.")
