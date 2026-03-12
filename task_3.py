from typing import Dict, List


def build_antonym_dictionaries(antonyms: List[str]) -> (Dict[str, str], Dict[str, str]):
    """
    Builds two dictionaries for antonym lookup:
    - original: maps each word to its antonym
    - reverse: maps each antonym back to the original word

    Args:
        antonyms: A list of strings, each containing two words separated by a space.
                  Each pair is bidirectional.

    Returns:
        A tuple of two dictionaries: (original_dict, reverse_dict)
    """
    original_dict = {}
    reverse_dict = {}
    for pair in antonyms:
        words_pair = pair.split()
        if len(words_pair) != 2:
            print(f"Invalid pair.")
            continue
        word, word_an = words_pair
        word_lower = word.lower()
        word_an_lower = word_an.lower()

        original_dict[word_lower] = word_an_lower
        reverse_dict[word_an_lower] = word_lower
    return original_dict, reverse_dict


def find_antonym(word: str, original_dict: Dict[str, str], reverse_dict: Dict[str, str]) -> str:
    """
    Finds the antonym of a word, checking both dictionaries case-insensitively.
    If the word is found as a key, returns its antonym.
    If the word is found as a value, returns the corresponding key.
    If not found, returns the original word.

    Args:
        word: The word to find the antonym for.
        original_dict: Dictionary from words to antonyms.
        reverse_dict: Dictionary from antonyms to original words.

    Returns:
        The antonym or original word if not found.
    """
    word_lower = word.lower()
    if word_lower in original_dict:
        return original_dict[word_lower]
    elif word_lower in reverse_dict:
        return reverse_dict[word_lower]
    else:
        return word


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter the number of word pairs: "))
            if number < 0:
                print("Enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter an integer.")

    pairs_antonym = [input() for _ in range(number)]
    original_dict, reverse_dict = build_antonym_dictionaries(pairs_antonym)

    word = input("Enter the word for finding the antonym: ")
    antonym = find_antonym(word, original_dict, reverse_dict)

    print("Antonym:", antonym)
