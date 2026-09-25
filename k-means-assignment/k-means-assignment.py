def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    result = []
    for p in points:
        best_j = 0
        best_d = sum((a - b) ** 2 for a,b in zip(p, centroids[0]))

        for j in range(1, len(centroids)):
            dist = sum((a - b) ** 2 for a,b in zip(p, centroids[j]))
            if dist < best_d:
                best_d = dist
                best_j = j

        result.append(best_j)

    return result