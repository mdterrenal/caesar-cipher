"""A module to test the methods in the Encoder class."""

import unittest
from encoder import Encoder


class TestEncoder(unittest.TestCase):
    """A class to test the functionality of the Encoder class."""

    def test_empty_string(self):
        encoder = Encoder('')
        self.assertEqual(encoder.encode_message(3), '')
        self.assertEqual(encoder.encode_message(14), '')
        self.assertEqual(encoder.encode_message(26), '')

    def test_all_caps(self):
        encoder = Encoder('HELLO')
        self.assertEqual(encoder.encode_message(2), 'JGNNQ')

    def test_all_lower(self):
        encoder = Encoder('hello')
        self.assertEqual(encoder.encode_message(2), 'JGNNQ')

    def test_mixed_case(self):
        encoder = Encoder('hElLo')
        self.assertEqual(encoder.encode_message(2), 'JGNNQ')

    def test_mixed_chars(self):
        encoder = Encoder('he ll o!')
        self.assertEqual(encoder.encode_message(2), 'JG NN Q!')

if __name__ == '__main__':
    unittest.main()
