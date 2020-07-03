def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]
# The two colons without specified parameter will
# include all the characters from the original string, a stride of 1 will include every character without skipping, and
# negating that stride will reverse the order of the characters.
