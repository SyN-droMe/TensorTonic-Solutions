def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    result = list(series)
    for _ in range(order):
        result = [result[i] - result[i - 1] for i in range(1, len(result))]

    return result