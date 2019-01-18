"""A module containing a class that encodes messages."""


class Encoder:
    """A class that allows functionality for encoding messages."""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, message):
        """Initialize an instance of Encoder with a message."""

        self.message = message.upper()

    def encode_message(self, key):
        """Modify message by encrypting it using cipher.

        Encrypt the message by shifting characters by key towards
        the letter Z, wrapping around to A if necessary.
        """

        encoded_message = ''
        for char in self.message:
            if char.isalpha():
                encoded_char = self.convert_char(char, key)
                encoded_message = encoded_message + encoded_char
            else:
                encoded_message = encoded_message + char
        return encoded_message

    def convert_char(self, char, key):
        return Encoder.alphabet[(Encoder.alphabet.index(char) + key) % 26]
