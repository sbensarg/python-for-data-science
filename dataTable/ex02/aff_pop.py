import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value):
    """
    Convert population strings like:
    '2.5M' -> 2500000
    '300K' -> 300000
    """
    if isinstance(value, str):
        value = value.strip()
        if value.endswith("M"):
            return float(value[:-1]) * 1_000_000
        elif value.endswith("K"):
            return float(value[:-1]) * 1_000
    try:
        return float(value)
    except Exception:
        return 0.0


def main():
    try:
        dataset = load("population_total.csv")
        if dataset is None:
            return

        # Choose countries to compare
        country1 = "Morocco"
        country2 = "France"

        country1_data = dataset[dataset["country"] == country1]
        country2_data = dataset[dataset["country"] == country2]

        if country1_data.empty or country2_data.empty:
            print("Country not found in dataset.")
            return

        # Select years between 1800 and 2050
        years = [int(col) for col in dataset.columns[1:]
                 if 1800 <= int(col) <= 2050]

        # Extract and clean population data
        pop1 = country1_data.loc[:, map(str, years)] \
                            .iloc[0] \
                            .apply(convert_population)

        pop2 = country2_data.loc[:, map(str, years)] \
                            .iloc[0] \
                            .apply(convert_population)

        plt.figure(figsize=(10, 6))

        plt.plot(years, pop1, label=country1)
        plt.plot(years, pop2, label=country2)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        # Population axis format
        plt.yticks(
            [20_000_000, 40_000_000, 60_000_000],
            ["20M", "40M", "60M"]
        )

        plt.legend(loc="lower right")
        plt.grid(True)

        plt.xticks(range(1800, 2051, 50))

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
