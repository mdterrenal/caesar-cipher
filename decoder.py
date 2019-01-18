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

        decode_message = [alphabet[(alphabet.index(char) - key) % 26]
                          for char in self.message]
        return ''.join(decode_message)
