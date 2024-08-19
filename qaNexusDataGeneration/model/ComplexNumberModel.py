class ComplexNumber:
    """
    Represents a complex number with a real and imaginary part.

    A complex number is a number of the form `a + bi`, where `a` is the real part
    and `b` is the imaginary part.

    Attributes:
        real (float): The real part of the complex number.
        imaginary (float): The imaginary part of the complex number.
    """
    
    def __init__(self, real: float, imaginary: float):
        """
        Constructs a `ComplexNumber` with the specified real and imaginary parts.

        Args:
            real (float): The real part of the complex number.
            imaginary (float): The imaginary part of the complex number.
        """
        self.real = real
        self.imaginary = imaginary
    
    def get_real(self) -> float:
        """
        Returns the real part of this complex number.

        Returns:
            float: The real part of this complex number.
        """
        return self.real
    
    def get_imaginary(self) -> float:
        """
        Returns the imaginary part of this complex number.

        Returns:
            float: The imaginary part of this complex number.
        """
        return self.imaginary
    
    def __str__(self) -> str:
        """
        Returns a string representation of this complex number in the form
        `a + bi`, where `a` is the real part and `b` is the imaginary part,
        formatted to two decimal places.

        Returns:
            str: A string representation of this complex number.
        """
        return f"{self.real:.2f} + {self.imaginary:.2f}i"
