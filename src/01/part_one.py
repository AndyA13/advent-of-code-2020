
class PartOne:

    def load_data(self, filename):

        with open(filename) as f:
            lines = f.readlines()
            numbers = []
        
            for line in lines:
                numbers.append(int(line))

            return numbers

    def find_pair(self, numbers):
        # I could split the list in 2, numbers < target / 2 and number > target / 2
        # as two numbers less than or greater than half, are not going to equal the total
        # meh
        for a in numbers:
            for b in numbers:
                if a + b == 2020:
                    return [a, b]

        return [0,0]

    def calculate_answer(self, pair):
        return pair[0] * pair[1]

    def run(self):
        data = self.load_data("part_one.txt")
        pair = self.find_pair(data)
        answer = self.calculate_answer(pair)

        print(answer)


if __name__ == "__main__":
    task = PartOne()
    task.run()