from qaNexusDataGeneration.utils import data_generator
a = data_generator.generate_int(0, 10)
b = data_generator.generate_email(domain="@test.com")
c = data_generator.generate_phone_number("US")
print(c)