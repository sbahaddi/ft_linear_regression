import numpy as np


def openCsv(file):
    X = []
    Y = []
    try:
        with open(file, "r") as file:
            # skipping the header
            lines = file.readline()
            # reaing all lines
            lines = file.readlines()
            for line in lines:
                # splitting by ','
                split = line.split(",")
                # add Xs
                X.append(split[0])
                # add Ys
                Y.append(split[1][:-1])
    except Exception:
        print("Can't open file.")
    return (np.array(X, dtype=float), np.array(Y, dtype=float))