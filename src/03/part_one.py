
class PartOne:

    def load_data(self, filename):

        with open(filename) as f:
            lines = f.readlines()

        parsed = []

        for line in lines:
            parsed.append(line.replace('\n', ''))

        return parsed

    def map_path(self, map, vector):

        # start at top left 0,0
        position = Vector(0, 0)

        distance = len(map) - 1

        trees = 0

        while position.y <= distance:

            if self.is_position_tree(position, map):
                # print("tree at {0}, {1}".format(position.x, position.y))
                trees += 1
            else:
                # print("space at {0}, {1}".format(position.x, position.y))
                pass

            position = self.get_next_position(position, vector)

        return trees

    def get_next_position(self, location, vector):

        x = location.x + vector.x
        y = location.y + vector.y

        return Vector(x, y)

    def is_position_tree(self, position, map):

        width = len(map[0])

        x = position.x

        if x >= width:
            x = x % width

        return map[position.y][x] == "#"


class Vector:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    instance = PartOne()
    map = instance.load_data("part_one.txt")
    trees = instance.map_path(map, Vector(3, 1))
    print("{0} trees encountered".format(trees))
