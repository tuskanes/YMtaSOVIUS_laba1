import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import label


def control_card(x_b, T_nom, standard_deviation, n):

    plt.plot(x_b, marker= 'o', linestyle = '-', color = 'red')
    plt.axhline(y =T_nom, color = 'green', linestyle = '--', label = 'Середнє')
    plt.axhline(y=T_nom + 2 * standard_deviation / np.sqrt(n), color='y', linestyle='--', label='+2σ')
    plt.axhline(y=T_nom - 2 * standard_deviation / np.sqrt(n), color='y', linestyle='--', label='-2σ')
    plt.axhline(y =T_nom + 3 * standard_deviation / np.sqrt(n), color='b', linestyle= '--', label='+3σ')
    plt.axhline(y =T_nom - 3 * standard_deviation / np.sqrt(n), color='b', linestyle= '--', label='-3σ')
    plt.legend()
    plt.xlabel('Номер вибірки')
    plt.show()
