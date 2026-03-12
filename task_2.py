from typing import Dict, List


def dictionary(translate: List[str]) -> Dict[str, str]:
    """
    Creates a dictionary from a list of word translate.

    Args:
        translate (List[str]): List of strings, each containing two words.

    Returns:
        Dict[str, str]: Dictionary with Russian-to-English mappings.
    """
    dict_en = {}
    for pair in translate:
        words_pair = pair.split()
        if len(words_pair) != 2:
            print(f"Invalid pair")
            continue
        word_ru, word_en = words_pair
        dict_en[word_ru] = word_en
    return dict_en


def phrase_translate(phrase: str, dictionary: Dict[str, str]) -> str:
    """
    Translates a phrase word-by-word using the dictionary.
    Words not found in the dictionary remain unchanged.

    Args:
        phrase (str): The phrase to translate.
        dictionary (Dict[str, str]): Dictionary with translations.

    Returns:
        str: Translated phrase.
    """
    text = phrase.split()
    translated_phrase = [dictionary.get(word, word) for word in text]
    return ' '.join(translated_phrase)


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter the number of word pairs: "))
            if number < 0:
                print("Enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input")

    pairs_translate = [input() for _ in range(number)]
    dictionary = dictionary(pairs_translate)

    phrase = input("Enter the phrase to translate: ")
    phrase_new = phrase_translate(phrase, dictionary)

    print("Translated phrase:", phrase_new)
