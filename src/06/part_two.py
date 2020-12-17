from part_one import PartOne

class PartTwo(PartOne):

    def count_shared_answers(self, group):

        shared = set()
        first = True

        for line in group:

            line_set = set(line)

            if first:
                shared = line_set
                first = False
            else:
                shared = shared & line_set

        return len(shared)


if __name__ == "__main__":
    i = PartTwo()
    groups = i.load_data("part_one.txt")

    total_count = 0

    for group in groups:
        total_count = total_count + i.count_shared_answers(group)

    print("Shared answers: {0}".format(total_count))



