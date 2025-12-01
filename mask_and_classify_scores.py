import numpy as np


def mask_and_classify_scores(arr):

    if type(arr) != np.ndarray or arr.ndim != 2 or arr.shape[0] < 4 or arr.shape[0] != arr.shape[1]:
        return None

    # Part A
    cleaned = arr.copy()
    cleaned[arr<0] = 0
    cleaned[arr>100] = 100

    # Part B
    levels = cleaned.copy()
    levels[levels < 40] = 0
    levels[(levels >= 40) & (levels < 70)] = 1
    levels[levels >= 70] = 2

    # Part C
    row_pass_counts = np.empty(arr.shape[0])

    for idx, row in enumerate(cleaned):
        entry = 0
        for j in row:
            if j >= 50:
                entry += 1
        row_pass_counts[idx] = entry

    return cleaned, levels, row_pass_counts