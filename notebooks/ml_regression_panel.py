import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def load_dataset(csv_folder="data/cnn_2d"):
    labels = pd.read_csv(os.path.join(csv_folder, "labels.csv"))
    features = []
    targets = []

    for idx in labels["index"]:
        df = pd.read_csv(os.path.join(csv_folder, f"sim_{idx}.csv"))
        final = df[df["t"] == df["t"].max()]
        u_avg = final["u"].mean()
        features.append([labels.loc[idx, "D"], labels.loc[idx, "r"], labels.loc[idx, "K"]])
        targets.append(u_avg)

    X = np.array(features)
    y = np.array(targets)
    return X, y

def train_and_plot():
    X, y = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    plt.scatter(y_test, y_pred)
    plt.xlabel("Real u_avg")
    plt.ylabel("Predicho u_avg")
    plt.title("Regresión sobre brotes simulados")
    plt.grid(True)
    plt.show()
