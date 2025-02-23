def is_utf8(filename):
    """Check if a file is UTF-8 encoded."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            f.read()
        return True
    except UnicodeDecodeError:
        return False