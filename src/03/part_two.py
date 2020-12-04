from part_one import PartOne, Vector

if __name__ == "__main__":

    instance = PartOne()

    map = instance.load_data("part_one.txt")

    trees = []

    trees.append(instance.map_path(map, Vector(1, 1)))
    trees.append(instance.map_path(map, Vector(3, 1)))
    trees.append(instance.map_path(map, Vector(5, 1)))
    trees.append(instance.map_path(map, Vector(7, 1)))
    trees.append(instance.map_path(map, Vector(1, 2)))

    product = 1

    for i in trees:
        product = product * i

    print("Product: {0}".format(product))

