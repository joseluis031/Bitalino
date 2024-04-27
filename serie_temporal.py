import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Cargar datos
datos = pd.read_csv('cora_ger.csv')
serie_temporal = datos['Septima_Columna']

# Análisis exploratorio básico podría incluir visualización de la serie
serie_temporal.plot()

# Determinar la estacionalidad, tendencia, etc. Podría requerir diferenciación o transformación logarítmica

# Identificar los parámetros p, d, q para ARIMA y los parámetros estacionales para SARIMA
# Esto normalmente se hace utilizando gráficos de autocorrelación y autocorrelación parcial,
# así como optimizando el criterio de información (por ejemplo, AIC)

# Ajustar el modelo ARIMA
p = 1
d = 0
q = 1
P = 1
D = 0
Q = 1
s = 6  # Estacionalidad mensual

modelo_arima = ARIMA(serie_temporal, order=(p, d, q))
resultado_arima = modelo_arima.fit()

# Ajustar el modelo SARIMA
modelo_sarima = SARIMAX(serie_temporal, order=(p, d, q), seasonal_order=(P, D, Q, s))
resultado_sarima = modelo_sarima.fit()

# Realizar predicciones
predicciones_arima = resultado_arima.forecast(steps=10)
predicciones_sarima = resultado_sarima.forecast(steps=10)

# Visualizar las predicciones
plt.plot(serie_temporal, label='Original')
# plt.plot(predicciones_arima, label='ARIMA Predictions')
plt.plot(predicciones_sarima, label='SARIMA Predictions')
plt.legend()
plt.show()