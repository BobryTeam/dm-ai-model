import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import RidgeCV
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

df = pd.read_csv('./test-data.csv', index_col=None)

X = df.drop('predict', axis=1)
y = df['predict']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

degree = 10
alphas = np.logspace(-6, 6, 13)

# Создание pipeline
model = Pipeline([
    ('poly_features', PolynomialFeatures(degree=degree)),
    ('ridge', RidgeCV(alphas=alphas, store_cv_results=True))
])
model.fit(X_train, y_train)

print("Правильность на обучающем наборе: {:.2f}".format(model.score(X_train, y_train)))
print("Правильность на тестовом наборе: {:.2f}".format(model.score(X_test, y_test)))

print("Правильность на обучающем наборе: {:.2f}".format(model.score(X_train, y_train)))
print("Правильность на тестовом наборе: {:.2f}".format(model.score(X_test, y_test)))
# print(X_test)
# print(model.predict(X_test))

y_pred = model.predict(X_test)

# Оценка качества модели
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f'MSE: {mse}')
print(f'MAE: {mae}')

# Лучшее значение alpha
best_alpha = model.named_steps['ridge'].alpha_
print(f'Best alpha: {best_alpha}')

joblib.dump(model, 'model.joblib')
