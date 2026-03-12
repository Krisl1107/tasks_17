from typing import Dict, List


def dictionary_forms(things: List[str]) -> Dict[str, List[str]]:
    """
    Converts a list of strings describing words and their synonyms into a dictionary.

    Args:
        things: A list of strings, each string contains a form and its synonyms separated by spaces.
                The first word in each string is considered the "form" of the item,
                and the rest are its synonyms.

    Returns:
        A dictionary where the keys are the forms in lowercase,
        and the values are lists of synonyms in lowercase.
    """
    forms = {}
    for form in things:
        parts = form.split()
        if len(parts) < 2:
            print(f"Invalid pair")
            continue
        form_lower = parts[0].lower()
        synonyms_lower = [word.lower() for word in parts[1:]]
        forms[form_lower] = synonyms_lower
    return forms


def find_item_form(item: str, dictionary: Dict[str, List[str]]) -> str:
    """
    Finds the form of an item in the dictionary, case-insensitively.

    Args:
        item: The word to find the form for.
        dictionary: A dictionary where the keys are forms and the values are lists of synonyms.

    Returns:
        The form (key) associated with the item if found, otherwise None.
    """
    item_low = item.lower()
    for form, things in dictionary.items():
        if item_low in things:
            return form
    return None


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter the number of word forms: "))
            if number < 0:
                print("Enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input")

    words = [input() for _ in range(number)]
    dictionary_items = dictionary_forms(words)

    word = input("Enter the word to find form: ").strip()
    find_form = find_item_form(word, dictionary_items)

    if find_form:
        print("Form of item:", find_form)
    else:
        print("Word not find:", word)
