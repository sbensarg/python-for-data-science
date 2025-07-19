def give_bmi(height: list[int | float], 
             weight: list[int | float]) -> list[int | float]:

    if len(height) != len(weight):
        raise ValueError("The two lists must be the same size.")

    bmi = []

    # Apply BMI = weight / (height^2) for each pair of height and weight
    for h, w in zip(height, weight):
        bmi_value = w / (h ** 2)
        bmi.append(bmi_value)

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list of integers or floats.")

    for i, b in enumerate(bmi):
        if not isinstance(b, (int, float)):
            raise TypeError(f"Element at index {i} in bmi is not a number: {b}")

    if not isinstance(limit, (int, float)):
        raise TypeError("limit must be an integer or float.")

    res = []

    for b in bmi:
        if b > limit:
            res.append(True)
        else:
            res.append(False)

    return res
