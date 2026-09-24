def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    sums = {}
    c = {}

    for cat, t in zip(categories, targets):
        sums[cat] = sums.get(cat, 0.0) + t
        c[cat] = c.get(cat, 0) + 1

    means = {cat: sums[cat] / c[cat] for cat in sums}
    return [means[cat] for cat in categories]