import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    display life expectancy graph for Morocco.
    """
    try:
        dataset = load("life_expectancy_years.csv")
        if dataset is None:
            return

        country_data = dataset[dataset["country"] == "Morocco"]

        if country_data.empty:
            print("country not found")
            return

        # Years columns (exclude 'country')
        years = dataset.columns[1:].astype(int)

        life_expectancy = country_data.iloc[0, 1:].astype(float)

        plt.figure(figsize=(8, 5))
        plt.plot(years, life_expectancy)

        plt.title("Life Expectancy in Morocco")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")

        plt.yticks(range(20, 91, 10))

        # Display 8 ticks increasing by ~40 years
        start_year = int(years.min())
        end_year = int(years.max())

        ticks = list(range(start_year, end_year + 1, 40))[:8]
        plt.xticks(ticks)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("an unexpected error occurred:", e)


if __name__ == "__main__":
    main()
