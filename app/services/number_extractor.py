class NumberExtractor:
    """A class to manage the extraction of numbers from a predefined set.
    Attributes:
        numbers (set): A set containing numbers from 1 to 100.
        extracted (int or None): The last extracted number, or None
        if no number has been extracted.
    Methods:
        extract(number: int): Extracts a number from the set if it
        is within the allowed range.
        get_extracted(): Returns the last extracted number,
        raising an error if no number has been extracted.
    """
    def __init__(self):
        self.numbers = set(range(1, 101))
        self.extracted = None

    def extract(self, number: int):
        """Extracts a specified number from the predefined set of numbers.
        Args:
            number (int): The number to be extracted, which must be
            within the range of 1 to 100.
        Raises:
            ValueError: If the number is outside the allowed range.
        Returns:
            int: The extracted number.
        """
        if number not in self.numbers:
            raise ValueError("Number outside the allowed range (1-100).")
        self.extracted = number
        return number

    def get_extracted(self):
        """Retrieves the last extracted number.
        Raises:
            ValueError: If no number has been extracted yet.
        Returns:
            int: The last extracted number.
        """
        if self.extracted is None:
            raise ValueError("No number has been drawn yet.")
        return self.extracted
