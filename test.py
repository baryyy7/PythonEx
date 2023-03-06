import os
import pandas as pd
import numpy as np
import base64
import random
import pickle

from datetime import datetime
import time 


covid_root = r"C:\\Users\\barya\\Downloads\\covid"
orig = r"C:\\Users\\barya\\Downloads\\orig"
ex_3 = r"C:\\Users\\barya\\Downloads\\ex3"



filenames_columns_to_random_dict = {}
index = 0
total_num_dicts = 150
fake_dicts_list = [{} for i in range (total_num_dicts)]

for filename in os.listdir(covid_root):
    filepath = f"{covid_root}\\{filename}"
    print(filename)
    if(not filename.endswith('.csv')):
        continue
    df : pd.DataFrame = pd.read_csv(filepath)
    for column in df.columns:

        # b 32 encrypt the columns
        encoded_col =  str(base64.b32encode(bytes(column, 'utf-8'))) # bytes
        encoded_col = encoded_col[2:-1]
        # base64.b32encode(bytearray(encoded_col, 'ascii')).decode('utf-8')

        col_dir_path = f"{orig}\\{encoded_col}"
        if(not os.path.exists(col_dir_path)):
            os.makedirs(col_dir_path)
        np_col : np.ndarray= df[column]

        filename_no_csv_suffix = filename.replace('.csv','')
        
        datetime_object = datetime.strptime(filename_no_csv_suffix, '%m-%d-%Y')
        random_addition_to_time = random.randint(814812693, 919912693)
        origin_time = datetime_object.timestamp()

        moved_time = origin_time - random_addition_to_time

        randomized_timestamp = int(moved_time)

        np.savez(f"{col_dir_path}\\{randomized_timestamp}_{index}", np_col)
        if encoded_col not in filenames_columns_to_random_dict: 
            filenames_columns_to_random_dict[encoded_col] = {}
        filenames_columns_to_random_dict[encoded_col][index] = random_addition_to_time

        for i in range(len(fake_dicts_list)):
            cur_dict = fake_dicts_list[i]
            if encoded_col not in cur_dict: 
                cur_dict[encoded_col] = {}
                cur_dict[encoded_col][index] = index * random.randint(12693,312693) * - 1
        
        index += 1





for i in range(total_num_dicts):
    path = f"{ex_3}\\{i}"
    if(not os.path.exists):
        os.mkdir(path)
    if (i == 6):
        with open(f"{path}\\{i}.pkl", 'wb') as handle:
            pickle.dump(filenames_columns_to_random_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        with open(f"{path}\\{i}.pkl", 'wb') as handle:
            pickle.dump(fake_dicts_list[i], handle, protocol=pickle.HIGHEST_PROTOCOL)



