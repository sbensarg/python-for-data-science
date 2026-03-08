import pandas as pd


def load(path: str):
    """
    load a CSV dataset from the given path.
    """
    try:
        dataset = pd.read_csv(path)
        print(f"loading dataset of dimensions {dataset.shape}")
        return dataset
    except (FileNotFoundError, pd.errors.ParserError, Exception):
        print("error: could not load dataset.")
        return None


def main():
    """
    main function.
    does nothing (required by subject rules).
    """
    pass


if __name__ == "__main__":
    main()
