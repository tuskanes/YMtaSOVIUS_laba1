import matplotlib.pyplot as plt
import numpy as np

def plot_dsd(values, w):
    fig, ax = plt.subplots()

    ax.plot(values, w, color='darkblue')
    ax.scatter(values, w),
    ax.set_title("Графік відносних частот")
    ax.set_xlabel("x_i")
    ax.set_ylabel("w")
    plt.grid(True)
    plt.show()


def plot_isd(values, w_div_h):
    bin_widths = np.diff(values)
    plt.bar(values[:-1], w_div_h, width=bin_widths, align='edge', color='darkblue', edgecolor='black')

    plt.title('Гістограма')
    plt.xlabel('$x_i$')
    plt.ylabel('$w_i$h')
    plt.grid(True)
    plt.show()


def plot_empir(x, y, intervals, y_values_for_interval):
    # Стрілки
    for i in range(1, len(x)):
        plt.arrow(x[i - 1], y[i - 1], x[i] - x[i - 1], 0, head_width=0.015625, head_length=(x[i - 1] - x[i]) + 0.01,
                  fc='blue', ec='blue')

    plt.step(x, y, where='post', label='F*(x)', color='darkblue')

    plt.title('Графік емпіричної функції')
    plt.xlabel('x')
    plt.ylabel('F*(x)')
    plt.grid(True)
    plt.legend()

    plt.plot(intervals, y_values_for_interval,linestyle='--', color='red')
    plt.scatter(intervals, y_values_for_interval)
    plt.show()