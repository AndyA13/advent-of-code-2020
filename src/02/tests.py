import unittest
from part_one import PartOne
from part_two import PartTwo

class PartOneTests(unittest.TestCase):

    def test_can_load_data(self):

        target = PartOne()

        passwords = target.load_data("test_data.txt")

        self.assertEqual(len(passwords), 3)

    def test_line_parses_correctly(self):

        target = PartOne()

        result = target.parse_line("2-5 g: abcgg")

        self.assertEqual(2, result.min)
        self.assertEqual(5, result.max)
        self.assertEqual("g", result.key)
        self.assertEqual("abcgg", result.password)

    def test_valid_password_passes(self):

        target = PartOne()

        password = target.parse_line("1-3 a: abcde")

        result = target.validate_password(password)

        self.assertTrue(result)

    def test_invalid_password_fails(self):

        target = PartOne()

        password = target.parse_line("1-3 b: cdefg")

        result = target.validate_password(password)

        self.assertFalse(result)

    def test_count_returns_correct_number(self):

        target = PartOne()

        passwords = target.load_data("test_data.txt")

        result = target.count_valid_passwords(passwords)

        self.assertEqual(2, result[0])
        self.assertEqual(1, result[1])

class PartTwoTests(unittest.TestCase):

    def test_line_parses_correctly(self):

        target = PartTwo()

        password = target.parse_line("2-5 g: abcgg")

        self.assertEqual(password.key, "g")
        self.assertEqual(password.password, "abcgg")
        self.assertEqual(password.indexes, [2,5])

    def test_valid_passwords_passes(self):

        target = PartTwo()
        password = target.parse_line("1-3 a: abcde")
        result = target.validate_password(password)

        self.assertTrue(result)

    def test_invalid_password_fails_no_match(self):

        target = PartTwo()
        password = target.parse_line("1-3 b: cdefg")
        result = target.validate_password(password)

        self.assertFalse(result)

    def test_invalid_password_fails_double_match(self):

        target = PartTwo()
        password = target.parse_line("2-9 c: ccccccccc")
        result = target.validate_password(password)

        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()