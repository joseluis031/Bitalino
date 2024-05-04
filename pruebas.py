import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
import warnings

# Ignoring warning messages
warnings.filterwarnings('ignore')

# Creating a DataFrame from the provided data

df = pd.read_csv('cora_ger.csv')

# Perform Dickey-Fuller test
result = adfuller(df['Septima_Columna'])
adf_statistic = result[0]
p_value = result[1]

# Fit an ARIMA model (p=1, d=1, q=1) just as an example to compute AIC, BIC.
# A grid search would be needed in a real analysis to find optimal parameters.
model = ARIMA(df['Septima_Columna'], order=(1, 1, 1))
model_fit = model.fit()

# AIC and BIC
aic = model_fit.aic
bic = model_fit.bic

# Mean Squared Error (we need predictions and true values to compute MSE)
# Let's make a simple prediction for the last 10 points as an example.
X = df['Septima_Columna'].values
size = int(len(X) * 0.8)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
    model = ARIMA(history, order=(1,1,1))
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)

mse = mean_squared_error(test, predictions)

# Output the test results and metrics
print(adf_statistic, p_value, aic, bic, mse)

