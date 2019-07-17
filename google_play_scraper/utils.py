def nested_lookup(source, indexes):
    if len(indexes) == 1:
        return source[indexes[0]]
    return nested_lookup(source[indexes[0]], indexes[1::])
