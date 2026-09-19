# Largest and Smallest Number in a List

numbers = [45, 12, 89, 7, 33, 91, 54]

if not numbers:
    print("List is empty.")
else:
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    print("List:", numbers)
    print("Largest:", largest)
    print("Smallest:", smallest)
