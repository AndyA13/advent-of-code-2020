
class PartOne:

    def load_data(self, filename):

        with open(filename) as f:
            lines = f.readlines()

        passwords = []

        for line in lines:
            passwords.append(self.parse_line(line))

        return passwords

    def parse_line(self, line):

        # 1-3 a: abcde
        parts = line.split(":")
        password = parts[1].strip()

        # 1-3 a
        parts = parts[0].split(" ")
        key = parts[1].strip()

        # 1-3
        parts = parts[0].split("-")
        min = int(parts[0].strip())
        max = int(parts[1].strip())

        return Password(min, max, key, password)

    def validate_password(self, password):

        appearances = password.password.count(password.key)

        return appearances >= password.min and appearances <= password.max

    def count_valid_passwords(self, passwords):

        valid = 0
        invalid = 0

        for password in passwords:
            if self.validate_password(password):
                valid += 1
            else:
                invalid += 1

        return [valid, invalid]

class Password:

    min = 0
    max = 0
    key = ''
    password =''

    def __init__(self, min, max, key, password):
        self.min = min
        self.max = max
        self.key = key
        self.password = password


if __name__ == "__main__":
    instance = PartOne()
    passwords = instance.load_data("part_one.txt")
    result = instance.count_valid_passwords(passwords)
    print("Valid:   {0}".format(result[0]))
    print("Invalid: {0}".format(result[1]))
