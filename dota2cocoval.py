import os
import json
import math

class_map = ['plane', 'baseball-diamond', 'bridge', 'ground-track-field',
         'small-vehicle', 'large-vehicle', 'ship', 'tennis-court',
         'basketball-court', 'storage-tank', 'soccer-ball-field', 'roundabout',
         'harbor', 'swimming-pool', 'helicopter']

annotations = []
def convert(txt_file_path, image_id_offset=0):
    with open(txt_file_path, 'r') as file:
        lines = file.readlines()
        lines_to_write = lines[2:]
    if lines_to_write == []:
        annotation = {
            "image_id": int(os.path.splitext(os.path.basename(txt_file_path))[0][1:]) + image_id_offset,
            "bbox": [],
            "category_id": None
        }
        annotations.append(annotation)
        
    for line in lines_to_write:
        parts = line.strip().split()
        category_id = class_map.index(parts[8]) + 1
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, parts[0:8])
        bbox = [x1, y1, x2, y2, x3, y3, x4, y4]
        
        annotation = {
            "image_id": int(os.path.splitext(os.path.basename(txt_file_path))[0][1:]) + image_id_offset,
            "bbox": bbox,
            "category_id": category_id
        }
        annotations.append(annotation)


txt_folder_path = '/ext/lx/dota/val/labelTxt/'
json_file_path = '/ext/lx/dota/val/DOTA_1.0.json' 

for txt_file in os.listdir(txt_folder_path):
    if txt_file.endswith('.txt'):
        txt_file_path = os.path.join(txt_folder_path, txt_file)
        convert(txt_file_path, image_id_offset=0)
print(annotations)

with open(json_file_path, 'w') as output_file:
    json.dump(annotations, output_file)
    
# convert(txt_file_path, image_id_offset=0)
# print(annotations)