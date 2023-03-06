from PIL import Image
import numpy as np

path_root  = r"C:\\Users\\barya\\Downloads\\ex2"

img_root = r"C:\\Users\\barya\\Downloads\\ex2\\hacker_note.png"

img = np.asarray(Image.open(img_root))

random_noise_agg = None
flag = False
for x in  range(1,70):
    random_noise = np.random.rand(*img.shape)

    random_noise[:,:,0] = (random_noise[:,:,0] * 510) - 255
    random_noise[:,:,1] = (random_noise[:,:,1] * 330) - 260
    random_noise[:,:,2] = (random_noise[:,:,2] * 390) - 120
    random_noise[:,:,3] = (random_noise[:,:,3] * 400) - 255
    if not flag:
        random_noise_agg = random_noise
        flag = True
    else: 
        random_noise_agg += random_noise

random_noise = random_noise_agg

noised_img = img - random_noise

clipped = np.clip(noised_img, 1 , 254).round().astype(np.uint8)


im_noised = Image.fromarray(clipped)

real_noise = clipped - img

im_noised.save(f"{path_root}\\noised_img.png")

np.savez(f"{path_root}\\mysterious_file.npz", real_noise)








