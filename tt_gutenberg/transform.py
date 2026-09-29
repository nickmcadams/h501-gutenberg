from tt_gutenberg.data import load_authors, load_metadata, load_languages

DATA = {
    "authors": load_authors,
    "metadata": load_metadata,
    "languages": load_languages,
}


def get_data():
    """Merge Gutenberg data and add translation counts."""
    authors = DATA["authors"]
    metadata = DATA["metadata"]
    languages = DATA["languages"]

    if callable(authors):
        authors = authors()

    if callable(metadata):
        metadata = metadata()

    if callable(languages):
        languages = languages()

    merged = metadata.merge(
        languages,
        on="gutenberg_id"
    )

    language_counts = merged.groupby(
        "gutenberg_author_id"
    ).size().rename("language_count")

    df = metadata.merge(
        authors,
        on="gutenberg_author_id",
        suffixes=("_metadata", "_author")
    )

    return df.merge(
        language_counts,
        on="gutenberg_author_id"
    )