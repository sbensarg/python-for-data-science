def NULL_not_found(object) -> int:
    # Define the dictionary of null-like objects and their descriptions
    my_dict = {
        None: "Nothing",
        float("NaN"): "Cheese",
        0: "Zero",
        "": "Empty",
        False: "Fake"
    }

    # Check if the object matches one of the keys in the dictionary
    for key, description in my_dict.items():
        # We use 'is' for None because '==' may not work well with NaN
        if (key is None and object is None) or (key != key and object != object) or (object == key):
            print(f"{description}: {object} <{type(object)}>")
            return 1
    
    # If no match is found, print "Type not found"
    print("Type not found")
    return 0
    