import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = DecisionTreeClassifier()

model.fit(X, y)

accuracy = model.score(X, y)

print(f"Model Accuracy is {accuracy*100:.02f}%")
