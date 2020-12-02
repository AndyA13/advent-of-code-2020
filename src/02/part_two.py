
class PartTwo:

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
        indexes = [int(parts[0].strip()), int(parts[1].strip())]

        return Password(indexes, key, password)

    def validate_password(self, password):

        valid = False

        for i in password.indexes:
            
            if password.password[i - 1] == password.key:

                # letter in correct position
                if valid == True:

                    # already matched, can only match once
                    return False

                valid = True

        return valid

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

    # indices?
    indexes = []
    key = ''
    password =''

    def __init__(self, indexes, key, password):
        self.indexes = indexes
        self.key = key
        self.password = password


if __name__ == "__main__":
    instance = PartTwo()
    passwords = instance.load_data("part_one.txt")
    result = instance.count_valid_passwords(passwords)
    print("Valid:   {0}".format(result[0]))
    print("Invalid: {0}".format(result[1]))
