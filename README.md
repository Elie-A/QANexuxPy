# QANexusPY

QANexusPY is a Python library designed for handling quality assurance (QA) tasks such as assertions, data generation, and more. The library provides utility functions and predefined constants for working with complex data generation and validation, tailored to various QA needs.

## Features

- **Assertions Module (`qaNexusAssertion`)**: Provides custom assertion helpers, constants, and exception handling to enhance the testing and validation processes.
- **Data Generation Module (`qaNexusDataGeneration`)**: Allows for generating complex data like phone numbers, dates, and handling different data models. Includes support for enums, constants, and utility methods for generating complex data.

## Installation

### Local Installation

To install the QANexusPY library locally, follow these steps:

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal.
3. Run the following command to install the library:

```bash
pip install .
```

Alternatively, for development purposes, you can install the library in "editable" mode:

```bash
pip install -e .
```

### Requirements

Make sure you have `pip` and `setuptools` installed. The library works with Python 3.6 and above.

## Usage

### Importing the Modules

You can import the various modules and classes provided by QANexusPY to work with assertions and data generation. For example:

```python
from qaNexusAssertion.utils.assertion_helpers import assert_equal
from qaNexusDataGeneration.utils.data_generator import generate_phone_number
```

### Example: Using Assertion Helpers

```python
from qaNexusAssertion.utils.assertion_helpers import assert_equal

try:
    assert_equal(5, 5)
    print("Assertion passed!")
except AssertionError as e:
    print(f"Assertion failed: {e}")
```

### Example: Data Generation

```python
from qaNexusDataGeneration.utils.data_generator import generate_phone_number

phone_number = generate_phone_number(country_code="US")
print(f"Generated phone number: {phone_number}")
```

## Functions and Modules

### Assertion Helpers (`qaNexusAssertion`)

- **assert_equal(actual, expected)**: Asserts that the actual and expected values are equal.
- **assert_not_equal(actual, expected)**: Asserts that the actual and expected values are not equal.
- **assert_true(value)**: Asserts that the value is `True`.

### Data Generation (`qaNexusDataGeneration`)

- **generate_phone_number(country_code: str)**: Generates a valid phone number for the specified country.
- **generate_complex_data()**: Generates a complex data structure, such as a model with multiple attributes.

## Project Structure

The project is structured as follows:

```
QANexusPY/
│
├── qaNexusAssertion/
│   ├── utils/
│   └── statictVariables/
├── qaNexusDataGeneration/
│   ├── enums/
│   ├── model/
│   ├── statictVariables/
│   └── utils/
├── README.md
└── setup.py
```

- **`qaNexusAssertion`**: Contains helpers for custom assertions and exception handling.
- **`qaNexusDataGeneration`**: Focuses on generating various types of data including enums and complex models.

## License

This project is licensed under the MIT License.
