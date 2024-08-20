from qaNexusAssertion.statictVariables.AssertionsConstants import Constants

class AssertionException(Exception):
    """
    Custom runtime exception used for assertions in the QA Nexus application.
    This exception is intended to be thrown when an assertion fails.
    The exception message will be formatted with a predefined color specified in Constants.
    """

    def __init__(self, message):
        """
        Constructs a new AssertionException with the specified detail message.
        The message is prefixed and suffixed with color codes from Constants
        to highlight the error in the console output.
        
        :param message: The detail message to be used for this exception. This message is formatted with color codes.
        """
        # Calls the base class (Exception) constructor with the formatted message
        super().__init__(f"{Constants.RED_CONSOLE_COLOR}{message}{Constants.DEFAULT_CONSOLE_COLOR}")