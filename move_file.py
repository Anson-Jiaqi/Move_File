import math
import os
import shutil
import re
#test
folder_path = r"D:\Study\Project\Data\copy\file"
root = r"D:\Study\Project\Data\copy"
channel_set = set()
#test2
X = 4
Y = 2
layer = 0
matrix = [[1 for _ in range(X)] for _ in range(Y)]
order = [[1 for _ in range(X)] for _ in range(Y)]
channel_names = ""


p = os.listdir(folder_path)

print("1")
i = 0
for x in range(X):
    for y in range(Y):
        matrix[y][x] = p[i]
        order[y][x] = i
        i = i+1








# for y in range(Y):
#     first_level = f"{y :06d}"
#     print(first_level)
#     for x in range(X):
#         matrix[x][y]

##############################
for pi in p:
    x=0
    y=0
    create = 0
    for filename in os.listdir(os.path.join(folder_path, pi)):
        # print(filename)
        if not filename.endswith(".tif") or filename.endswith("Overlay.tif"):
            continue
        match = re.search(r"_(\w+)_(Z\d{3}).tif", filename)
        if not match:
            continue
        channel_name = match.group(1)
        channel_set.add(channel_name)
        Z = match.group(2)
        if create == 0 :
            num_channels = len(channel_set)
            for channel_name in channel_set:
                channel_path = os.path.join(root, channel_name)
                if not os.path.exists(channel_path):
                    os.makedirs(channel_path)
                    create = 1
################################

for channel_name in channel_set:
    channel_path = os.path.join(root, channel_name)
    for y in range(Y):
        first_level = f"{y :06d}"
        first_path = os.path.join(channel_path, first_level)
        if not os.path.exists(first_path):
            os.makedirs(first_path)


        for x in range(X):
            name1 = f"{y :06d}"
            name2 = f"{x :06d}"
            second_level = name1 + "_" + name2
            second_path = os.path.join(first_path,second_level)
            if not os.path.exists(second_path):
                os.makedirs(second_path)



for channel_name in channel_set:
    channel_path = os.path.join(root, channel_name)
    for y in range(Y):
        first_level = f"{y :06d}"
        for x in range(X):
            name1 = f"{y :06d}"
            name2 = f"{x :06d}"
            second_level = name1 + "_" + name2
            pt = matrix[y][x]
            print(pt)
            path = os.path.join(folder_path, pt)
            file_names = os.listdir(path)
            sorted_file_names = sorted(file_names)
            for filename in sorted_file_names:
                match = re.search(r"_(\w+)_(Z\d{3}).tif", filename)
                channel_name = match.group(1)
                Z = match.group(2)
                num_str = Z[1:]
                num = int(num_str)*8+order[y][x]
                new_filename = f"{num :06d}" + ".tif"
                path1 = os.path.join(root,channel_name)
                path2 = os.path.join(path1,first_level)
                path3 = os.path.join(path2,second_level)
                target = os.path.join(path3,new_filename)
                old_filepath = os.path.join(path, filename)
                shutil.move(old_filepath, target)

















