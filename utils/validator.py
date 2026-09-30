def is_valid_row(row):
    for value in row:
        if value is None:
            return False
    return True
