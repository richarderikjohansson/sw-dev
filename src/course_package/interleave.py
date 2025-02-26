from course_package.reverse import reverse_list


def interleave_two_lists(list1, list2):
    """
    Function that takes two inputs as lists, reverses the first list and
    then interleaves every other argument from the two lists and combines
    them into a new list

    Args:
    list1 (list): list that should be reversed
    list2 (list): the second list that not will be reversed

    Returns:
    new_list (list): Interleaved list from list1 and list2
    """
    assert isinstance(list2, list), f"{type(list2)} is not of type 'list'"

    list1 = reverse_list(list1)
    new_list = list()

    for pair in zip(list1, list2):
        new_list.extend(pair)

    return new_list
