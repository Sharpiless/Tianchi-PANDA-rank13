import cv2
import os
from tqdm import tqdm

base = 'VOCData/images/'

for img in tqdm(os.listdir(base)):
    if not img.endswith('.jpg'):
        continue
    pt = os.path.join(base, img)
    image = cv2.imread(pt)
    h, w = image.shape[:2]
    ratio = 1200 / w
    image = cv2.resize(image, None, fx=ratio, fy=ratio)
    cv2.imwrite(pt, image)