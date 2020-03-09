import unittest

from .date import Date


class TestDate(unittest.TestCase):

    # A simple testCase class for the Date
    # Methods to be tested:
    # 1. month()
    # 2. day()
    # 3. year()
    # 4. dayOfWeek()
    # 5. toString()
    # 6. greaterThan()
    # 7. lessThan()
    # 8. lessThanOrEqualTo

    def setUp(self):
        # Input Date
        self.date = Date(2, 5, 2009)
        self.other_date = Date(1, 23, 2009)

        # Expected Values
        self.expected_month = 2
        self.expected_day = 5
        self.expected_year = 2009
        self.expected_day_of_week = 3
        self.expected_day_of_week_in_words = "Thursday"

    # Test the return of month from the date
    # Input (02/05/2009) - Expected Output 02
    def test_month(self):
        self.assertEqual(self.date.month(), self.expected_month)

    # Test the return of day from the date
    # Input (02/05/2009) - Expected Output 05
    def test_day(self):
        self.assertEqual(self.date.day(), self.expected_day)

    # Test the return of year from the date
    # Input (02/05/2009) - Expected Output 2009
    def test_year(self):
        self.assertEqual(self.date.year(), self.expected_year)

    # Test the return of day of the week from the date
    # Input (02/05/2009) - Expected Output 2009 3
    def test_day_of_week(self):
        self.assertEqual(self.date.dayOfWeek(), self.expected_day_of_week)

    def test_day_of_week_in_words(self):
        self.assertEqual(self.date.dayOfWeekInWords(), self.expected_day_of_week_in_words)

    def test_greater_than_operator(self):
        self.assertEqual(self.date > self.other_date, True)

    def test_less_than_operator(self):
        self.assertEqual(self.date < self.other_date, False)

    def test_greater_than_or_equal(self):
        self.assertEqual(self.date >= self.other_date, True)

    def test_less_than_or_equal(self):
        self.assertEqual(self.date <= self.other_date, False)


if __name__ == "__main__":
    unittest.main()