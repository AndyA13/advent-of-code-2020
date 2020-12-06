
class PartOne:

    def load_data(self, filename):

        with open(filename) as f:
            lines = f.readlines()

        passports = []
        current_lines = []

        for line in lines:

            if not line or line == "\n":
                # end of passport
                passports.append(Passport(current_lines))

                current_lines.clear()

            else:
                current_lines.append(line)

        # catch the last one
        if len(current_lines) > 0:
            passports.append(Passport(current_lines))

        return passports

class Passport():

    byr = "" # (Birth Year)
    iyr = "" # (Issue Year)
    eyr = "" # (Expiration Year)
    hgt = "" # (Height)
    hcl = "" # (Hair Color)
    ecl = "" # (Eye Color)
    pid = "" # (Passport ID)
    cid = "" # (Country ID)

    def __init__(self, lines):

        for line in lines:

            parts = line.split(" ")

            for part in parts:

                kvp = part.split(":")

                self.__setattr__(kvp[0], kvp[1])

    def is_valid(self):

        return self.byr != "" \
            and self.iyr != "" \
            and self.eyr != "" \
            and self.hgt != "" \
            and self.hcl != "" \
            and self.ecl != "" \
            and self.pid != ""


if __name__ == "__main__":
    instance = PartOne()
    passports = instance.load_data("part_one.txt")

    valid_count = 0

    for p in passports:
        if p.is_valid():
            valid_count += 1

    print("{0} passports were valid".format(valid_count))