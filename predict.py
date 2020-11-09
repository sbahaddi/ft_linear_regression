import argparse
import pandas as pd
from thetas import getThetas, saveThetas
from readCsv import openCsv


def predictPrice(theta0, theta1, mileage):
    price = (theta1 * mileage) + theta0
    return price


if __name__ == "__main__":
    # read csv
    X, Y = openCsv("data.csv")

    # read thetas
    theta0, theta1 = getThetas("thetas")

    # read mileage
    mileage = int(input("Enter your mileage: "))

    # normalize mileage
    mileage = (mileage - X.min()) / (X.max() - X.min())

    # estimate price
    predictedPrice = predictPrice(theta0, theta1, float(mileage))

    # denormalize price
    if predictedPrice != 0.0:
        predictedPrice = predictedPrice * (Y.max() - Y.min()) + Y.min()

    print("Predicted price is : ", predictedPrice)
