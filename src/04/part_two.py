import re

class PartTwo:

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

                # bloody line breaks will be the end of me!
                self.__setattr__(kvp[0], kvp[1].replace("\n", ""))

    def __repr__(self):
        return "byr: {0}\niyr: {1}\neyr: {2}\nhgt: {3}\nhcl: {4}\necl: {5}\npid: {6}" \
            .format(self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid)

    def is_valid(self):

        return self.validate_byr() \
            and self.validate_iyr() \
            and self.validate_eyr() \
            and self.validate_hgt() \
            and self.validate_hcl() \
            and self.validate_ecl() \
            and self.validate_pid()

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    def validate_byr(self):
        return self.validate_number(self.byr, 1920, 2002)

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    def validate_iyr(self):
        return self.validate_number(self.iyr, 2010, 2020)

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    def validate_eyr(self):
        return self.validate_number(self.eyr, 2020, 2030)

    # hgt (Height) - a number followed by either cm or in:
    #  If cm, the number must be at least 150 and at most 193.
    #  If in, the number must be at least 59 and at most 76.
    def validate_hgt(self):
        if self.hgt.endswith("cm"):
            return self.validate_number(self.hgt.rstrip("cm"), 150, 193)

        if self.hgt.endswith("in"):
            return self.validate_number(self.hgt.rstrip("in"), 59, 76)

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    def validate_hcl(self):
        match = re.fullmatch("^#[0-9a-f]{6}$", self.hcl)
        return match != None

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    def validate_ecl(self):
        allowed_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.ecl in allowed_values

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    def validate_pid(self):
        match = re.fullmatch("^[0-9]{9}$", self.pid)
        return match != None

    def validate_number(self, value, min, max):
        try:
            val = int(value)
            if val >= min and val <= max:
                return True
        except:
            pass

        return False


if __name__ == "__main__":
    instance = PartTwo()
    passports = instance.load_data("part_one.txt")

    valid_count = 0

    for p in passports:
        if p.is_valid():
            valid_count += 1

    print("{0} passports were valid".format(valid_count))