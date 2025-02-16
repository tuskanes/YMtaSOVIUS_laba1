import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def table_print_discrete(x_val, y_val):
    table = PrettyTable()
    table.field_names = ["x", "F*(x)"]
    table.add_row([f"x <= {x_val[0]}", y_val[0]], divider=True)
    for i in range(np.size(x_val)-1):
        table.add_row([f"{x_val[i]} < x <= {x_val[i+1]}", y_val[i+1]], divider=True)
    table.add_row([f"x > {x_val[np.size(x_val)-1]}", y_val[np.size(y_val)-1]], divider=True)
    print(table)

def table_print_interval(x_val, y_val):
    table = PrettyTable()
    table.field_names = ["x", "F*(x)"]
    for i in range(np.size(y_val)):
        table.add_row([f"x = {x_val[i]}", y_val[i]], divider=True)
    print(table)

def empirical_distribution_function(x_i, n_data_discrete, intervals, n_data_intervals, n):
    ####Функціональний ряд для дискретного#############
    n_data_discrete = np.insert(n_data_discrete, 0, 0)
    y_values = []
    sum = 0
    for i in range(len(n_data_discrete)-1):
        sum += n_data_discrete[i]
        y_values.append(round(sum/n,3))

    y_values.append(1)
    table_print_discrete(x_i, y_values)

    x_values = np.insert(x_i, 0, x_i[0] - 0.1)
    last_x_value = x_values[-1] + (x_values[-1] * 0.1)
    first_x_value = x_values[0] - 0.5
    x = np.concatenate(([first_x_value], x_values, [last_x_value]))
    y = np.concatenate(([0], y_values, [1.0]))

    # Побудова графіка
    plt.step(x, y, where='post', label='F*(x)', color='darkblue')
    # Налаштування графіка
    plt.title('Графік функції F*(x)')
    plt.xlabel('x')
    plt.ylabel('F*(x)')
    plt.grid(True)
    plt.legend()
    print(len(intervals))
    print(len(n_data_intervals))
    #######Функціональний ряд для інтервального#######
    y_values_for_interval = []
    sum_for_intervals = 0
    for i in range(len(intervals)):
        if i == 0:
            y_values_for_interval.append(0)
        else:
            sum_for_intervals += n_data_intervals[i - 1]
            y_values_for_interval.append(sum_for_intervals / n)
    table_print_interval(intervals, y_values_for_interval)
    plt.plot(intervals, y_values_for_interval,linestyle='--',)
    plt.scatter(intervals, y_values_for_interval)
    plt.show()


    return y_values_for_interval