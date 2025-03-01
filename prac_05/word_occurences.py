# Get user input
text = input("Text: ")

# Split the text into words
words = text.split()

# Dictionary to store word counts
word_counts = {}

# Count occurrences of each word
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sort words alphabetically and print results
for word in sorted(word_counts):
    print(f"{word} : {word_counts[word]}")
