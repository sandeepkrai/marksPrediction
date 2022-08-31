import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def marks_prediction(marks):
    X = pd.read_csv("xtrain.csv")
    y = pd.read_csv("ytrain.csv")

    x = X.values
    y = y.values

    plt.scatter(x,y)
    plt.xlabel("No. of hours")
    plt.ylabel("Maks scored")
    plt.show()

    model = LinearRegression()

    model.fit(x,y)

    mark = int(marks)
    x_test = np.array(mark)
    x_test = x_test.reshape(1,-1)

    return model.predict(x_test)

