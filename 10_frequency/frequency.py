def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """
    sum = 0
    for num in lst:
        if num == search_term:
            sum = sum + 1
    print(sum)


frequency([1, 2, 3, 4, 1, 1], 1)
