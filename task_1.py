from collections import Counter
from typing import List, Tuple


def main(input_string: str) -> List[Tuple[str, int]]:
    """
    Counts the frequency of each word in the input string and returns the list
    of words sorted by decreasing frequency.

    Args:
        input_string (str): The string containing words to analyze.

    Returns:
        List[Tuple[str, int]]: List of tuples where each tuple contains a word
        and its frequency, sorted by frequency in descending order.
    """

    words = input_string.split()
    count = Counter(words)

    sorted_words = sorted(count.items(), key=lambda word: word[1], reverse=True)

    return [word for word, _ in sorted_words]


if __name__ == "__main__":
    user_input = input("Enter string: ")
    sorted_words = main(user_input)

    for word in sorted_words:
        print(word)
