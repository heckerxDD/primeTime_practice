import random as rd
import numpy as np
import pandas as pd
import string


def gen_data_delay(logic_level):
    cell_delay = np.random.randint(10, 40, size=100) * 0.001
    net_delay = np.random.randint(5, 15, size=100) * 0.001
    total_cell_delay = 0
    total_net_delay = 0
    for lvl in range(logic_level):
        total_cell_delay += rd.choice(cell_delay)
        total_net_delay += rd.choice(net_delay)
    data_delay = total_net_delay + total_cell_delay
    return data_delay


def gen_hierarchy(num):
    letters = string.ascii_lowercase
    LETTERS = string.ascii_uppercase
    pins = "DQE"
    basename = ''.join(rd.choice(letters) for i in range(num))
    dirname = ''.join(rd.choice(LETTERS) for j in range(num))
    full_name = dirname + "/" + basename + "/" + rd.choice(pins)
    return full_name

def main():
    path_count = np.arange(0, 100)
    logic_lvl = np.random.randint(15, 35, size=100)
    data_path_delay = []
    full_name = []
    for x in logic_lvl:
        data_path_delay.append(gen_data_delay(x))
        full_name.append(gen_hierarchy(8))

    paths = pd.DataFrame({
        "path number": path_count,
        "logic level": logic_lvl,
        "data path delay": data_path_delay,
        "start point": full_name
    })

    paths.to_csv("./pt_report_for_plotting")

if __name__ == "__main__":
    main()