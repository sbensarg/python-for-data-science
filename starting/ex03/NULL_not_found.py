def NULL_not_found(object) -> int:
    # Define the dictionary of null-like objects and their descriptions
    my_dict = {
        "Nothing": None,
        "Cheese": float("NaN"),
        "Zero": 0,
        "Empty": "",
        "Fake": False,
    }

    # Check if the object matches one of the keys in the dictionary
    for description, key in my_dict.items():
        if (
            (key is None and object is None)
            or (key != key and object != object)  # NaN comparison
            or (object is key)  # Exact match using `is`
        ):
            print(f"{description}: {object} {type(object)}$")
            return 1

    # If no match is found, print "Type not Found"
    print("Type not Found$")
    return 1
