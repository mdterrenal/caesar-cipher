"""A module to test the methods in the Decoder class."""

import unittest
from decoder import Decoder


class TestDecoder(unittest.TestCase):
    """A class to test the functionality of the Decoder class."""

    def test_empty_string(self):
        decoder = Decoder('')
        self.assertEqual(decoder.decode_message(3), '')
        self.assertEqual(decoder.decode_message(14), '')
        self.assertEqual(decoder.decode_message(26), '')

    def test_all_caps(self):
        decoder = Decoder()

    def test_all_lower(self):
        decoder = Decoder()

    def test_mixed_case(self):
        decoder = Decoder()

    def test_mixed_chars(self):
        decoder = Decoder()


if __name__ == '__main__':
    unittest.main()
