def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    week = {1: "sunday", 2: "monday", 3: "tuesday",
            4: "wednesday", 5: "thurs", 6: "fri", 7: "sat"}

    for(k, v) in week.items():
        if day_of_week > 7:
            return 'enter a valid day'
        if day_of_week == k:
            print(v)
