import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from sympy import symbols
from sympy.abc import sigma
from sympy.printing.pretty import pretty
from sympy import latex


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
    fig, ax = plt.subplots()

    ax.plot(unique_elements, relative_frequency, color='darkblue')
    ax.scatter(unique_elements, relative_frequency)
    ax.set_title('Frequency polygon')
    ax.set_xlabel('xi')
    ax.set_ylabel('w')
    print(table)
    plt.grid(True)
    plt.show()

    sample_average_value =  round(np.sum(unique_elements * frequency) / n, 3)
    print(f"x_B : {sample_average_value}")
    sample_variance = np.round(np.sum(np.power(unique_elements, 2) * frequency) / n - np.power(sample_average_value, 2), 5)
    print(f"D_b : {sample_variance}")
    standard_deviation_of_the_sample = np.sqrt(sample_variance)
    print(f"sigma : {standard_deviation_of_the_sample} ")
    coefficient_of_variation = round(standard_deviation_of_the_sample / sample_average_value *100, 2)
    print(f"V : {coefficient_of_variation}")

    return unique_elements ,frequency , sample_average_value





