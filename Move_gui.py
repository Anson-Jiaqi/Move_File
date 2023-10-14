import math
import os
import shutil
import re
import tkinter as tk
from tkinter import filedialog

# pattern for the keywords in file name
pattern = r'(?i)([Ff][0-9]+|[Tt][0-9]+|[Zz][0-9]+|[Cc][0-9]+)'

folder_path = r""
target = r""
channel_set = set()
F_set = set()


# This function is used to find the file number in the file name
# Then sort the F number in ascending order and save it in the F set
def findF(p):
    for filename in p:
        matches = re.findall(pattern, filename)
        channel_name = ""
        Z = ""
        F = ""
        if matches:
            keys = {}
            for match in matches:  # check the keywords in the file name
                key = match[0][0].upper() + match[0][1:]

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
    sorted_F_set = sorted(F_set, key=lambda x: int(x[1:]))  # sort the F number
    return sorted_F_set


# This function is used to set the order type of the File
def orders(type, sorted_F_set, matrix, order, X, Y):
    match type:  # There are totally 8 type in this function. Detail can check the image in README.md
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
                elif (x + 1) % 2 == 0:  # even
                    for y in range(Y):
                        y1 = Y - y - 1
                        matrix[y1][x] = sorted_F_set[i]
                        order[y1][x] = i
                        i = i + 1
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


# This function is used to create the channel folder
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
                key = match[0][0].upper() + match[0][1:]

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


# Create the two-level hierarchy folder
def create_folder():
    for channel_name in channel_set:
        channel_path = os.path.join(target, channel_name)
        for y in range(Y):  # Create the first level folder
            first_level = f"{y :06d}"
            first_path = os.path.join(channel_path, first_level)
            if not os.path.exists(first_path):
                os.makedirs(first_path)

            for x in range(X):  # Create the second level folder
                name1 = f"{y :06d}"
                name2 = f"{x :06d}"
                second_level = name1 + "_" + name2
                second_path = os.path.join(first_path, second_level)
                if not os.path.exists(second_path):
                    os.makedirs(second_path)


# Move the file to the target folder and rename each files according to the rules of Terastitcher
def movefile(target, p, matrix, order):
    print(target)
    for channel_name in channel_set:
        channel_path = os.path.join(target, channel_name)
        for y in range(Y):
            first_level = f"{y :06d}"
            for x in range(X):
                name1 = f"{y :06d}"
                name2 = f"{x :06d}"
                second_level = name1 + "_" + name2
                pt = matrix[y][x]  # Get the file number in the current position
                for filename in p:
                    matches = re.findall(pattern, filename)
                    channel_name = ""
                    Z = ""
                    F = ""
                    if matches:
                        for match in matches:
                            key = match[0][0].upper() + match[0][1:]
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
                    if F == pt:  # Check if current file should in current position
                        num_str = Z[1:]
                        num = int(num_str) * X * Y + order[y][x]  # Create the new file name according to the X, Y and Z
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
    def browse_folder():
        global folder_path
        folder_path = filedialog.askdirectory()
        folder_path = os.path.normpath(folder_path)
        folder_path_label.config(text=folder_path)


    def browse_target():
        global target
        target = filedialog.askdirectory()
        target = os.path.normpath(target)
        target_label.config(text=target)


    def update_types():
        global types
        types = int(types_entry.get())


    def run_code():
        global X, Y
        X = int(x_entry.get())
        Y = int(y_entry.get())
        types = int(types_entry.get())
        matrix = [[1 for _ in range(X)] for _ in range(Y)]
        order = [[1 for _ in range(X)] for _ in range(Y)]
        if folder_path and target and types is not None:
            p = os.listdir(folder_path)
            sorted_F_set = findF(p)
            orders(types, sorted_F_set, matrix, order, X, Y)
            addChannel(p)
            create_folder()
            print(target)
            print(order)
            print(matrix)
            movefile(target, p, matrix, order)
            print("Complete")
        else:
            print("Please input the value")

# create the GUI
    root = tk.Tk()
    root.title("Move File")
    root.geometry("400x400")

    x_label = tk.Label(root, text="X:")
    x_label.pack()
    x_entry = tk.Entry(root)
    x_entry.pack()
    y_label = tk.Label(root, text="Y:")
    y_label.pack()
    y_entry = tk.Entry(root)
    y_entry.pack()

    browse_folder_button = tk.Button(root, text="Select Folder", command=browse_folder)
    browse_folder_button.pack()
    folder_path_label = tk.Label(root, text="Folder Path:")
    folder_path_label.pack()

    browse_target_button = tk.Button(root, text="Select the target folder", command=browse_target)
    browse_target_button.pack()
    target_label = tk.Label(root, text="Target folder path:")
    target_label.pack()
    types_label = tk.Label(root, text="Arrangement type:")
    types_label.pack()
    types_entry = tk.Entry(root)
    types_entry.pack()

    run_button = tk.Button(root, text="Run", command=run_code)
    run_button.pack()

    # Global variables
    folder_path = ""
    target = ""
    types = None
    X = 0
    Y = 0

    root.mainloop()
