from tt_gutenberg import data as DATA


def get_data():
    """Merge Gutenberg data and add translation counts."""
    authors = DATA.load_authors()
    metadata = DATA.load_metadata()
    languages = DATA.load_languages()

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