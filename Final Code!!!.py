import time

subjects = ["Math", "Science", "English", "History", "Art"]
students = {}

def average(grades):
    return sum(grades.values()) / len(grades)

def report(student_data, grade):
    print(f"\n--- Report for {student_data['name']} (Class {grade}) ---")
    for subject, grade in student_data['grades'].items():
        print(f"{subject}: {grade}")
    print(f"Average: {average(student_data['grades']):.2f}")

    if average(student_data['grades']) >= 90:
        print("Remarks: Excellent!")
    elif average(student_data['grades']) >= 75:
        print("Remarks: Good job!")
    elif average(student_data['grades']) >= 60:
        print("Remarks: Satisfactory.")
    else:
        print("Remarks: Needs improvement.")

def main():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            print("Welcome to DIGIGRADE......\n")
            time.sleep(1)
            print(f"{name}, we welcome you to this online platform...")
            time.sleep(1)

            while True:
                print("\nChoose an option:")
                print("1. Add a student's grades")
                print("2. View student reports")
                print("3. Exit")

                choice = input("Enter your choice (1-3): ")

                if choice == '1':
                    grade = input("Enter the grade you want to choose (1-12): ")
                    if grade.isdigit() and 1 <= int(grade) <= 12:
                        student_name = input("Enter the student name: ")
                        if student_name.isalpha():
                            student_id = input("Enter the student ID: ")
                            if student_id.isalnum():
                                student_data = {
                                    "name": student_name,
                                    "id": student_id,
                                    "grades": {}
                                }

                                for subject in subjects:
                                    while True:
                                        subject_grade = input(f"Enter the grade for {subject}: ")
                                        if subject_grade.isdigit() and 0 <= int(subject_grade) <= 100:
                                            student_data["grades"][subject] = int(subject_grade)
                                            break
                                        else:
                                            print("Invalid grade.")

                                if grade not in students:
                                    students[grade] = []
                                students[grade].append(student_data)

                                report(student_data, grade)

                                break
                            else:
                                print("Invalid student name.")
                        else:
                            print("Invalid grade.")
                    else:
                        print("Invalid grade.")
                elif choice == '2':
                    # Implement functionality to view student reports
                    print("View student reports functionality will be added in the future.")
                elif choice == '3':
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Invalid name.")

        # Ask if they want to enter another student (case-insensitive)
        another = input("\nWould you like to enter another student? (yes/no): ").lower()
        if another not in ('yes', 'no'):
            print("Please enter 'yes' or 'no'.")
        elif another != 'yes':
            break

if __name__ == "__main__":
    main()
