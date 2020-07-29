def leapyear(year):
    """ Funkcia na vypocet prestupneho roku
    :param year: integer v tvare YYYY (2000)
    :return: True / False
    """
    if isinstance(year, str):
        return False
    if year:
        if ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0:
            return True
        return False