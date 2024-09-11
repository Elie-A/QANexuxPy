import re
import random
import uuid
import time
import math
import numpy as np
from typing import List
from datetime import datetime
from qaNexusDataGeneration.statictVariables.DataGeneratorConstants import Constants
from qaNexusDataGeneration.enums.SupportedDateFormatsEnums import (
    SupportedDateFormatsEnums,
)
from qaNexusDataGeneration.enums.CountryCodePhoneNumberPatternEnums import (
    CountryCodePhoneNumberPatternEnums,
)
from qaNexusDataGeneration.enums.MonthsAbbreviationsEnums import (
    MonthsAbbreviationsEnums,
)
from qaNexusDataGeneration.model.ComplexNumberModel import ComplexNumber


def generate_string(length=Constants.DEFAULT_STRING_LENGTH):
    """
    Generates a random string with the default length specified in Constants.DEFAULT_STRING_LENGTH.

    :param length: The length of the generated string. Defaults to Constants.DEFAULT_STRING_LENGTH.
    :return: A randomly generated string.
    """
    return "".join(random.choices(Constants.ALPHA_NUM, k=length))


def generate_email(
    domain=Constants.DEFAULT_DOMAIN,
    username_length=Constants.DEFAULT_EMAIL_USERNAME_LENGTH,
):
    """
    Generates a random email address with the specified username length and domain.

    :param domain: The domain to use for the email address. Defaults to DEFAULT_DOMAIN.
    :param username_length: The length of the username part of the email address. Defaults to DEFAULT_EMAIL_USERNAME_LENGTH.
    :return: A randomly generated email address.
    """
    username = generate_string(username_length)
    return username + domain


def generate_phone_number(country_code="US"):
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

    phone_number = generate_random_phone_number(phone_regex)

    while not pattern.match(phone_number):
        phone_number = generate_random_phone_number(phone_regex)

    return phone_number


def generate_random_phone_number(pattern):
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
            if ch == "d":
                # Handle \d{n} pattern
                if i + 1 < len(pattern) and pattern[i + 1] == "{":
                    closing_brace_index = pattern.find("}", i + 2)
                    if closing_brace_index != -1:
                        repeat_count_str = pattern[i + 2 : closing_brace_index]
                        repeat_count = int(repeat_count_str)
                        phone_number.extend([str(random.randint(0, 9))] * repeat_count)
                        i = closing_brace_index
                    else:
                        phone_number.append("d")
                else:
                    phone_number.append(str(random.randint(0, 9)))
            else:
                phone_number.append(ch)
            is_escaped = False
        else:
            if ch == "\\":
                is_escaped = True
            else:
                phone_number.append(ch)

        i += 1

    return "".join(phone_number)


def get_max_days(month, year):
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


def generate_date(format=Constants.DEFAULT_DATE_FORMAT):
    """
    Generates a random date based on the specified format. If no format is provided, it defaults to "yyyy-MM-dd".

    :param format: An instance of SupportedDateFormatsEnums specifying the date format to use
    :return: A randomly generated date in the specified format
    """
    year = -1
    month = ""
    day = ""

    secure_random = random.Random()

    # Get the current date and time
    now = datetime.now()

    # Extract the current year
    current_year = now.year

    # Handle case where format is a string rather than an Enum instance
    if isinstance(format, str):
        format_string = format
    else:
        format_string = format.date_format

    if "yyyy" in format_string or "YYYY" in format_string:
        year = secure_random.randint(
            1900, current_year
        )  # Random year between 1900 and current year

    if "MM" in format_string:
        month_num = secure_random.randint(1, 12)  # Random month between 1 and 12
        month = f"{month_num:02d}"
    if "MMM" in format_string:
        month_enum = secure_random.choice(list(MonthsAbbreviationsEnums))
        month = month_enum.abbreviation

    if "dd" in format_string:
        if year != -1 and month.isdigit():
            max_days = get_max_days(int(month), year)
        else:
            max_days = 31
        day = f"{secure_random.randint(1, max_days):02d}"  # Random day

    if "DD" in format_string:
        if year != -1 and month.isdigit():
            max_days = get_max_days(int(month), year)
        else:
            max_days = 31
        day = f"{secure_random.randint(1, max_days):02d}"  # Random day

    return (
        format_string.replace("YYYY", str(year))
        .replace("yyyy", str(year))
        .replace("MMM", month)
        .replace("MM", month)
        .replace("DD", day)
        .replace("dd", day)
    )


def generate_uuid(type=Constants.DEFAULT_UUID_TYPE):
    """
    Generate a UUID based on the specified type.

    This method generates a UUID (Universally Unique Identifier) of the specified version.
    The following UUID types are supported:

    - "v1": UUID based on the host ID and current time.
    - "v3": UUID based on the MD5 hash of a namespace and a name.
    - "v4": Randomly generated UUID.
    - "v5": UUID based on the SHA-1 hash of a namespace and a name.

    Parameters:
    type (str): The type of UUID to generate. Must be one of "v1", "v3", "v4", or "v5".
                Defaults to `Constants.DEFAULT_UUID_TYPE`.

    Returns:
    str: A string representation of the generated UUID.

    Raises:
    ValueError: If an unsupported UUID type is provided.

    Example:
    >>> generate_uuid("v1")
    'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    >>> generate_uuid("v4")
    '3d4e2fbb-7f5f-4d46-9250-27f85c44d5d6'

    >>> generate_uuid("v5")
    '6ba7b810-9dad-11d1-80b4-00c04fd430c8'

    Notes:
    - For UUID versions v3 and v5, the name parameter is hardcoded in this implementation.
    To customize, you might need to modify the method or provide additional parameters.
    """
    if type == "v1":
        return str(uuid.uuid1())
    elif type == "v3":
        return str(uuid.uuid3())
    elif type == "v4":
        return str(uuid.uuid4())
    elif type == "v5":
        return str(uuid.uuid5())
    else:
        return str(uuid.uuid4())


def generate_ssn():
    """
    Generates a random Social Security Number (SSN) in the format "XXX-XX-XXXX".

    Returns:
        str: A randomly generated SSN in the format "XXX-XX-XXXX".
    """
    return "{:03d}-{:02d}-{:04d}".format(
        random.randint(0, 999), random.randint(0, 99), random.randint(0, 9999)
    )


def generate_passport_number():
    """
    Generates a random passport number consisting of 9 digits.

    Returns:
        str: A randomly generated passport number as a string of 9 digits.
    """
    passport_number = "".join(str(random.randint(0, 9)) for _ in range(9))
    return passport_number


def calculate_luhn_checksum(number):
    """
    Calculates the Luhn checksum digit for a given number string.

    Args:
        number (str): The number string to calculate the checksum for.

    Returns:
        int: The Luhn checksum digit.
    """
    sum_ = 0
    alternate = False
    for i in range(len(number) - 1, -1, -1):
        n = int(number[i])
        if alternate:
            n *= 2
            if n > 9:
                n -= 9
        sum_ += n
        alternate = not alternate
    return (10 - (sum_ % 10)) % 10


def generate_credit_card_number():
    """
    Generates a random credit card number, including a Luhn checksum digit.

    Returns:
        str: A randomly generated credit card number.
    """
    cc_number = "".join(str(random.randint(0, 9)) for _ in range(15))
    checksum = calculate_luhn_checksum(cc_number)
    return cc_number + str(checksum)


def generate_bank_account_number():
    """
    Generates a random bank account number consisting of 12 digits.

    Returns:
        str: A randomly generated bank account number as a string of 12 digits.
    """
    return "".join(str(random.randint(0, 9)) for _ in range(12))


def generate_iban():
    """
    Generates a random IBAN (International Bank Account Number) with the default country code "DE".

    Returns:
        str: A randomly generated IBAN with the country code "DE" followed by 20 digits.
    """
    country_code = "DE"
    return country_code + "".join(str(random.randint(0, 9)) for _ in range(20))


def generate_boolean():
    """
    Generates a random boolean value.

    Returns:
        bool: A randomly generated boolean value.
    """
    return random.choice([True, False])


def generate_binary_data(length):
    """
    Generates random binary data of the specified length.

    Args:
        length (int): The length of the binary data.

    Returns:
        bytes: A randomly generated byte array of the specified length.
    """
    return random.randbytes(length)


def generate_timestamp():
    """
    Generates a random timestamp.

    Returns:
        str: A randomly generated timestamp in ISO 8601 format.
    """
    current_time = int(time.time() * 1000)
    random_millis = random.randint(0, 1000000000)
    random_time = current_time - random_millis
    return datetime.datetime.fromtimestamp(random_time / 1000).isoformat()


def generate_unix_timestamp():
    """
    Generates a random Unix timestamp.

    Returns:
        int: A randomly generated Unix timestamp.
    """
    return int(time.time()) - random.randint(0, 1000000000)


def generate_time():
    """
    Generates a random time in the format "HH:mm:ss".

    Returns:
        str: A randomly generated time.
    """
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def generate_ip_address():
    """
    Generates a random IP address in the format "X.X.X.X".

    Returns:
        str: A randomly generated IP address.
    """
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"


def generate_mac_address():
    """
    Generates a random MAC address in the format "XX:XX:XX:XX:XX:XX".

    Returns:
        str: A randomly generated MAC address.
    """
    return ":".join(f"{random.randint(0, 255):02X}" for _ in range(6))


def generate_hex_color():
    """
    Generates a random hex color code in the format "#RRGGBB".

    Returns:
        str: A randomly generated hex color code.
    """
    return f"#{random.randint(0, 0xFFFFFF):06X}"


def generate_int(min_val, max_val):
    """
    Generates a random integer between the specified minimum and maximum values (inclusive).

    Args:
        min_val (int): The minimum value.
        max_val (int): The maximum value.

    Returns:
        int: A randomly generated integer between min_val and max_val (inclusive).
    """
    return random.randint(min_val, max_val)


def generate_float(min_val, max_val):
    """
    Generates a random float between the specified minimum and maximum values.

    Args:
        min_val (float): The minimum value.
        max_val (float): The maximum value.

    Returns:
        float: A randomly generated float between min_val and max_val.
    """
    return random.uniform(min_val, max_val)


def generate_double(min_val, max_val):
    """
    Generates a random double between the specified minimum and maximum values.

    Args:
        min_val (float): The minimum value.
        max_val (float): The maximum value.

    Returns:
        float: A randomly generated double between min_val and max_val.
    """
    return random.uniform(min_val, max_val)


def generate_long(min_val, max_val):
    """
    Generates a random long between the specified minimum and maximum values.

    Args:
        min_val (int): The minimum value.
        max_val (int): The maximum value.

    Returns:
        int: A randomly generated long between min_val and max_val.
    """
    return random.randint(min_val, max_val)


def generate_byte():
    """
    Generates a random byte.

    Returns:
        int: A randomly generated byte.
    """
    return random.randint(0, 255)


def generate_byte_array(length):
    """
    Generates a random byte array of the specified length.

    Args:
        length (int): The length of the byte array.

    Returns:
        bytes: A randomly generated byte array.
    """
    return random.randbytes(length)


def generate_short(min_val, max_val):
    """
    Generates a random short between the specified minimum and maximum values (inclusive).

    Args:
        min_val (int): The minimum value.
        max_val (int): The maximum value.

    Returns:
        int: A randomly generated short between min_val and max_val (inclusive).
    """
    return random.randint(min_val, max_val)


def generate_char(min_val, max_val):
    """
    Generates a random char between the specified minimum and maximum values (inclusive).

    Args:
        min_val (str): The minimum char value.
        max_val (str): The maximum char value.

    Returns:
        str: A randomly generated char between min_val and max_val (inclusive).
    """
    return chr(random.randint(ord(min_val), ord(max_val)))


def generate_hex(length):
    """
    Generates a random hex string of the specified length.

    Args:
        length (int): The length of the hex string.

    Returns:
        str: A randomly generated hex string.
    """
    return "".join(f"{random.randint(0, 15):X}" for _ in range(length))


def generate_gaussian(mean: float, standard_deviation: float) -> float:
    """
    Generates a random Gaussian distributed value.

    Args:
        mean (float): The mean of the distribution.
        standard_deviation (float): The standard deviation of the distribution.

    Returns:
        float: A randomly generated Gaussian distributed value.
    """
    return random.gauss(mean, standard_deviation)


def generate_random_with_custom_distribution(probabilities: List[float]) -> int:
    """
    Generates a random integer based on a custom distribution.

    Args:
        probabilities (List[float]): An array of probabilities for each integer.

    Returns:
        int: A randomly generated integer based on the given probabilities.
    """
    return np.random.choice(len(probabilities), p=probabilities)


def generate_random_prime(min_val: int, max_val: int) -> int:
    """
    Generates a random prime number between the specified minimum and maximum values.

    Args:
        min_val (int): The minimum value.
        max_val (int): The maximum value.

    Returns:
        int: A randomly generated prime number between min_val and max_val.
    """

    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    num = random.randint(min_val, max_val)
    while not is_prime(num):
        num = random.randint(min_val, max_val)
    return num


def generate_random_percentage() -> float:
    """
    Generates a random percentage between 0 and 100.

    Returns:
        float: A randomly generated percentage.
    """
    return random.uniform(0.0, 100.0)


def generate_random_from_set(s: List[int]) -> int:
    """
    Generates a random integer from a given set of integers.

    Args:
        s (List[int]): An array of integers.

    Returns:
        int: A randomly selected integer from the given set.
    """
    return random.choice(s)


def generate_random_even(min_val: int, max_val: int) -> int:
    """
    Generates a random even integer between the specified minimum and maximum values.

    Args:
        min_val (int): The minimum value.
        max_val (int): The maximum value.

    Returns:
        int: A randomly generated even integer between min_val and max_val.
    """
    num = random.randint(min_val, max_val)
    if num % 2 != 0:
        num += 1
    return num


def generate_random_odd(min_val: int, max_val: int) -> int:
    """
    Generates a random odd integer between the specified minimum and maximum values.

    Args:
        min_val (int): The minimum value.
        max_val (int): The maximum value.

    Returns:
        int: A randomly generated odd integer between min_val and max_val.
    """
    num = random.randint(min_val, max_val)
    if num % 2 == 0:
        num += 1
    return num


def generate_unique_random_sequence(
    min_val: int, max_val: int, length: int
) -> List[int]:
    """
    Generates a unique random sequence of integers.

    Args:
        min_val (int): The minimum value.
        max_val (int): The maximum value.
        length (int): The length of the sequence.

    Returns:
        List[int]: An array containing a unique random sequence of integers.
    """
    if length > (max_val - min_val + 1):
        raise ValueError("Sequence length exceeds the range size.")
    numbers = list(range(min_val, max_val + 1))
    random.shuffle(numbers)
    return numbers[:length]


def generate_random_exponential(lambda_val: float) -> float:
    """
    Generates a random value based on an exponential distribution.

    Args:
        lambda_val (float): The rate parameter of the distribution.

    Returns:
        float: A randomly generated value based on the exponential distribution.
    """
    return -math.log(1 - random.random()) / lambda_val


def generate_random_complex_number(
    real_min: float, real_max: float, imaginary_min: float, imaginary_max: float
) -> ComplexNumber:
    """
    Generates a random complex number with real and imaginary parts within specified ranges.

    Args:
        real_min (float): The minimum value for the real part.
        real_max (float): The maximum value for the real part.
        imaginary_min (float): The minimum value for the imaginary part.
        imaginary_max (float): The maximum value for the imaginary part.

    Returns:
        ComplexNumber: A randomly generated complex number.
    """
    real_part = random.uniform(real_min, real_max)
    imaginary_part = random.uniform(imaginary_min, imaginary_max)
    return ComplexNumber(real_part, imaginary_part)


def is_numeric(s: str) -> bool:
    """
    Checks if a string is numeric.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is numeric, False otherwise.
    """
    return s.isdigit()
