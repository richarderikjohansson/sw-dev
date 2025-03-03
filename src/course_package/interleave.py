from course_package.reverse import reverse_list


def interleave_two_lists(list1: list, list2: list) -> list:
    """
    Function that takes two inputs as lists, reverses the first list and
    then interleaves every other element from the two lists and combines
    them into a new list

    Parameters
    ----------
    list1 : list that should be reversed
    list2 : the second list that not will be reversed

    Returns
    -------
    new_list : Interleaved list from list1 and list2
    """

    reversed_list = reverse_list(list1)
    new_list = []

    for pair in zip(reversed_list, list2):
        new_list.extend(pair)

    return new_list
