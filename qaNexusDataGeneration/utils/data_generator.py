import re
import random
from datetime import datetime
from qaNexusDataGeneration.constantVariables.DataGeneratorConstants import Constants
from qaNexusDataGeneration.enums import CountryCodePhoneNumberPatternEnums, MonthsAbbreviationsEnums, SupportedDateFormatsEnums

class DataGenerator:
    def __init__(self):
        # Initialization code
        pass
    
    def generate_string(self, length=Constants.DEFAULT_STRING_LENGTH):
        """
        Generates a random string with the default length specified in Constants.DEFAULT_STRING_LENGTH.

        :param length: The length of the generated string. Defaults to Constants.DEFAULT_STRING_LENGTH.
        :return: A randomly generated string.
        """
        return "".join(random.choices(Constants.ALPHA_NUM, k=length))

    def generate_email(
        self,
        domain=Constants.DEFAULT_DOMAIN,
        username_length=Constants.DEFAULT_EMAIL_USERNAME_LENGTH,
    ):
        """
        Generates a random email address with the specified username length and domain.

        :param domain: The domain to use for the email address. Defaults to DEFAULT_DOMAIN.
        :param username_length: The length of the username part of the email address. Defaults to DEFAULT_EMAIL_USERNAME_LENGTH.
        :return: A randomly generated email address.
        """
        username = self.generate_string(username_length)
        return username + domain

    def generate_phone_number(self, country_code="US"):
        """
        Generates a random phone number based on the specified country code.

        :param country_code: The country code to determine the phone number format. Defaults to "US".
        :return: A randomly generated phone number in the format corresponding to the given country code.
        :raises ValueError: If the country code is invalid.
        """
        try:
            country_enum = CountryCodePhoneNumberPatternEnums[country_code]
        except KeyError:
            raise ValueError(f"Invalid country code: {country_code}")

        phone_regex = country_enum.value
        pattern = re.compile(phone_regex)
        
        phone_number = self.generate_random_phone_number(phone_regex)
        
        while not pattern.match(phone_number):
            phone_number = self.generate_random_phone_number(phone_regex)
            
        return phone_number

    def generate_random_phone_number(self, pattern):
        """
        Generates a random phone number based on a pattern.

        :param pattern: The pattern to use for generating the phone number.
        :return: A randomly generated phone number.
        """
        phone_number = []
        is_escaped = False
        i = 0
        
        while i < len(pattern):
            ch = pattern[i]
            
            if is_escaped:
                if ch == 'd':
                    # Handle \d{n} pattern
                    if i + 1 < len(pattern) and pattern[i + 1] == '{':
                        closing_brace_index = pattern.find('}', i + 2)
                        if closing_brace_index != -1:
                            repeat_count_str = pattern[i + 2:closing_brace_index]
                            repeat_count = int(repeat_count_str)
                            phone_number.extend([str(random.randint(0, 9))] * repeat_count)
                            i = closing_brace_index
                        else:
                            phone_number.append('d')
                    else:
                        phone_number.append(str(random.randint(0, 9)))
                else:
                    phone_number.append(ch)
                is_escaped = False
            else:
                if ch == '\\':
                    is_escaped = True
                else:
                    phone_number.append(ch)
                    
            i += 1

        return ''.join(phone_number)

    def get_max_days(self, month, year):
        """
        Returns the maximum number of days in a given month and year, considering leap years.

        :param month: The month (1 for January, 2 for February, etc.)
        :param year: The year
        :return: The maximum number of days in the given month
        """
        if month == 2:  # February
            return 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28
        elif month in {4, 6, 9, 11}:  # April, June, September, November
            return 30
        else:  # All other months
            return 31

    def generate_date(self, format=None):
        """
        Generates a random date based on the specified format. If no format is provided, it defaults to "yyyy-MM-dd".

        :param format: An instance of SupportedDateFormatsEnums specifying the date format to use
        :return: A randomly generated date in the specified format
        """
        year = -1
        month = ""
        day = ""

        secure_random = random.Random()

        if format is None:
            current_date = datetime.now()
            year = current_date.year
            month = f"{current_date.month:02d}"
            day = f"{current_date.day:02d}"
            return f"{year}-{month}-{day}"

        format_string = format.date_format

        if "yyyy" in format_string:
            year = secure_random.randint(1900, 2023)  # Random year between 1900 and 2023

        if "MM" in format_string:
            month_num = secure_random.randint(1, 12)  # Random month between 1 and 12
            month = f"{month_num:02d}"
        if "MMM" in format_string:
            month_enum = secure_random.choice(list(MonthsAbbreviationsEnums))
            month = month_enum.abbreviation

        if "dd" in format_string:
            max_days = self.get_max_days(int(month), year) if year != -1 and month.isdigit() else 31
            day = f"{secure_random.randint(1, max_days):02d}"  # Random day

        return (format_string
                .replace("yyyy", str(year))
                .replace("yy", str(year)[2:])
                .replace("MM", month)
                .replace("MMM", month)
                .replace("dd", day))
