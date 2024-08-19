import unittest
import re
from datetime import datetime
from qaNexusDataGeneration.constantVariables.DataGeneratorConstants import Constants
from qaNexusDataGeneration.enums import CountryCodePhoneNumberPatternEnums, SupportedDateFormatsEnums
from qaNexusDataGeneration.utils.data_generator import DataGenerator

class TestDataGenerator(unittest.TestCase):
    
    def setUp(self):
        self.generator = DataGenerator()

    # def test_generate_string(self):
    #     result = self.generator.generate_string()
    #     self.assertEqual(len(result), Constants.DEFAULT_STRING_LENGTH)
    #     self.assertTrue(all(c in Constants.ALPHA_NUM for c in result))
    #     print("GENERATE STRING: " + result)

    # def test_generate_email(self):
    #     result = self.generator.generate_email()
    #     self.assertTrue('@' in result)
    #     self.assertTrue(result.endswith(Constants.DEFAULT_DOMAIN))
    #     username_length = Constants.DEFAULT_EMAIL_USERNAME_LENGTH
    #     self.assertEqual(len(result.split('@')[0]), username_length)
    #     print("GENERATE EMAIL: " + result)

    # def test_generate_phone_number(self):
    #     for country_code in CountryCodePhoneNumberPatternEnums:
    #         result = self.generator.generate_phone_number(country_code.name)
    #         phone_regex = country_code.value
    #         self.assertTrue(re.match(phone_regex, result))
    #         print("GENERATE PHONE NUMBER: " + result)

    def test_generate_date(self):
        # Test default format
        result = self.generator.generate_date()
        current_date = datetime.now()
        expected = f"{current_date.year}-{current_date.month:02d}-{current_date.day:02d}"
        self.assertEqual(result, expected)
        print("GENERATE DATE_1: " + result)

        # Test custom format
        format_enum = SupportedDateFormatsEnums.SupportedDateFormatsEnums.YYYY_MM_DD.value
        result = self.generator.generate_date(format=format_enum)
        self.assertTrue(result.startswith("yyyy"))
        print("GENERATE DATE_2: " + result)

    # def test_get_max_days(self):
    #     # Test February in a leap year
    #     self.assertEqual(self.generator.get_max_days(2, 2020), 29)
    #     # Test February in a non-leap year
    #     self.assertEqual(self.generator.get_max_days(2, 2019), 28)
    #     # Test April (30 days)
    #     self.assertEqual(self.generator.get_max_days(4, 2023), 30)
    #     # Test July (31 days)
    #     self.assertEqual(self.generator.get_max_days(7, 2023), 31)

if __name__ == '__main__':
    unittest.main()
