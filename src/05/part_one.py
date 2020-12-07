class PartOne():

    def load_data(self, filename):
        
        with open(filename) as f:
            lines = f.readlines()

        boarding_passes = []

        for line in lines:
            line = line.replace("\n", "")

            boarding_passes.append(BoardingPass(line))

        return boarding_passes

class BoardingPass():

    source = ""
    row = -1
    column = -1

    def __init__(self, line):
        self.source = line

        row_string = line[:7]
        column_string = line[7:]

        row_string = row_string.replace("B", "1").replace("F", "0")
        self.row = int(row_string, 2)

        column_string = column_string.replace("R", "1").replace("L", "0")
        self.column = int(column_string, 2)

    def calculate_id(self):
        return self.row * 8 + self.column

if __name__ == "__main__":
    target = PartOne()
    passes = target.load_data("part_one.txt")

    # get the highest Id
    ids = []
    for boarding_pass in passes:
        ids.append(boarding_pass.calculate_id())

    print("Highest ID: {0}".format(max(ids)))