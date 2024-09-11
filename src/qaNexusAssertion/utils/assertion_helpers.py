import re
import datetime
from typing import Callable, Collection, Dict, List, Type, TypeVar, Any, Union
from qaNexusAssertion.utils.assertion_exception import AssertionException

T = TypeVar('T')  # Define the TypeVar for generic type usage

def assert_is_number(obj, message):
    """
    Asserts that the given object is an instance of a number.

    :param obj: The object to check.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the object is not an instance of a number.
    """
    if not isinstance(obj, (int, float, complex)):
        raise AssertionException(message)

def assert_is_not_number(obj, message):
    """
    Asserts that the given object is not an instance of a number.

    :param obj: The object to check.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the object is an instance of a number.
    """
    if isinstance(obj, (int, float, complex)):
        raise AssertionException(message)
    
def assert_equals(expected, actual, message):
    """
    Asserts that two objects are equal.

    :param expected: The expected object.
    :param actual: The actual object.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the objects are not equal.
    """
    if expected is None and actual is None:
        return
    if expected != actual:
        raise AssertionException(f"{message} Expected: {expected}, but was: {actual}")

def assert_not_equals(expected, actual, message):
    """
    Asserts that two objects are not equal.

    :param expected: The object that is expected to be different.
    :param actual: The actual object.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the objects are equal.
    """
    if expected is None and actual is None:
        raise AssertionException(f"{message} Both objects are null, expected them to be different.")
    if expected == actual:
        raise AssertionException(f"{message} Expected objects to be different, but both were: {actual}")

def assert_deep_equals(expected, actual, message):
    """
    Asserts that two objects are deeply equal.

    :param expected: The expected object.
    :param actual: The actual object.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the objects are not deeply equal.
    """
    if expected != actual:
        raise AssertionException(f"{message} Expected: {expected}, but was: {actual}")

def assert_not_deep_equals(expected, actual, message):
    """
    Asserts that two objects are not deeply equal.

    :param expected: The object that is expected to be different.
    :param actual: The actual object.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the objects are deeply equal.
    """
    if expected == actual:
        raise AssertionException(f"{message} Expected objects to be different, but both were deeply equal: {actual}")

def assert_is_true(condition, message):
    """
    Asserts that a condition is true.

    :param condition: The condition to check.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the condition is false.
    """
    if not condition:
        raise AssertionException(message)

def assert_is_false(condition, message):
    """
    Asserts that a condition is false.

    :param condition: The condition to check.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the condition is true.
    """
    if condition:
        raise AssertionException(message)
    
def assert_throws(runnable, message):
    """
    Asserts that executing the given callable throws an exception.

    :param runnable: The callable to execute.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If no exception is thrown.
    """
    try:
        runnable()
    except Exception:
        return
    raise AssertionException(message)

def assert_is_type_of(expected_type, obj, message):
    """
    Asserts that the given object is an instance of the specified class.

    :param expected_type: The expected class type.
    :param obj: The object to check.
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the object is not an instance of the expected class.
    """
    if not isinstance(obj, expected_type):
        raise AssertionException(f"{message} Expected type: {expected_type.__name__}, but was: {type(obj).__name__}")

def assert_in_range(value, min_value, max_value, message):
    """
    Asserts that a number is within the specified range (exclusive).

    :param value: The value to check.
    :param min_value: The minimum value (exclusive).
    :param max_value: The maximum value (exclusive).
    :param message: The message to include in the exception if the assertion fails.
    :raises AssertionException: If the value is not within the specified range.
    """
    if not (min_value < value < max_value):
        raise AssertionException(f"{message} Expected: {min_value} < {value} < {max_value}")
    
def assert_not_in_range(value, min_value, max_value, message):
    """
    Asserts that a number is not within the specified range (exclusive).
    """
    if min_value < value < max_value:
        raise AssertionException(f"{message} Expected: {value} to not be in range ({min_value}, {max_value})")

def assert_in_range_included(value, min_value, max_value, message):
    """
    Asserts that a number is within the specified range (inclusive).
    """
    if not (min_value <= value <= max_value):
        raise AssertionException(f"{message} Expected: {min_value} <= {value} <= {max_value}")

def assert_not_in_range_included(value, min_value, max_value, message):
    """
    Asserts that a number is not within the specified range (inclusive).
    """
    if min_value <= value <= max_value:
        raise AssertionException(f"{message} Expected: {value} to not be in range [{min_value}, {max_value}]")

def assert_collection_contains(collection, element, message):
    """
    Asserts that a collection contains the specified element.
    """
    if element not in collection:
        raise AssertionException(f"{message} Collection does not contain: {element}")

def assert_subset_of(subset, superset, message):
    """
    Asserts that the first collection is a subset of the second collection.
    """
    if not set(subset).issubset(superset):
        raise AssertionException(f"{message} Expected subset, but was not found")

def assert_disjoint(collection1, collection2, message):
    """
    Asserts that two collections are disjoint (do not share any common elements).
    """
    if set(collection1).intersection(collection2):
        common_elements = set(collection1).intersection(collection2)
        raise AssertionException(f"{message} Collections are not disjoint; common element(s): {common_elements}")

def assert_is_null_or_undefined(obj, message):
    """
    Asserts that an object is either null or undefined (not set).
    """
    if obj is not None:
        raise AssertionException(message)

def assert_is_null(obj, message):
    """
    Asserts that an object is null.
    """
    if obj is not None:
        raise AssertionException(message)

def assert_is_not_null_or_undefined(obj, message):
    """
    Asserts that an object is not null.
    """
    if obj is None:
        raise AssertionException(message)

def assert_object_has_property(obj, property_name, message):
    """
    Asserts that an object has a specified property.
    """
    if isinstance(obj, dict):
        if property_name not in obj:
            raise AssertionException(f"{message} Object does not have property: {property_name}")
    else:
        if not hasattr(obj, property_name):
            raise AssertionException(f"{message} Object does not have property: {property_name}")

def assert_has_property_value(obj, field_name, expected_value, message):
    """
    Asserts that an object has a specified property with a given value.
    """
    if isinstance(obj, dict):
        actual_value = obj.get(field_name, None)
    else:
        if not hasattr(obj, field_name):
            raise AssertionException(f"{message} Object does not have property: {field_name}")
        actual_value = getattr(obj, field_name)

    if actual_value != expected_value:
        raise AssertionException(f"{message} Expected value for '{field_name}' was {expected_value}, but got {actual_value}")
    
def assert_empty_object(obj: Union[dict, Collection, str, None], message: str):
    """
    Asserts that an object (dict, collection, or string) is empty.
    
    Args:
        obj: The object to check. Can be a dict, collection, string, or None.
        message: The message to include in the exception if the assertion fails.

    Raises:
        AssertionException: If the object is not empty.
    """
    if obj is None:
        raise AssertionException(f"{message} Expected non-empty object, but got None.")
        
    if isinstance(obj, dict) and obj:
        raise AssertionException(f"{message} Expected empty map, but was not.")
    elif isinstance(obj, Collection) and obj:
        raise AssertionException(f"{message} Expected empty collection, but was not.")
    elif isinstance(obj, str) and obj:
        raise AssertionException(f"{message} Expected empty string, but was not.")
    
def assert_greater_than(value: float, reference: float, message: str):
    """
    Asserts that a number is greater than a specified reference value.
    """
    if value <= reference:
        raise AssertionException(f"{message} Expected: {value} > {reference}")

def assert_greater_than_or_equal(value: float, reference: float, message: str):
    """
    Asserts that a number is greater than or equal to a specified reference value.
    """
    if value < reference:
        raise AssertionException(f"{message} Expected: {value} >= {reference}")

def assert_less_than(value: float, reference: float, message: str):
    """
    Asserts that a number is less than a specified reference value.
    """
    if value >= reference:
        raise AssertionException(f"{message} Expected: {value} < {reference}")

def assert_less_than_or_equal(value: float, reference: float, message: str):
    """
    Asserts that a number is less than or equal to a specified reference value.
    """
    if value > reference:
        raise AssertionException(f"{message} Expected: {value} <= {reference}")

def assert_object_has_keys(obj: Dict[Any, Any], keys: Collection[Any], message: str):
    """
    Asserts that a dictionary has all specified keys.
    """
    missing_keys = [key for key in keys if key not in obj]
    if missing_keys:
        raise AssertionException(f"{message} Object is missing key(s): {', '.join(map(str, missing_keys))}")

def assert_is_collection_empty(collection: Collection[Any], message: str):
    """
    Asserts that a collection is empty.
    """
    if collection:
        raise AssertionException(f"{message} Expected empty collection, but was not.")

def assert_collection_is_not_empty(collection: Collection[Any], message: str):
    """
    Asserts that a collection is not empty.
    """
    if not collection:
        raise AssertionException(f"{message} Expected non-empty collection, but was empty.")

def assert_collection_length(collection: Collection[Any], expected_length: int, message: str):
    """
    Asserts that a collection has a specified length.
    """
    if len(collection) != expected_length:
        raise AssertionException(f"{message} Expected length: {expected_length}, but was: {len(collection)}")

def assert_string_length(string: str, expected_length: int, message: str):
    """
    Asserts that a string has a specified length.
    """
    if len(string) != expected_length:
        raise AssertionException(f"{message} Expected length: {expected_length}, but was: {len(string)}")

def assert_string_contains(string: str, substring: str, message: str):
    """
    Asserts that a string contains a specified substring.
    """
    if substring not in string:
        raise AssertionException(f"{message} String does not contain: {substring}")

def assert_string_starts_with(string: str, prefix: str, message: str):
    """
    Asserts that a string starts with a specified prefix.
    """
    if not string.startswith(prefix):
        raise AssertionException(f"{message} String does not start with: {prefix}")

def assert_string_ends_with(string: str, suffix: str, message: str):
    """
    Asserts that a string ends with a specified suffix.
    """
    if not string.endswith(suffix):
        raise AssertionException(f"{message} String does not end with: {suffix}")

def assert_string_matches_regex(string: str, regex: str, message: str):
    """
    Asserts that a string matches a specified regular expression pattern.
    """
    if not re.fullmatch(regex, string):
        raise AssertionException(f"{message} String does not match pattern: {regex}")

def assert_string_not_matches_regex(string: str, regex: str, message: str):
    """
    Asserts that a string does not match a specified regular expression pattern.
    """
    if re.fullmatch(regex, string):
        raise AssertionException(f"{message} String matches pattern: {regex}")

def assert_instance_of(expected_class: Type[Any], obj: Any, message: str):
    """
    Asserts that an object is an instance of a specified class.

    Args:
        expected_class: The class that the object is expected to be an instance of.
        obj: The object to check.
        message: The message to include in the exception if the assertion fails.

    Raises:
        AssertionException: If the object is not an instance of the expected class.
    """
    if not isinstance(obj, expected_class):
        raise AssertionException(f"{message} Object is not an instance of: {expected_class.__name__}")
    
def assert_date(obj: object, message: str):
    """
    Asserts that the given object is a date.

    Args:
        obj (object): The object to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the object is not a date.
    """
    if not isinstance(obj, datetime.date):
        raise AssertionException(f"{message} Object is not a Date")

def assert_date_format(date: str, format: str, message: str):
    """
    Asserts that the given date string matches the specified format.

    Args:
        date (str): The date string to check.
        format (str): The format string to compare against.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the date string does not match the format.
    """
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise AssertionException(f"{message} Date does not match format: {format}")

def assert_is_function(obj: object, message: str):
    """
    Asserts that the given object is callable (i.e., a function).

    Args:
        obj (object): The object to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the object is not callable.
    """
    if not callable(obj):
        raise AssertionException(f"{message} Object is not callable")

def assert_not_deep_include(collection: Collection, element: object, message: str):
    """
    Asserts that the given element is not deeply included in the collection.

    Args:
        collection (Collection): The collection to check.
        element (object): The element to check for.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the collection deeply includes the element.
    """
    if element in collection:
        raise AssertionException(f"{message} Collection deeply includes: {element}")

def assert_nested_include(collection: Collection, nested_element: object, message: str):
    """
    Asserts that the given nested element is included in the collection.

    Args:
        collection (Collection): The collection to check.
        nested_element (object): The nested element to check for.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the nested element is not included in the collection.
    """
    for element in collection:
        if isinstance(element, Collection) and nested_element in element:
            return
    raise AssertionException(f"{message} Collection does not include nested element: {nested_element}")

def assert_not_nested_include(collection: Collection, nested_element: object, message: str):
    """
    Asserts that the given nested element is not included in the collection.

    Args:
        collection (Collection): The collection to check.
        nested_element (object): The nested element to check for.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the nested element is included in the collection.
    """
    for element in collection:
        if isinstance(element, Collection) and nested_element in element:
            raise AssertionException(f"{message} Collection includes nested element: {nested_element}")

def assert_close_to(actual: float, expected: float, delta: float, message: str):
    """
    Asserts that the actual value is close to the expected value within a given delta.

    Args:
        actual (float): The actual value.
        expected (float): The expected value.
        delta (float): The acceptable delta.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the actual value is not within the delta of the expected value.
    """
    if abs(actual - expected) > delta:
        raise AssertionException(f"{message} Expected: {actual} to be close to: {expected} within: {delta}")

def assert_collections_same_members(collection1: Collection, collection2: Collection, message: str):
    """
    Asserts that two collections have the same members.

    Args:
        collection1 (Collection): The first collection.
        collection2 (Collection): The second collection.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the collections do not have the same members.
    """
    if not (set(collection1) == set(collection2)):
        raise AssertionException(f"{message} Collections do not have the same members")

def assert_collection_not_same_members(collection1: Collection, collection2: Collection, message: str):
    """
    Asserts that two collections do not have the same members.

    Args:
        collection1 (Collection): The first collection.
        collection2 (Collection): The second collection.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the collections have the same members.
    """
    if set(collection1) == set(collection2):
        raise AssertionException(f"{message} Collections have the same members, but they should not")

def assert_is_increment_of(value: int, reference: int, message: str):
    """
    Asserts that the value is exactly one greater than the reference value.

    Args:
        value (int): The value to check.
        reference (int): The reference value.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is not an increment of the reference value.
    """
    if value != reference + 1:
        raise AssertionException(f"{message} Expected: {value} to be increment of: {reference}")

def assert_not_increment_of(value: int, reference: int, message: str):
    """
    Asserts that the value is not exactly one greater than the reference value.

    Args:
        value (int): The value to check.
        reference (int): The reference value.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is an increment of the reference value.
    """
    if value == reference + 1:
        raise AssertionException(f"{message} Expected: {value} not to be increment of: {reference}")

def assert_is_decrement_of(value: int, reference: int, message: str):
    """
    Asserts that the value is exactly one less than the reference value.

    Args:
        value (int): The value to check.
        reference (int): The reference value.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is not a decrement of the reference value.
    """
    if value != reference - 1:
        raise AssertionException(f"{message} Expected: {value} to be decrement of: {reference}")

def assert_not_decrement_of(value: int, reference: int, message: str):
    """
    Asserts that the value is not exactly one less than the reference value.

    Args:
        value (int): The value to check.
        reference (int): The reference value.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is a decrement of the reference value.
    """
    if value == reference - 1:
        raise AssertionException(f"{message} Expected: {value} not to be decrement of: {reference}")

def assert_zero(value: float, message: str):
    """
    Asserts that the value is zero.

    Args:
        value (float): The value to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is not zero.
    """
    if value != 0:
        raise AssertionException(f"{message} Expected: {value} to be zero")

def assert_not_zero(value: float, message: str):
    """
    Asserts that the value is not zero.

    Args:
        value (float): The value to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is zero.
    """
    if value == 0:
        raise AssertionException(f"{message} Expected: {value} not to be zero")

def assert_positive(value: float, message: str):
    """
    Asserts that the value is positive.

    Args:
        value (float): The value to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is not positive.
    """
    if value <= 0:
        raise AssertionException(f"{message} Expected: {value} to be positive")

def assert_negative(value: float, message: str):
    """
    Asserts that the value is negative.

    Args:
        value (float): The value to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is not negative.
    """
    if value >= 0:
        raise AssertionException(f"{message} Expected: {value} to be negative")

def assert_odd(value: int, message: str):
    """
    Asserts that the value is odd.

    Args:
        value (int): The value to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is not odd.
    """
    if value % 2 != 1:
        raise AssertionException(f"{message} Expected: {value} to be odd")

def assert_even(value: int, message: str):
    """
    Asserts that the value is even.

    Args:
        value (int): The value to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the value is not even.
    """
    if value % 2 != 0:
        raise AssertionException(f"{message} Expected: {value} to be even")

def assert_valid_url(url: str, message: str):
    """
    Asserts that the given string is a valid URL.

    Args:
        url (str): The URL to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the string is not a valid URL.
    """
    if not re.match(r'^https?://\S+$', url):
        raise AssertionException(f"{message} String is not a valid URL")

def assert_valid_email(email: str, message: str):
    """
    Asserts that the given string is a valid email address.

    Args:
        email (str): The email address to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the email address is not valid.
    """
    regex = r'^[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}$'
    if not re.match(regex, email):
        raise AssertionException(f"{message} Email address is not valid")

def assert_is_array(obj: object, message: str):
    """
    Asserts that the given object is a list.

    Args:
        obj (object): The object to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the object is not a list.
    """
    if not isinstance(obj, list):
        raise AssertionException(f"{message} Object is not a list")

def assert_is_not_array(obj: object, message: str):
    """
    Asserts that the given object is not a list.

    Args:
        obj (object): The object to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the object is a list.
    """
    if isinstance(obj, list):
        raise AssertionException(f"{message} Object is a list, but should not be")

def assert_array_length(array: List, expected_length: int, message: str):
    """
    Asserts that the length of the array matches the expected length.

    Args:
        array (List): The list to check.
        expected_length (int): The expected length of the list.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the length of the list does not match the expected length.
    """
    if len(array) != expected_length:
        raise AssertionException(f"{message} Expected array length: {expected_length}, but was: {len(array)}")

def assert_object_is_empty(obj: object, message: str):
    """
    Asserts that the given object (dict, list, or string) is empty.

    Args:
        obj (object): The object to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the object is not empty.
    """
    if isinstance(obj, (dict, list, str)) and obj:
        raise AssertionException(f"{message} Expected empty object, but was not.")

def assert_object_is_not_empty(obj: object, message: str):
    """
    Asserts that the given object (dict, list, or string) is not empty.

    Args:
        obj (object): The object to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the object is empty.
    """
    if isinstance(obj, (dict, list, str)) and not obj:
        raise AssertionException(f"{message} Expected non-empty object, but was empty.")

def assert_object_includes(obj: Dict, value: object, message: str):
    """
    Asserts that the given object (dict) includes the specified value.

    Args:
        obj (Dict): The dictionary to check.
        value (object): The value to check for.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the object does not include the value.
    """
    if value not in obj.values():
        raise AssertionException(f"{message} Object does not include value: {value}")

def assert_string_is_empty(s: str, message: str):
    """
    Asserts that the given string is empty.

    Args:
        s (str): The string to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the string is not empty.
    """
    if s:
        raise AssertionException(f"{message} Expected empty string, but was not.")

def assert_string_is_not_empty(s: str, message: str):
    """
    Asserts that the given string is not empty.

    Args:
        s (str): The string to check.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the string is empty.
    """
    if not s:
        raise AssertionException(f"{message} Expected non-empty string, but was empty.")

def assert_string_matches_pattern(s: str, pattern: str, message: str):
    """
    Asserts that the given string matches the specified regular expression pattern.

    Args:
        s (str): The string to check.
        pattern (str): The regular expression pattern.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the string does not match the pattern.
    """
    if not re.match(pattern, s):
        raise AssertionException(f"{message} String does not match pattern: {pattern}")

def assert_function_throws(func: Callable, expected_exception: Type[Exception], message: str):
    """
    Asserts that the given function throws the expected exception.

    Args:
        func (Callable): The function to call.
        expected_exception (Type[Exception]): The expected exception type.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the function does not throw the expected exception.
    """
    try:
        func()
    except Exception as e:
        if isinstance(e, expected_exception):
            return
        else:
            raise AssertionException(f"{message} Expected exception: {expected_exception.__name__}, but was: {e.__class__.__name__}")
    raise AssertionException(f"{message} Expected exception, but none was thrown.")

def assert_function_does_not_throw(func: Callable, message: str):
    """
    Asserts that the given function does not throw any exception.

    Args:
        func (Callable): The function to call.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the function throws an exception.
    """
    try:
        func()
    except Exception as e:
        raise AssertionException(f"{message} Expected no exception, but caught: {e.__class__.__name__}")

def assert_function_returns(expected_value: T, func: Callable[[], T], message: str):
    """
    Asserts that the given function returns the expected value.

    Args:
        expected_value (T): The expected return value.
        func (Callable[[], T]): The function to call.
        message (str): The error message if the assertion fails.

    Raises:
        AssertionException: If the function does not return the expected value.
    """
    result = func()
    if result != expected_value:
        raise AssertionException(f"{message} Expected return: {expected_value}, but was: {result}")