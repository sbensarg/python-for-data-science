import sys

# Define the Morse code dictionary
NESTED_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", " ": "/"
}


def encode_to_morse(input_string):
    """Encodes a string into Morse code."""
    for char in input_string:
        if char.upper() not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")

    morse_code = "".join(
        NESTED_MORSE[char.upper()] + " " for char in input_string
    ).strip()
    return morse_code


def main():
    """Main function to process command-line arguments."""
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    input_string = sys.argv[1]

    if not isinstance(input_string, str):
        raise AssertionError("the arguments are bad")

    try:
        print(encode_to_morse(input_string))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
