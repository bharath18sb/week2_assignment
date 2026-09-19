import csv
import os

FILE_NAME = "students.csv"

def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader, None) # Skip header
            for row in reader:
                students.append(row)
    return students

def save_students(students):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Roll Number"])
        writer.writerows(students)

def add_student(students):
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    roll = input("Enter roll number: ")
    students.append([name, marks, roll])
    save_students(students)
    print("Student added!")

def search_student(students):
    roll = input("Enter roll number to search: ")
    for s in students:
        if s[2] == roll:
            print(f"Found: Name: {s[0]}, Marks: {s[1]}, Roll: {s[2]}")
            return
    print("Student not found.")

def delete_student(students):
    roll = input("Enter roll number to delete: ")
    for i, s in enumerate(students):
        if s[2] == roll:
            students.pop(i)
            save_students(students)
            print("Student deleted!")
            return
    print("Student not found.")

def display_students(students):
    if not students:
        print("No records.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s[0]}, Marks: {s[1]}, Roll: {s[2]}")

def main():
    students = load_students()
    while True:
        print("\n--- Student Management ---")
        print("1. Add\n2. Search\n3. Delete\n4. Display\n5. Exit")
        choice = input("Choice: ")

        if choice == '1': add_student(students)
        elif choice == '2': search_student(students)
        elif choice == '3': delete_student(students)
        elif choice == '4': display_students(students)
        elif choice == '5': break
        else: print("Invalid!")

main()
