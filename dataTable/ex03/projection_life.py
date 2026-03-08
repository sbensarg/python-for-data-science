import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    display life expectancy vs GDP per capita
    for the year 1900.
    """
    try:
        income = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        life = load("life_expectancy_years.csv")

        if income is None or life is None:
            return

        year = "1900"

        data = income[["country", year]].merge(
            life[["country", year]],
            on="country",
            suffixes=("_gdp", "_life")
        )

        gdp = data[f"{year}_gdp"].astype(float)
        life_exp = data[f"{year}_life"].astype(float)

        plt.figure(figsize=(10, 6))

        plt.scatter(gdp, life_exp)

        # log scale for GDP
        plt.xscale("log")

        # custom xaxis ticks
        plt.xticks(
            [300, 1000, 10000],
            ["300", "1k", "10k"]
        )

        # top title
        plt.title("1900")

        # bottom X label
        plt.xlabel("Gross Domestic Product")

        # y axis
        plt.ylabel("Life Expectancy (Years)")

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("an unexpected error occurred:", e)


if __name__ == "__main__":
    main()
