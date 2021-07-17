# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from tqdm import tqdm
import os
from os import getcwd


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 
    y = (box[2] + box[3]) / 2.0 
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h

small_num = 0
keep_num = 0

def convert_annotation(image_id):
    global small_num, keep_num
    # try:
    in_file = open('VOCData/images/{}.xml'.format(image_id), encoding='utf-8')
    out_file = open('VOCData/labels/{}.txt'.format(image_id),
                    'w', encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes[cls]
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        if b2 - b1 < w * 0.005 or b4 - b3 < h * 0.005:
                small_num += 1
                continue
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        keep_num += 1
        out_file.write(str(cls_id) + " " +
                       " ".join([str(a) for a in bb]) + '\n')
    # except Exception as e:
    #     print(e, image_id)


if __name__ == '__main__':

    sets = ['train', 'val']

    image_ids = [v.split('.')[0]
                 for v in os.listdir('VOCData/images/') if v.endswith('.xml')]

    split_num = int(0.95 * len(image_ids))

    # classes = {
    #     "head":0, "visible body":1, "full body":2, "small car":3, 
    #     "midsize car":3, "large car":3,  "bicycle":3, "motorcycle":3, 
    #     "tricycle":3, "electric car":3, "baby carriage":3, "unsure":3
    # }

    # classes = {
    #     "visible body":1, "small car":3, 
    #     "midsize car":3, "large car":3,  "bicycle":3, "motorcycle":3, 
    #     "tricycle":3, "electric car":3, "baby carriage":3, "unsure":3
    # }
    classes = {"head":0, "full body":2}



    if not os.path.exists('VOCData/labels/'):
        os.makedirs('VOCData/labels/')

    list_file = open('train.txt', 'w')
    for image_id in tqdm(image_ids[:split_num]):
        list_file.write('VOCData/images/{}.jpg\n'.format(image_id))
        convert_annotation(image_id)
    list_file.close()

    list_file = open('val.txt', 'w')
    for image_id in tqdm(image_ids[split_num:]):
        list_file.write('VOCData/images/{}.jpg\n'.format(image_id))
        convert_annotation(image_id)
    list_file.close()
    print('small_num:', small_num)
    print(' keep_num:', keep_num)
