from tt_gutenberg.transform import get_data

def list_authors(by_languages=False, alias=False):
    """Return a list of Gutenberg authors."""
    df = get_data()
    if "translation_count" not in df.columns:
        translation_counts = (
            df.groupby("author_alias")
            .size()
            .rename("translation_count")
        )

        df = df.merge(
            translation_counts,
            on="author_alias"
        )

    df = df.sort_values("translation_count", ascending=False)
    
    if alias:
        return df["author_alias"].dropna().tolist()

    return df["gutenberg_author_id"].tolist()