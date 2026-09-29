from tt_gutenberg.data import load_authors, load_metadata


def get_data():
    """Merge Gutenberg author and metadata datasets."""
    authors = load_authors()
    metadata = load_metadata()

    return metadata.merge(
        authors,
        on="gutenberg_author_id",
        suffixes=("_metadata", "_author")
    )