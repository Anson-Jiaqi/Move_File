import math
import os
import shutil
import re

folder_path = r"D:\Study\Project\Data\4x2\file"
root = r"D:\Study\Project\Data\4x2\target"
channel_set = set()
F_set = set()
pattern = r'(?i)([Ff][0-9]+|[Tt][0-9]+|[Zz][0-9]+|[Cc][0-9]+)'
X = 4
Y = 2
layer = 0
matrix = [[1 for _ in range(X)] for _ in range(Y)]
order = [[1 for _ in range(X)] for _ in range(Y)]

channel_names = ""


p = os.listdir(folder_path)
for filename in p:
    matches = re.findall(pattern, filename)
    channel_name = ""
    Z = ""
    F = ""
    if matches:
        keys = {}
        for match in matches:
            key = match[0][0].upper() + match[0][1:]  # 将关键字的首字母转换为大写

            if key == "C":
                value = match[1:]
                value = int(value)
                channel_name = "C" + str(value)
            if key == "Z":
                value = match[1:]
                value = int(value)
                Z = "Z" + str(value)
            if key == "T":
                value = match[1:]
                value = int(value)
                time = "T" + str(value)
            if key == "F":
                value = match[1:]
                value = int(value)
                F = "F" + str(value)
        F_set.add(F)

sorted_F_set = sorted(F_set, key=lambda x: int(x[1:]))


i = 0
for x in range(X):
    for y in range(Y):
        matrix[y][x] = sorted_F_set[i]
        order[y][x] = i
        i = i+1








# for y in range(Y):
#     first_level = f"{y :06d}"
#     print(first_level)
#     for x in range(X):
#         matrix[x][y]

##############################
for filename in p:
    # print(filename)
    matches = re.findall(pattern, filename)
    channel_name = ""
    Z = ""
    F = ""
    if matches:
        keys = {}
        for match in matches:
            key = match[0][0].upper() + match[0][1:]  # 将关键字的首字母转换为大写

            if key == "C":
                value = match[1:]
                value = int(value)
                channel_name = "C" + str(value)
            if key == "Z":
                value = match[1:]
                value = int(value)
                Z = "Z" + str(value)
            if key == "T":
                value = match[1:]
                value = int(value)
                time = "T" + str(value)
            if key == "F":
                value = match[1:]
                value = int(value)
                F = "F" + str(value)

    channel_set.add(channel_name)

num_channels = len(channel_set)
for channel_name in channel_set:
    channel_path = os.path.join(root, channel_name)
    if not os.path.exists(channel_path):
        os.makedirs(channel_path)

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
            for filename in p:


                matches = re.findall(pattern, filename)
                channel_name = ""
                Z = ""
                F = ""
                if matches:
                    keys = {}
                    for match in matches:
                        print(match)
                        key = match[0][0].upper() + match[0][1:]  # 将关键字的首字母转换为大写
                        if key == "C":
                            value = match[1:]
                            value = int(value)
                            channel_name = "C" + str(value)
                        if key == "Z":
                            value = match[1:]
                            value = int(value)
                            Z = "Z" + str(value)
                        if key == "T":
                            value = match[1:]
                            value = int(value)
                            time = "T" + str(value)
                        if key == "F":
                            value = match[1:]
                            value = int(value)
                            F = "F" + str(value)
                if F == pt:
                    num_str = Z[1:]
                    num = int(num_str)*8+order[y][x]
                    new_filename = f"{num :06d}" + ".tif"
                    path1 = os.path.join(root,channel_name)
                    path2 = os.path.join(path1,first_level)
                    path3 = os.path.join(path2,second_level)
                    target = os.path.join(path3,new_filename)
                    old_filepath = os.path.join(folder_path, filename)
                    if os.path.exists(old_filepath):
                        shutil.move(old_filepath, target)

















