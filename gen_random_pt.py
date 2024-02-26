import pandas as pd
import numpy as np
import random as rd
import string


path_count = np.arange(0, 1000, dtype=np.int32)  # example contains 1000 timing paths with random attributes
pre_slack = np.random.randint(0, 30, size=1000, dtype=np.int32) * -0.001
# demonstrates previous cycle path timing violations
cur_slack = np.random.randint(0, 30, size=1000, dtype=np.int32) * -0.001
# demonstrates current cycle path timing violation
post_slack = np.random.randint(0, 30, size=1000, dtype=np.int32) * -0.001
# demonstrates next cycle path timing violation

pre_logic_lvl = np.random.randint(15, 30, size=1000, dtype=np.int32)
cur_logic_lvl = np.random.randint(15, 30, size=1000, dtype=np.int32)
post_logic_lvl = np.random.randint(15, 30, size=1000, dtype=np.int32)  # demonstrates typical logic levels

pre_data_delay = np.random.randint(250, 450, size=1000, dtype=np.int32) * -0.001
cur_data_delay = np.random.randint(250, 450, size=1000, dtype=np.int32) * -0.001
post_data_delay = np.random.randint(250, 450, size=1000, dtype=np.int32) * -0.001
# demonstrates typical data path delays

clock_skew = np.random.randint(20, 80, size=1000, dtype=np.int32) * 0.001
# demonstrates typical clock skews between launching flop and capturing flop

chars = string.ascii_lowercase + string.digits
startpoint = [''.join(rd.choice(chars) for i in range(10)) for j in range(1000)]
endpoint = [''.join(rd.choice(chars) for m in range(10)) for n in range(1000)][::-1]
np_startpoint = np.array(startpoint)
np_endpoint = np.array(endpoint)
# represents typical startpoint and endpoint

paths = pd.DataFrame({
    'pre_slack': pre_slack,
    'cur_slack': cur_slack,
    'post_slack': post_slack,
    'pre_logic_lvl': pre_logic_lvl,
    'cur_logic_lvl': cur_logic_lvl,
    'post_logic_lvl': post_logic_lvl,
    'pre_data_delay': pre_data_delay,
    'cur_data_delay': cur_data_delay,
    'post_data_delay': post_data_delay,
    'clock_skew': clock_skew,
    'startpoint': startpoint,
    'endpoint': endpoint
})
paths.to_csv('./path_info_example.csv')