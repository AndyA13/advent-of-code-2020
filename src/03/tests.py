import unittest
from part_one import PartOne, Vector

#    0 -> x
#  0 ..##.......
#  | #...#...#..
#  y .#....#..#.
#    ..#.#...#.#
#    .#...##..#.
#    ..#.##.....
#    .#.#.#....#
#    .#........#
#    #.##...#...
#    #...##....#
#    .#..#...#.#


class PartOneTests(unittest.TestCase):

    def test_can_load_data(self):

        target = PartOne()
        lines = target.load_data("test_data.txt")

        self.assertEqual(len(lines), 11)

    def test_line_breaks_removed(self):

        target = PartOne()
        lines = target.load_data("test_data.txt")

        self.assertEqual(len(lines[0]), 11)

    def test_get_next_position_adds_vector(self):

        target = PartOne()

        start = Vector(0, 0)

        result = target.get_next_position(start, Vector(1,2))

        self.assertEqual(1, result.x)
        self.assertEqual(2, result.y)

    def test_can_map_path_to_tree(self):

        lines = []
        lines.append("....")
        lines.append("...#")

        target = PartOne()

        position = Vector(3, 1)

        result = target.is_position_tree(position, lines)

        self.assertTrue(result)

    def test_can_map_path_to_space(self):

        lines = []
        lines.append("####")
        lines.append("###.")

        target = PartOne()
        position = Vector(3, 1)

        result = target.is_position_tree(position, lines)

        self.assertFalse(result)

    def test_can_map_across_boundary(self):

        lines = []
        lines.append("...")
        lines.append("#..")

        target = PartOne()
        position = Vector(3, 1)

        result = target.is_position_tree(position, lines)

        self.assertTrue(result)

    def test_can_map_across_boundary_twice(self):

        lines = []
        lines.append("..")
        lines.append(".#")

        target = PartOne()
        position = Vector(6, 1)

        result = target.is_position_tree(position, lines)

        self.assertFalse(result)


    def test_map_returns_expected_result(self):

        target = PartOne()

        map = target.load_data("test_data.txt")

        trees = target.map_path(map, Vector(3, 1))

        self.assertEqual(trees, 7)

    def test_tree_at_twelve_four(self):

        target = PartOne()
        
        map = target.load_data("test_data.txt")

        self.assertTrue(target.is_position_tree(Vector(12, 4), map))


if __name__ == "__main__":
    unittest.main()