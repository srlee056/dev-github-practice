import unittest
import dec_to_hex as dh


class TestDecimalToHexadecimal(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(dh.decimal_to_hexadecimal(16), "10")

    def test_negative_integer(self):
        self.assertEqual(dh.decimal_to_hexadecimal(-16), "-10")

    def test_zero(self):
        self.assertEqual(dh.decimal_to_hexadecimal(0), "0")

    def test_large_number(self):
        self.assertEqual(dh.decimal_to_hexadecimal(255), "ff")

    def test_large_negative_number(self):
        self.assertEqual(dh.decimal_to_hexadecimal(-255), "-ff")


if __name__ == "__main__":
    unittest.main()
