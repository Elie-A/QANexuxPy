from enum import Enum

class SupportedDateFormatsEnums(Enum):
    """
    Enum representing the supported date formats.
    Each enum constant corresponds to a specific date format pattern used for formatting and parsing dates.
    """

    # Date format patterns corresponding to the enum constants
    YYYY_MM_DD = "yyyy-MM-dd"
    YYYY_MM_DD_SLASH = "yyyy/MM/dd"
    YYYY_MMM_DD = "yyyy-MMM-dd"
    YYYY_MMM_DD_SLASH = "yyyy/MMM/dd"
    DD_MM_YYYY = "dd-MM-yyyy"
    DD_MMM_YYYY = "dd-MMM-yyyy"
    DD_MMM_YYYY_SLASH = "dd/MMM/yyyy"

    def __init__(self, date_format):
        """
        Constructs an instance of SupportedDateFormats with the specified date format pattern.

        :param date_format: The date format pattern
        """
        self._date_format = date_format

    @property
    def date_format(self):
        """
        Returns the date format pattern associated with this enum constant.

        :return: The date format pattern
        """
        return self._date_format
