import sys


def main():
    # Ensure there are exactly two arguments
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    # Parse the arguments
    s = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    # Split the string into words
    words = s.split()

    # Use list comprehension and lambda to filter words longer than n
    result = list(filter(lambda word: len(word) > n, words))

    # Output the result
    print(result)


if __name__ == "__main__":
    main()
