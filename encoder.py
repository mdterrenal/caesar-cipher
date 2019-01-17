"""A module containing a class that encodes messages."""


class Encoder:
    """A class that allows functionality for encoding messages."""

    def __init__(self, message):
        """Initialize an instance of Encoder with a message."""

        self.message = message.upper()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encode_message(self, key):
        """Modify message by encrypting it using cipher.

        Encrypt the message by shifting characters by key towards
        the letter Z, wrapping around to A if necessary.
        """

        encode_message = [self.alphabet[(self.alphabet.index(char) + key) % 26]
                          for char in self.message]
        return ''.join(encode_message)
