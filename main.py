from prettytable import PrettyTable
from mode import *
from data import *
from control_card import control_card
from distribution.discrete_statistical_distribution import discrete_distribution
from distribution.interval_distribution import interval_sampling_distribution
from distribution.empirical_functions import empirical_distribution_function

datas = [A_arr, B_arr, C_arr, D_arr, E_arr]
x_b = []
for data in datas:
    values, counts = np.unique(data, return_counts=True)
    table = PrettyTable()
    table.field_names = ["Унікальне значення", "Кількість"]
    for i in range(np.size(values)):
        table.add_row([values[i], counts[i]], divider=True)
    print(table)



    x_i, n_data_discrete, sample_average_value = discrete_distribution(data)
    mode_dsd(data)
    median_dsd(x_i)
    x_b.append(sample_average_value)
    intervals, n_data_intervals, n, h = interval_sampling_distribution(data)
    y_values_for_interval = empirical_distribution_function(x_i, n_data_discrete, intervals, n_data_intervals, n)

    mode_isd(intervals, n_data_intervals, h)
    median_isd(y_values_for_interval, intervals, h)
    print("####################################################")


T_nom = 50
standard_deviation = 2.5
n = 75
control_card(x_b, T_nom, standard_deviation, n)
