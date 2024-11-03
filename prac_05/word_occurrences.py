"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

text = input("Text: ")

word_counts = {}
words = text.split()
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

longest_word = max(len(word) for word in word_counts)

for word in sorted(word_counts):
    print(f"{word:{longest_word}} : {word_counts[word]}")
