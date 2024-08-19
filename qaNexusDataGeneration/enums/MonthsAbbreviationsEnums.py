from enum import Enum

class MonthsAbbreviationsEnums(Enum):
    """
    Enum representing the abbreviations of the twelve months of the year.
    Each enum constant corresponds to a month abbreviation commonly used in date formatting.
    """

    # Month abbreviations corresponding to the enum constants
    JAN = "Jan"
    FEB = "Feb"
    MAR = "Mar"
    APR = "Apr"
    MAY = "May"
    JUN = "Jun"
    JUL = "Jul"
    AUG = "Aug"
    SEP = "Sep"
    OCT = "Oct"
    NOV = "Nov"
    DEC = "Dec"

    def __init__(self, abbreviation):
        """
        Constructs an instance of MonthsAbbreviationsEnums with the specified abbreviation.

        :param abbreviation: The abbreviation of the month
        """
        self._abbreviation = abbreviation

    @property
    def abbreviation(self):
        """
        Returns the abbreviation of the month.

        :return: The abbreviation of the month
        """
        return self._abbreviation
