from collections import defaultdict
from string import ascii_lowercase

dictionary = open("/usr/share/dict/words", "r")
words_by_vowel = defaultdict(set)
vowels = ["a", "e", "i", "o", "u", "y"]

# Collect alphabetical words of length five containing no more than one vowel
for word in dictionary.readlines():
    word = word.strip().lower()
    if len(word) != 5:
        continue
    letters = set(word)
    if not letters.issubset(ascii_lowercase):
        continue
    vowels_in_word = set(vowels) & set(letters)
    if len(vowels_in_word) != 1:
        continue
    words_by_vowel[vowels_in_word.pop()].add(word)


def search(letters_remaining, solutions, candidate_words=set()):
    # Goal case:
    # - We have found six five-letter words without overlapping letters
    # - We have consumed all of the letters available
    if len(candidate_words) == 6 and len(letters_remaining) == 0:
        solution = ",".join(sorted(candidate_words))
        solutions.add(solution)
        return

    # Exit case:
    # - We selected six five-letter words but did not consume all letters
    if len(candidate_words) == 6:
        return

    # Recursive case: find words without overlapping letters and search those
    vowel = vowels[len(candidate_words)]
    for word in words_by_vowel[vowel]:
        letters = set(word)
        if not letters.issubset(letters_remaining):
            continue
        reduced_letters = letters_remaining.copy() - letters
        search(reduced_letters, solutions, candidate_words | {word})


solutions = set()
search(set(ascii_lowercase), solutions)

# dictionary: wamerican version 2019.10.06-1
# {'fitch,japan,kudzu,mysql,oxbow,verge'}
print(solutions)
