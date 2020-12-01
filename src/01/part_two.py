
class PartTwo:

    def load_data(self, filename):

        with open(filename) as f:
            lines = f.readlines()
            numbers = []
        
            for line in lines:
                numbers.append(int(line))

            return numbers

    def find_trio(self, numbers):
        # It's not pretty but it works (instantly)
        for a in numbers:
            for b in numbers:
                for c in numbers:
                    if a + b + c == 2020:
                        return [a, b, c]

        return [0,0,0]

    def calculate_answer(self, pair):
        return pair[0] * pair[1] * pair[2]

    def run(self):
        data = self.load_data("part_one.txt")
        pair = self.find_trio(data)
        answer = self.calculate_answer(pair)

        print(answer)


if __name__ == "__main__":
    task = PartTwo()
    task.run()