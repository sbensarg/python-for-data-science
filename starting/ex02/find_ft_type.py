def all_thing_is_obj(object: any) -> int:
    # List to store known types
    known_types = ['list', 'tuple', 'set', 'dict', 'str']

    # Get the type name of the object
    obj_type = type(object).__name__

    # Print type information for specific types
    if obj_type == 'str':
        print(f"{object} is in the kitchen : {type(object)}")
    elif obj_type in known_types:
        print(f"{obj_type.capitalize()} : {type(object)}")
    else:
        print("Type not found")

    return 42
