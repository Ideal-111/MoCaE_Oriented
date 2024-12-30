import json
import os
import math


class_map = ['plane', 'baseball-diamond', 'bridge', 'ground-track-field',
         'small-vehicle', 'large-vehicle', 'ship', 'tennis-court',
         'basketball-court', 'storage-tank', 'soccer-ball-field', 'roundabout',
         'harbor', 'swimming-pool', 'helicopter']


with open('/ext/lx/dota/val/DOTA_1.0.json', 'r') as file:
    data = json.load(file)   
image_id_mapping = {image['file_name'].split('.')[0]: image['id'] for image in data['images']}
# image_id_mapping = {f"P{annotation['image_id']:04d}":annotation['image_id'] for annotation in data}
# print(image_id_mapping)

coco_format = []
# directory = 'dotatest/orpn_results'
directory = 'dotatest/gliding_vertex_results'
for file_name in os.listdir(directory):
    if file_name.endswith('.txt'):
        file_path = os.path.join(directory, file_name)
        base_name = os.path.splitext(file_name)[0]
        # print(file_path)
        with open(file_path, 'r') as file:
            # print(file)
            for line in file:
                parts = line.strip().split()
                # print(parts[0])
                image_id = image_id_mapping[parts[0]]
                score = float(parts[1])
                x1, y1, x2, y2, x3, y3, x4, y4 = map(float, parts[2:10])
                # xmin = min(x1, x2, x3, x4)
                # xmax = max(x1, x2, x3, x4)
                # ymin = min(y1, y2, y3, y4)
                # ymax = max(y1, y2, y3, y4)
                # width = xmax - xmin
                # height = ymax - ymin
                coco_dict = {
                    "image_id": int(image_id),
                    "score": score,
                    # "bbox": [xmin, ymin, width, height],
                    "bbox": [x1, y1, x2, y2, x3, y3, x4, y4],
                    "category_id": class_map.index(base_name) + 1
                }
                coco_format.append(coco_dict)
      
# print(coco_format)          
# det_directory = '/home/lx/mocae/calibration/orcnn/obb_final_detections/val.bbox.json'
det_directory = '/home/lx/mocae/calibration/gliding/obb_final_detections/val.bbox.json'          
with open(det_directory, 'w') as output_file:
    json.dump(coco_format, output_file)
