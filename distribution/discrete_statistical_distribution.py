import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from charting import plot_dsd
table = PrettyTable()
table.field_names = ['value', 'frequency', 'relative frequency']


def discrete_distribution(arr):
    arr.sort()
    unique_elements, frequency = np.unique(arr, return_counts=True)
    n = len(arr)

    relative_frequency = [round(count / n, 4) for count in frequency]
    result =[{"element": elem, "frequency" : count , "relative frequency" : relative_count  }
             for elem, count, relative_count in zip(unique_elements, frequency, relative_frequency)]

    for element in result:
        table.add_row([element["element"], element["frequency"], element["relative frequency"]])
    print(table)
    plot_dsd(unique_elements, relative_frequency)
    table.clear_rows()


    sample_average_value =  round(np.sum(unique_elements * frequency) / n, 3)
    print(f"x_B : {sample_average_value}")
    sample_variance = np.round(np.sum(np.power(unique_elements, 2) * frequency) / n - np.power(sample_average_value, 2), 5)
    print(f"D_b : {sample_variance}")
    standard_deviation_of_the_sample = np.sqrt(sample_variance)
    print(f"σ : {standard_deviation_of_the_sample} ")
    coefficient_of_variation = round(standard_deviation_of_the_sample / sample_average_value *100, 2)
    print(f"V : {coefficient_of_variation} %")
    r = np.max(unique_elements) - np.min(unique_elements)
    print(f"R : {r}")
    return unique_elements ,frequency , sample_average_value





