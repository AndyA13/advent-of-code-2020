import unittest
from part_one import PartOne, BoardingPass

class Tests(unittest.TestCase):

    def test_boarding_pass_parses_row(self):

        target = BoardingPass("BBFFBBFRLL")

        self.assertEqual(target.row, 102)

    def test_boarding_pass_parses_column(self):

        target = BoardingPass("BBFFBBFRLL")

        self.assertEqual(target.column, 4)

    def test_boarding_pass_calculates_id(self):

        target = BoardingPass("BBFFBBFRLL")

        self.assertEqual(target.calculate_id(), 820)


if __name__ == "__main__":
    unittest.main()