# Sorting a list using sort() and lambda key

# List of tuples (name, age)
students = [("Alice", 22), ("Bob", 19), ("Charlie", 25), ("David", 21)]

print("Original list:", students)

# Sort based on age (the second element in the tuple)
students.sort(key=lambda student: student[1])

print("Sorted by age:", students)
