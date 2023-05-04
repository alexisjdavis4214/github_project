import sys

def caesar_cipher(shift, message):
    # Convert message to uppercase and remove non-alphabetic characters
    message = ''.join(c for c in message.upper() if c.isalpha())

    # Initialize encoded message
    encoded_message = ""

    # Iterate over each character in message
    for c in message:
        # Shift the character by the specified amount
        shifted = chr((ord(c) - 65 + shift) % 26 + 65)
        # Append the shifted character to the encoded message
        encoded_message += shifted

    # Split the encoded message into blocks of five letters
    blocks = [encoded_message[i:i+5] for i in range(0, len(encoded_message), 5)]

    # Print the encoded message in blocks of five letters, ten blocks per line
    for i, block in enumerate(blocks):
        if i % 10 == 9:
            print(block)
        else:
            print(block, end=' ')

if __name__ == "__main__":
    # Read in the shift amount and message from the command line arguments
    shift = int(sys.argv[1])
    message = sys.stdin.readline()

    # Call the caesar_cipher function with the specified shift and message
    caesar_cipher(shift, message)
