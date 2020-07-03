def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    out = ""

    for letter in phrase:
        if letter.lower == to_swap:
            letter = letter.upper()
        out += letter
    return out

    # for letter in array:
    #     if letter == to_swap.upper():
    #         letter.lower()
    # print(phrase)


flip_case('hello', 'E')
