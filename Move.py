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
    match type:
        case 1:
            #####  type 1  #####
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
        case 2:
            #####  type 2  #####
            i = 0
            for x in range(X):
                if (x + 1) % 2 == 1:  # odd
                    for y in range(Y):
                        matrix[y][x] = sorted_F_set[i]
                        order[y][x] = i
                        i = i + 1
                        print(i)
                elif (x + 1) % 2 == 0:  # even
                    for y in range(Y):
                        y1 = Y - y - 1
                        matrix[y1][x] = sorted_F_set[i]
                        order[y1][x] = i
                        i = i + 1
                        print(i)
        case 3:
            #####  type 3  #####
            i = 0
            for y in range(Y):
                for x in range(X):
                    y1 = Y - y - 1
                    if (y + 1) % 2 == 1:  # if odd row
                        x1 = X - x - 1
                        matrix[y1][x1] = sorted_F_set[i]
                        order[y1][x1] = i
                        i = i + 1
                    elif (y + 1) % 2 == 0:  # if even row
                        matrix[y1][x] = sorted_F_set[i]
                        order[y1][x] = i
                        i = i + 1
        case 4:
            #####  type 4  #####
            i = 0
            for y in range(Y):
                for x in range(X):
                    if (y + 1) % 2 == 1:  # if odd row
                        x1 = X - x - 1
                        matrix[y][x1] = sorted_F_set[i]
                        order[y][x1] = i
                        i = i + 1
                    elif (y + 1) % 2 == 0:  # if even row
                        matrix[y][x] = sorted_F_set[i]
                        order[y][x] = i
                        i = i + 1
        case 5:
            #####  type 5  #####
            i = 0
            for y in range(Y):
                for x in range(X):
                    y1 = Y - y - 1
                    if (y + 1) % 2 == 1:  # if odd row

                        matrix[y1][x] = sorted_F_set[i]
                        order[y1][x] = i
                        i = i + 1
                    elif (y + 1) % 2 == 0:  # if even row
                        x1 = X - x - 1
                        matrix[y1][x1] = sorted_F_set[i]
                        order[y1][x1] = i
                        i = i + 1
        case 6:
            #####  type 6  #####
            i = 0
            for x in range(X):
                for y in range(Y):
                    matrix[y][x] = sorted_F_set[i]
                    order[y][x] = i
                    i = i + 1

        case 7:
            #####  type 7  #####
            i = 0
            for y in range(Y):
                for x in range(X):
                    matrix[y][x] = sorted_F_set[i]
                    order[y][x] = i
                    i = i + 1
        case 8:
            #####  type 8  #####
            i = 0
            for y in range(Y):
                for x in range(X):
                    if (y + 1) % 2 == 1:  # if odd row
                        matrix[y][x] = sorted_F_set[i]
                        order[y][x] = i
                        i = i + 1
                    elif (y + 1) % 2 == 0:  # if even row
                        x1 = X - x - 1
                        matrix[y][x1] = sorted_F_set[i]
                        order[y][x1] = i
                        i = i + 1


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


def movefile(target, p):
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
    # folder_path = r"D:\Study\Project\Data\DF\file"
    # target = r"D:\Study\Project\Data\DF\target2"
    # types = 8
    # X = 2
    # Y = 2
    folder_path = input("Folder path: ")
    target = input("Target folder: ")
    types = input("Arrangement type: ")
    X = input("X: ")
    Y = input("Y: ")
    matrix = [[1 for _ in range(X)] for _ in range(Y)]
    order = [[1 for _ in range(X)] for _ in range(Y)]
    layer = 0
    p = os.listdir(folder_path)
    sorted_F_set = findF(p)
    print(sorted_F_set)
    orders(types, sorted_F_set)
    print(order)
    print(matrix)
    addChannel(p)
    create_folder()
    movefile(target, p)
