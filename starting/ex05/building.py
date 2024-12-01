import sys
import string


def count_character_types(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    punctuation = sum(1 for char in text if char in string.punctuation)
    spaces = sum(1 for char in text if char.isspace())
    digits = sum(1 for char in text if char.isdigit())
    total = len(text)
    return total, upper, lower, punctuation, spaces, digits


def main():
    args = sys.argv[1:]

    if len(args) > 1:
        raise AssertionError(
            "Too many arguments. Please provide only one string argument."
        )

    if len(args) == 0:
        text = input("What is the text to count?\n")
    else:
        text = args[0]

    total, upper, lower, punctuation, spaces, digits = (
        count_character_types(text)
    )

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
