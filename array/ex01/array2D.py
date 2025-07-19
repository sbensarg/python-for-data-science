import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array (list of lists) using NumPy from the start index to the end index.
    Prints the original shape and the new shape after slicing.

    Args:
        family (list): The 2D list to slice.
        start (int): The start index.
        end (int): The end index.

    Returns:
        list: The sliced 2D list.

    Raises:
        TypeError: If family is not a list of lists or is not rectangular.
        ValueError: If inner lists are not all of the same length.
    """
    # isinstance built-in function used for type checking

    if not isinstance(family, list):
        raise TypeError("family must be a list.")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("Each element of family must be a list.")
    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("All rows must have the same length.")

    array = np.array(family)
    print(f"My shape is : {array.shape}")
    sliced = array[start:end]
    print(f"My new shape is : {sliced.shape}")
    return sliced.tolist()
