def saveThetas(file, theta0, theta1):
    thetaFile = open(file, "w")
    thetaFile.write("{}\n{}".format(theta0, theta1))
    thetaFile.close()


def getThetas(file):
    try:
        with open(file, "r") as file:
            # theta0
            theta0 = float(file.readline())
            # theta1
            theta1 = float(file.readline())
            return (theta0, theta1)
    except Exception:
        theta0 = 0.0
        theta1 = 0.0
        return (theta0, theta1)
