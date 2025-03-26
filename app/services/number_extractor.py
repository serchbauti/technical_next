class NumberExtractor:
    def __init__(self):
        self.numbers = set(range(1, 101))
        self.extracted = None

    def extract(self, number: int):
        if number not in self.numbers:
            raise ValueError("Number outside the allowed range (1-100).")

        self.extracted = number
        return number

    def get_extracted(self):
        if self.extracted is None:
            raise ValueError("No number has been drawn yet.")
        return self.extracted
