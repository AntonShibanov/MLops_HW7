import numpy as np
import pandas as pd
import pickle
import json
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target
hyperparameters = {"n_estimators": 100, "random_state": 42}

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestClassifier(**hyperparameters)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Точность accuracy: {accuracy:.2f}')

# Сохраняем артефакты
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('hyperparameters.json', 'w') as f:
    json.dump(hyperparameters, f, indent=2)
