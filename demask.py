import os
import pandas as pd
import numpy as np
import base64
from PIL import Image

path_root  = r"C:\\Users\\barya\\Downloads\\ex2"

img_root = r"C:\\Users\\barya\\Downloads\\ex2\\noised_img.png"

noise_root = r"C:\\Users\\barya\\Downloads\\ex2\\mysterious_file.npz"

noise = np.load(noise_root)

img = np.asarray(Image.open(img_root))

real_img = img - noise['arr_0']

real_img = Image.fromarray(real_img)

real_img.save(f"{path_root}\\uncover.png")