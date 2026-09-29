from tt_gutenberg.data import load_authors, load_metadata, load_languages

DATA = {
    "gutenberg_authors": load_authors,
    "gutenberg_metadata": load_metadata,
    "gutenberg_languages": load_languages,
}


def get_data():
    """Merge Gutenberg data and add translation counts."""
    authors = DATA["gutenberg_authors"]()
    metadata = DATA["gutenberg_metadata"]()
    languages = DATA["gutenberg_languages"]()

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