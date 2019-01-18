"""A module to test the methods in the Encoder class."""

import unittest

class TestEncoder(unittest.TestCase):
    """A class to test the functionality of the Encoder class."""

    def test_empty_string():
        encoder = Encoder('')
        self.assertEqual(encoder.encode_message(3), '')
        self.assertEqual(encoder.encode_message(14), '')
        self.assertEqual(encoder.encode_message(26), '')

    def test_all_caps():
        encoder = Encoder()

    def test_all_lower():
        encoder = Encoder()

    def test_mixed_case():
        encoder = Encoder()

    def test_mixed_chars():
        encoder = Encoder()


if __name__ == '__main__':
    unittest.main()
