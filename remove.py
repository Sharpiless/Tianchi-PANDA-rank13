import os
from tqdm import tqdm
base = 'VOCData/images'
for pt in tqdm(os.listdir(base)):
    if '_p_' in pt:
        os.remove(os.path.join(base, pt))