
class PartOne:

    def load_data(self, filename):

        with open(filename) as f:
            lines = f.readlines()

        groups = []
        group = []

        for line in lines:
            line = line.replace("\n", "")

            if line == "":
                groups.append(group)
                group = []
            else:
                group.append(line)

        if len(group) > 0:
            groups.append(group)

        return groups

    def count_unique_answers(self, group):

        unique = set()

        for line in group:

            line_set = set(line)

            unique = unique | line_set

        return len(unique)


if __name__ == "__main__":
    i = PartOne()
    groups = i.load_data("part_one.txt")

    total_count = 0

    for group in groups:
        total_count = total_count + i.count_unique_answers(group)

    print("Unique answers: {0}".format(total_count))



