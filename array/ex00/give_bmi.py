def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("The two lists must be the same size.")

    bmi = []
    for h, w in zip(height, weight):
        bmi_value = w / (h ** 2)
        bmi.append(bmi_value)

    return bmi


def apply_limit(
   bmi: list[int | float],
   limit: int | float
) -> list[bool]:
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list of integers or floats.")

    for i, b in enumerate(bmi):
        if not isinstance(b, (int, float)):
            raise TypeError(
                f"Element at index {i} in bmi is not a number: {b}"
            )

    if not isinstance(limit, (int, float)):
        raise TypeError("limit must be an integer or float.")

    res = []
    for b in bmi:
        res.append(b > limit)

    return res


def main():
    try:
        heights = [1.75, 1.6, 1.8]
        weights = [70, 60, 90]
        limit = 25

        bmi_values = give_bmi(heights, weights)
        print("BMI values:", bmi_values)

        result = apply_limit(bmi_values, limit)
        print("Above limit:", result)

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
