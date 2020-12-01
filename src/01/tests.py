import unittest
from part_one import PartOne

class DayOneTests(unittest.TestCase):

    def test_can_load_data(self):

        target = PartOne()

        numbers = target.load_data("test_data.txt")

        self.assertEqual(len(numbers), 6)

    def test_can_find_number_pair(self):

        target = PartOne()

        numbers = target.load_data("test_data.txt")

        answer = target.find_pair(numbers)

        self.assertEqual(answer[0] + answer[1], 2020)

    def test_returns_final_expected_answer(self):

        target = PartOne()
        numbers = target.load_data("test_data.txt")
        pair = target.find_pair(numbers)
        answer = target.calculate_answer(pair)

        self.assertEqual(answer, 514579)


if __name__ == "__main__":
    unittest.main()