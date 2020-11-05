import argparse
import numpy as np
from readCsv import openCsv
from thetas import saveThetas
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--visu", help="select which visualization you want.")
parser.add_argument("-p", "--plot", help="visualize data to see their repartition")
args = parser.parse_args()

# init plot
if args.visu == "train":
    plt.ion()
    figure = plt.figure()
    ax = figure.add_subplot(1, 1, 1)


def plot_cicle(X, Y, Y_pred):
    ax.clear()
    ax.scatter(X, Y)
    ax.plot(X, Y_pred, "r")
    plt.pause(0.0001)


# def plot_finalTrain(X, Y, Y_pred):
#   plt.scatter(X, Y)
#  plt.plot(X, Y_pred, "r")
# plt.show()


class Regression:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.theta0 = 0.0
        self.theta1 = 0.0
        self.cost_history = []
        self.Y_pred = 0
        self.X_norm = 0
        self.Y_norm = 0

    def normalize_x(self):
        xmax = self.X.max()
        xmin = self.X.min()
        return (self.X - xmin) / (xmax - xmin)

    def normalize_y(self):
        ymax = self.Y.max()
        ymin = self.Y.min()
        return (self.Y - ymin) / (ymax - ymin)

    def hypothesis(self, theta0, theta1, X):
        Y_pred = (theta1 * X) + theta0
        return Y_pred

    def train(self, lr=0.001):
        self.X_norm = self.normalize_x()
        self.Y_norm = self.normalize_y()

        m = float(len(self.X_norm))
        iteration = 0

        while True:
            Y_pred = self.hypothesis(self.theta0, self.theta1, self.X_norm)

            if iteration % 3000 == 0 and args.visu == "train":
                plot_cicle(self.X_norm, self.Y_norm, Y_pred)

            tmp_theta0 = (1 / m) * np.sum(Y_pred - self.Y_norm)
            tmp_theta1 = (1 / m) * np.sum(self.X_norm * (Y_pred - self.Y_norm))

            if abs(tmp_theta0) < 0.0001 and abs(tmp_theta1) < 0.0001:
                print("Training finished.")
                break

            self.theta0 -= lr * tmp_theta0
            self.theta1 -= lr * tmp_theta1

            iteration += 1
        self.Y_pred = Y_pred


if __name__ == "__main__":
    X, Y = openCsv("data.csv")
    if args.plot == "on":
        plt.scatter(X, Y)
        plt.show()
    else:
        regression = Regression(X, Y)
        regression.train()
        saveThetas("thetas", regression.theta0, regression.theta1)
        if args.visu == "train":
            plt.ioff()
            plt.show()
