# Dictionary Word Frequency Counter

text = input("Enter a sentence: ")
words = text.lower().split()

frequency = {}

for word in words:
    # Remove basic punctuation if needed
    word = word.strip(".,!?")
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")
