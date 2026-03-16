import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv(""C:/Users/ADMIN/Desktop/lab/house_prices_small.csv"")
X = df[['bedrooms', 'bathrooms', 'sqft', 'age', 'city']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Coefs:", model.coef_)

joblib.dump(model, "house_price_model.pkl")
