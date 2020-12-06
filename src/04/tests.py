import unittest
from part_one import PartOne, Passport
from part_two import PartTwo, Passport as PassportV2

class PartOneTest(unittest.TestCase):

    def test_can_parse_data(self):

        target = PartOne()

        passports = target.load_data("test_data.txt")

        self.assertEqual(len(passports), 4)

    def test_can_parse_passport(self):

        test_data = []
        test_data.append("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd")
        test_data.append("byr:1937 iyr:2017 cid:147 hgt:183cm")

        passport = Passport(test_data)

        self.assertTrue(passport.is_valid())
        self.assertEqual(passport.iyr, "2017")
        self.assertEqual(passport.ecl, "gry")
        self.assertEqual(passport.cid, "147")
        self.assertEqual(passport.eyr, "2020")
        self.assertEqual(passport.pid, "860033327")
        self.assertEqual(passport.hcl, "#fffffd")
        self.assertEqual(passport.byr, "1937")

    def test_passport_is_valid_without_cid(self):

        test_data = []
        test_data.append("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd")
        test_data.append("byr:1937 iyr:2017 hgt:183cm")

        passport = Passport(test_data)

        self.assertEqual(passport.cid, "")
        self.assertTrue(passport.is_valid())

    def test_v2_passport_validates_valid_byr(self):

        target = PassportV2([])
        target.byr = "2002"

        self.assertTrue(target.validate_byr())

    def test_v2_passport_fails_invalid_byr(self):

        target = PassportV2([])
        target.byr = "2003"

        self.assertFalse(target.validate_byr())

    def test_v2_passport_validates_height_in(self):

        target = PassportV2([])
        target.hgt = "60in"

        self.assertTrue(target.validate_hgt())

    def test_v2_passport_validates_height_cm(self):

        target = PassportV2([])
        target.hgt = "190cm"

        self.assertTrue(target.validate_hgt())

    def test_v2_passport_fails_height_in(self):

        target = PassportV2([])
        target.hgt = "190in"

        self.assertFalse(target.validate_hgt())

    def test_v2_passport_fails_height(self):

        target = PassportV2([])
        target.hgt = "190"

        self.assertFalse(target.validate_hgt())

    def test_v2_passport_validates_hcl(self):
        target = PassportV2([])
        target.hcl = "#123abc"
        self.assertTrue(target.validate_hcl())

    def test_v2_passport_fails_invalid_hcl(self):
        target = PassportV2([])
        target.hcl = "#123abz"
        self.assertFalse(target.validate_hcl())

    def test_v2_passport_fails_invalid_hcl_2(self):
        target = PassportV2([])
        target.hcl = "123abc"
        self.assertFalse(target.validate_hcl())

    def test_v2_passport_validates_ecl(self):
        target = PassportV2([])
        target.ecl = "brn"
        self.assertTrue(target.validate_ecl())

    def test_v2_passport_fails_ecl(self):
        target = PassportV2([])
        target.ecl = "wat"
        self.assertFalse(target.validate_ecl())

    def test_v2_passport_validates_pid(self):
        target = PassportV2([])
        target.pid = "000000001"
        self.assertTrue(target.validate_pid())

    def test_v2_passport_fails_pid(self):
        target = PassportV2([])
        target.pid = "0123456789"
        self.assertFalse(target.validate_pid())

    def test_v2_invalid_data(self):
        target = PartTwo()
        passports = target.load_data("part_two_invalid.txt")

        self.assertEqual(len(passports), 4)

        for passport in passports:
            self.assertFalse(passport.is_valid())

    def test_v2_valid_data(self):
        target = PartTwo()
        passports = target.load_data("part_two_valid.txt")

        self.assertEqual(len(passports), 4)

        for passport in passports:
            self.assertTrue(passport.is_valid())


if __name__ == "__main__":
    unittest.main()