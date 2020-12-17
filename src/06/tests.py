import unittest
from part_one import PartOne
from part_two import PartTwo

class Tests(unittest.TestCase):

    def test_load_data_seperates_groups(self):
        target = PartOne()
        data = target.load_data("test_data.txt")

        self.assertEqual(len(data), 5)

        self.assertEqual(len(data[0]), 1)
        self.assertEqual(len(data[1]), 3)
        self.assertEqual(len(data[2]), 2)
        self.assertEqual(len(data[3]), 4)
        self.assertEqual(len(data[4]), 1)

    def test_unique_count(self):
        target = PartOne()
        data = ["abc", "abcd"]
        unique_count = target.count_unique_answers(data)
        self.assertEqual(unique_count, 4)

    def test_shared_count(self):
        target = PartTwo()

        data = ["abc", "cde"]
        shared_count = target.count_shared_answers(data)

        self.assertEqual(shared_count, 1)


if __name__ == "__main__":
    unittest.main()