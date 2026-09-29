from tt_gutenberg.data import load_authors, load_metadata


DATA = None


def get_data():
    """Merge Gutenberg authors and metadata datasets."""
    if isinstance(DATA, dict):
        frames = list(DATA.values())
        authors = frames[0]
        metadata = frames[1]
    else:
        authors = load_authors()
        metadata = load_metadata()

    df = metadata.merge(
    authors,
    on="gutenberg_author_id",
    suffixes=("_metadata", "_author")
    )

    df = df.rename(columns={"alias": "author_alias"})

    return df