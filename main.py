"""Module that represents the main program."""

from encoder import Encoder
from decoder import Decoder


def start_cipher():
    """Begin the cipher by asking some quick questions.

    Ask if the user wants to encode or decode the message and
    retrieve the message.
    """

    encode_or_decode = input('Welcome to the Caesar Cipher program. Would '
                             'you like me to encode or decode a message? ')
    encode_or_decode = encode_or_decode.strip().lower()
    while encode_or_decode != 'encode' and encode_or_decode != 'decode':
        encode_or_decode = input('That is not a valid response. '
                                 'Please try again. ')
        encode_or_decode = encode_or_decode.strip().lower()
    message = input('Wonderful. What message would you like me to use? ')
    if encode_or_decode in 'encode':
        encoder = Encoder(message)
    else:
        decoder = Decoder(message)


if __name__ == '__main__':
    start_cipher()
