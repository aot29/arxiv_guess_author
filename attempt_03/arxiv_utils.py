def flatten(xss):
    """Flatten a list of lists"""
    return [x for xs in xss for x in xs]

def get_unique_authors(df):
    """Given a dataframe, return unique authors"""
    authors = flatten(df['authors_parsed'])
    return set(authors)

def count_authors(df):
    """Given a dataframe, return count of unique authors"""
    return len(get_unique_authors(df))