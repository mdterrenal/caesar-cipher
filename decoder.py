"""A module that contains a class that decodes messages
encrypted with Caesar cipher."""


class Decoder:
    """A class that allows functionality for decoding messages."""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, message):
        """Initialize an instance of Decoder with a message."""

        self.message = message.upper()

    def decode_message(self, key):
        """Decode the message given the key used to encode it.

        Decrypt the message by shifting characters by key towards
        the letter A, wrapping around to Z if necessary.
        """

        decoded_message = ''
        for char in self.message:
            if char.isalpha():
                decoded_char = self.convert_char(char, key)
                decoded_message = decoded_message + decoded_char
            else:
                decoded_message = decoded_message + char
        return decoded_message

    def convert_char(self, char, key):
        return Decoder.alphabet[(Decoder.alphabet.index(char) - key) % 26]
