import sys

if len(sys.argv) != 2:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)
try:
    nbr = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)
if nbr % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
