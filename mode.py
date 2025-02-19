import numpy as np
import statistics

def mode_dsd(arr):
    reversed_arr = arr[::-1]
    Mo1 = statistics.mode(arr)
    Mo2 = statistics.mode(reversed_arr)
    if Mo1 == Mo2:
        print(f"Mo* (для дискретного розподілу вибірки) = {Mo1}")
    else:
        print(f"Mo* (для дискретного розподілу вибірки) = {Mo1} , {Mo2}")


def mode_isd(intervals, n_data, h):
    max_val = max(n_data)
    indeces = np.where(n_data == max_val)[0]

    n_Mo = 0
    for i in indeces:
        n_Mo += n_data[i]

    first_i = indeces[0]
    x_i1 = intervals[first_i]

    mode = x_i1 + h*((max_val - n_data[first_i-1]) / (2*max_val - n_data[first_i-1] - n_data[first_i+1]))
    print(f"Mo* (для інтегрального розподілу вибірки) = {round(mode, 3)}")


def median_dsd(arr):
  print(f"Me* (для дискретного розподілу вибірки) = "
        f"{statistics.median(arr)}")


def median_isd(empir, intervals, h):
    median = 0
    for i in range(np.size(empir)):
        if empir[i] < 0.5 < empir[i + 1]:
            median = (intervals[i] + (h * (0.5 - empir[i]) /
                      (empir[i + 1] - empir[i])))
            break

    print(f"Me* (для інтегрального розподілу вибірки) = {round(median, 3)}")


