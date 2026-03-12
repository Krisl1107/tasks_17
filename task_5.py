from typing import Dict, List, Optional, Set


def descendants(name: str, tree: Dict[str, List[str]], visited: Optional[Set[str]] = None) -> int:
    """
    Recursively counts the number of descendants (children, grandchildren, etc.) for a given person.

    Args:
        name (str): The name of the person for whom to count descendants.
        tree (Dict[str, List[str]]]): The family tree represented as a dictionary mapping parent to list of children.
        visited (Optional[Set[str]]): Set of already visited names to prevent cycles.

    Returns:
        int: Total number of descendants.
    """
    if visited is None:
        visited = set()

    total_descendants = 0
    if name in tree:
        for child in tree[name]:
            if child not in visited:
                visited.add(child)
                total_descendants += 1 + descendants(child, tree, visited)
    return total_descendants


def check_input(prompt: str) -> int:
    """
    Prompts the user to input a positive integer with validation.

    Args:
        prompt (str): The input prompt message.

    Returns:
        int: The validated positive integer.

    Raises:
        ValueError: If the input is not a valid positive integer.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    """
    Main function to build the tree and calculate descendants for a given person.
    """
    count = check_input("Enter the number of parent-child: ")

    tree = {}

    for _ in range(count):
        while True:
            entry = input("Enter parent and child: ").strip()
            parts = entry.split()
            if len(parts) != 2:
                print("Input error.")
                continue
            parent, child = parts
            break
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]

    find_name = input("Enter the name to count descendants for: ").strip()

    result = descendants(find_name, tree)
    print(f"Number of descendants: {result}")


if __name__ == "__main__":
    main()
