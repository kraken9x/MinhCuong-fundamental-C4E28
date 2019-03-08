letter_counts = {}

for letter in "Mississippi":
    letter = letter.lower()
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

from operator import itemgetter

print(sorted(letter_counts.items()))