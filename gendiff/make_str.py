def make_str(value):
    """Casts None to null, bool to str"""
    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    return value
