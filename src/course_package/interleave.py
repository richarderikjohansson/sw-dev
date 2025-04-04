def reverse_list(list_to_reverse: list) -> list:
    """Reverse a list

    Args:
        list_to_reverse: List to reverse

    Returns:
        Reversed list
    """
    reversed_list = list_to_reverse[::-1]
    return reversed_list


def interleave_two_lists(list1: list, list2: list) -> list:
    """Interleave two lists

    Args:
        list1: List to reverse
        list2: Other list

    Returns:
        List with interleaved from the two lists
    """

    reversed_list = reverse_list(list1)
    new_list = [str]

    for pair in zip(reversed_list, list2):
        new_list.extend(pair)

    return new_list
