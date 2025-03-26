class NumberExtractor:
    """A class to manage the extraction of numbers from a predefined set.
    Attributes:
        numbers (set): A set containing numbers from 1 to 100.
        extracted (int or None): The last extracted number, or None
        if no number has been extracted.
    Methods:
        extract(number: int): Extracts a number from the set if it
        is within the allowed range.
        calculate_number_extracted(): Calculate extracted number,
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
        self.extracted = self.calculate_number_extracted(number)
        return number

    def calculate_number_extracted(self, number: int):
        """Calculates the extracted number based on the given number.
        Args:
            number (int): The number to be extracted.
        Returns:
            int: The extracted number.
        """
        if number is None or number not in self.numbers:
            raise ValueError("Invalid number")
        sum_total = int(sum(self.numbers) / 2)
        sum_actual = sum_total - number
        return sum_total - sum_actual
