from tt_gutenberg.transform import get_data

def list_authors(by_languages=False, alias=False):
    """Return a list of Gutenberg authors."""
    df = get_data()

    translation_counts = (
        df.groupby("gutenberg_author_id")
        .size()
        .rename("translation_count")
    )

    df = df.merge(
        translation_counts,
        on="gutenberg_author_id"
    )

    df = df.sort_values("translation_count", ascending=False)
    if alias:
        return df["author_alias"].dropna().tolist()

    return df["gutenberg_author_id"].tolist()