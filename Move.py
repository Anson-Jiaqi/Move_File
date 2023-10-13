import math
import os
import shutil
import re

pattern = r'(?i)([Ff][0-9]+|[Tt][0-9]+|[Zz][0-9]+|[Cc][0-9]+)'
X = 0
Y = 0
folder_path = r""
target = r""
channel_set = set()
F_set = set()
matrix = [[1 for _ in range(X)] for _ in range(Y)]
order = [[1 for _ in range(X)] for _ in range(Y)]

def findF(p):
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
    return sorted_F_set


def orders(type, sorted_F_set):
    i = 0
    for x in range(X):
        if (x + 1) % 2 == 0:  # even
            for y in range(Y):
                matrix[y][x] = sorted_F_set[i]
                order[y][x] = i
                i = i + 1
        elif (x + 1) % 2 == 1:  # odd
            for y in range(Y):
                y1 = Y - y - 1
                matrix[y1][x] = sorted_F_set[i]
                order[y1][x] = i
                i = i + 1


# for y in range(Y):
#     first_level = f"{y :06d}"
#     print(first_level)
#     for x in range(X):
#         matrix[x][y]

##############################
def addChannel(p):
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
        channel_path = os.path.join(target, channel_name)
        if not os.path.exists(channel_path):
            os.makedirs(channel_path)

################################
def create_folder():
    for channel_name in channel_set:
        channel_path = os.path.join(target, channel_name)
        for y in range(Y):
            first_level = f"{y :06d}"
            first_path = os.path.join(channel_path, first_level)
            if not os.path.exists(first_path):
                os.makedirs(first_path)

            for x in range(X):
                name1 = f"{y :06d}"
                name2 = f"{x :06d}"
                second_level = name1 + "_" + name2
                second_path = os.path.join(first_path, second_level)
                if not os.path.exists(second_path):
                    os.makedirs(second_path)
def movefile(target,p):
    print(target)
    for channel_name in channel_set:
        channel_path = os.path.join(target, channel_name)
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
                        num = int(num_str) * X * Y + order[y][x]
                        new_filename = f"{num :06d}" + ".tif"
                        path1 = os.path.join(target, channel_name)
                        path2 = os.path.join(path1, first_level)
                        path3 = os.path.join(path2, second_level)
                        targetpath = os.path.join(path3, new_filename)
                        print(targetpath)
                        old_filepath = os.path.join(folder_path, filename)
                        if os.path.exists(old_filepath):
                            shutil.move(old_filepath, targetpath)

##############################################
# main #
##############################################

if __name__ == '__main__':
    folder_path = r"D:\Study\Project\Data\DF\file"
    target = r"D:\Study\Project\Data\DF\target2"
    type = "1"
    X = 2
    Y = 2
    matrix = [[1 for _ in range(X)] for _ in range(Y)]
    order = [[1 for _ in range(X)] for _ in range(Y)]
    layer = 0
    p = os.listdir(folder_path)
    sorted_F_set = findF(p)
    print(sorted_F_set)
    orders(type,sorted_F_set)
    addChannel(p)
    create_folder()
    movefile(target,p)
