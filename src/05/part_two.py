from part_one import PartOne, BoardingPass

if __name__ == "__main__":

    target = PartOne()
    boarding_passes = target.load_data("part_one.txt")

    ids = []

    for boarding_pass in boarding_passes:
        ids.append(boarding_pass.calculate_id())

    # find empty seats below 835 (max id from part one)
    for x in range(835):
        if not x in ids:
            print("Empty seat found: {0}".format(x))

