def ft_filter(function, iterable):
    """
    Construct an iterator from those elements of iterable for which function returns true.
    If function is None, return the items that are true.
    """
    if function is None:
        return (item for item in iterable if item)  # Only truthy items
    return (item for item in iterable if function(item))  # Filtered items
