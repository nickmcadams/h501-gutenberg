from tt_gutenberg.transform import get_data

def list_authors(by_languages=False, alias=False):
    """Return a list of Gutenberg authors."""
    df = get_data()
    df = df.sort_values("language_count", ascending=False)

    if alias:
        return df["alias"].dropna().tolist()

    return df["gutenberg_author_id"].tolist()