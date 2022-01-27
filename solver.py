from string import ascii_lowercase

dictionary = open("/usr/share/dict/words", "r")
words = set()
vowels = ["a", "e", "i", "o", "u", "y"]

# Collect alphabetical words of length five containing no more than one vowel
for word in dictionary.readlines():
    word = word.strip().lower()
    if len(word) != 5:
        continue
    if any(letter not in ascii_lowercase for letter in word):
        continue
    if len(set(vowels) & set(word)) > 1:
        continue
    words.add(word)


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
    for word in words:
        if vowel not in word:
            continue
        if any(letter not in letters_remaining for letter in word):
            continue
        reduced_letters = letters_remaining.copy()
        for letter in word:
            reduced_letters.discard(letter)
        search(reduced_letters, solutions, candidate_words | {word})


solutions = set()
search(set(ascii_lowercase), solutions)
print(solutions)
