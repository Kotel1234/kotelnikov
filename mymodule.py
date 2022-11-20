def search_for_vowels(phrase: str) -> set:
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: str) -> set:
    return set(letters).intersection(set(phrase))


