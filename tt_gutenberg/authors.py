from tt_gutenberg.data import load_authors, load_languages, load_metadata

def list_authors(by_languages=False, alias=False):
    """Return a list of Gutenberg authors."""
    df = load_authors()
    metadata = load_metadata()
    languages = load_languages()
    merged = metadata.merge(languages, on="gutenberg_id")
    language_counts = merged.groupby("gutenberg_author_id").size()
    df = df.merge(
    language_counts.rename("language_count"),
    on="gutenberg_author_id"
    )
    df = df.sort_values("language_count", ascending=False)

    if alias:
        return df["alias"].dropna().tolist()

    return df["gutenberg_author_id"].tolist()