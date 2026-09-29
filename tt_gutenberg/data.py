import pandas as pd


def load_authors():
    """Load the Gutenberg authors dataset."""
    url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_authors.csv"
    )
    return pd.read_csv(url)

def load_metadata():
    """Load the Gutenberg metadata dataset."""
    url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_metadata.csv"
    )
    return pd.read_csv(url)


def load_languages():
    """Load the Gutenberg languages dataset."""
    url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_languages.csv"
    )
    return pd.read_csv(url)
