import os
import pandas as pd
import numpy as np
import base64
import random
import pickle

from datetime import datetime
import time 

covid_root = r"C:\\Users\\barya\\Downloads\\covid"
ex1 = r"C:\\Users\\barya\\Downloads\\ex1"
ex_3 = r"C:\\Users\\barya\\Downloads\\ex3"


file_dir = f"{ex_3}\\{6}"
file_path = f"{file_dir}\\6.pkl"
with open(file_path,'rb') as o_file:
    loaded_dict = pickle.load(o_file)

some_noise = loaded_dict['INXW4ZTJOJWWKZA='][861]

date_file_noised = f"725915551_861"

epoch_after_reduction = int(date_file_noised.split('_')[0])

orig_epoch = epoch_after_reduction + some_noise

print(orig_epoch)

# dtime = datetime(orig_epoch)

# print(dtime)