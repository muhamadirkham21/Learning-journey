# python 3.11.5


def calculate_populations(day):

    """
    Calculate the population growth over a given number of days.

    Parameters:
    - day (int): The number of days to calculate the population growth for.

    Returns:
    - int: The population after the given number of days.

    The function calculates the population growth over the specified number of days. 
    The population triples every day, except for every third day when the population 
    is halved. The initial population is assumed to be 1.

    Examples:
    >>> calculate_populations(1)
    1
    >>> calculate_populations(2)
    3
    """

    populations = 1
    if day == 1: 
        return populations
    else:
        for i in range(2, day+1):
            if i % 3 == 0:
                populations //= 2
            else:
                populations *= 3
    
    return populations

print(calculate_populations(50))
