import numpy as np
from prettytable import PrettyTable
from charting import plot_isd
def check(x, num1, num2):
    return num1 < x < num2

def table_print(values, counts, w, check_last_val):
    table.field_names = ["Інтервали", "n*_i", "w*_i / h"]
    for i in range(np.size(counts-1)):
        if i == 0:
            table.add_row([f"[{values[i]}; {values[i+1]})", counts[i], w[i]], divider=True)
        elif i == np.size(counts-2):
            table.add_row([f"[{values[i]}; {values[i+1]}{']' if check_last_val else ')'}", counts[i], w[i]],
                          divider=True)
            break
        else:
            table.add_row([f"({values[i]}; {values[i+1]})", counts[i], w[i]], divider=True)
    print(table)
    table.clear_rows()

table = PrettyTable()
def interval_sampling_distribution(arr):
    values, counts = np.unique(arr, return_counts=True)
    check_last_val = True
    n = len(arr)
    k = round(np.sqrt(n))
    h = round((np.max(arr) - np.min(arr)) / (5 * np.log10(n)), 6)

    arr.sort()
    intervals = [round(arr[0] + i * h, 3) for i in range(k + 1)]

    # Якщо останнє значення не охоплене, додаємо ще один інтервал
    if intervals[-1] < arr[-1]:
        intervals.append(round(intervals[-1] + 0.5*h, 3))
        check_last_val = False

    n_data = np.array([])
    num = 0
    saved = 0
    flag = 0

    for i in range(np.size(intervals) - 1):
        for j in range(flag, np.size(values)):
            if check(values[j], intervals[i], intervals[i + 1]) or j == 0 or j == np.size(values) - 1:
                num += counts[j]
                continue
            elif values[j] == intervals[i] or values[j] == intervals[i + 1]:
                j1 = round(counts[j] / 2)
                j2 = counts[j] - j1
                saved = max(j1, j2)
                num += min(j1, j2)
                flag = j + 1
            else:
                flag = j
            break
        n_data = np.append(n_data, num)
        num *= 0
        num += saved
        saved *= 0
    density = []

    for i in n_data:
        density.append(round(i / (n * h), 4))

    table_print(intervals, n_data, density, check_last_val)
    plot_isd(intervals, density)

    return intervals, n_data, n, h
