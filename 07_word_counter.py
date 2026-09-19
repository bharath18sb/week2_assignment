# Word Counter from Text File

filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        chars = len(content)

        print(f"File: {filename}")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {chars}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
