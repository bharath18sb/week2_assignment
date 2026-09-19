# Simple Pattern Using Nested Loops

rows = 5

print("Pattern:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print() # New line after each row
