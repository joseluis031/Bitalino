import pandas as pd

def extraer_septima_columna_y_guardar_como_csv(nombre_archivo_entrada, nombre_archivo_salida):
    # Leer los datos del archivo de texto
    datos = pd.read_csv(nombre_archivo_entrada, delim_whitespace=True, header=None)
    
    # Extraer la séptima columna (columna con índice 6)
    datos_requeridos = datos.iloc[:, 6]
    
    # Crear un DataFrame con la columna extraída y el número de fila
    resultado = pd.DataFrame({
        'Numero_de_Fila': datos_requeridos.index,
        'Septima_Columna': datos_requeridos
    })
    
    # Guardar el DataFrame como un archivo CSV
    resultado.to_csv(nombre_archivo_salida, index=False)

# Usar la función con los nombres de archivos que quieras
#extraer_septima_columna_y_guardar_como_csv('cora_ger.txt', 'cora_ger.csv')

import pandas as pd
import matplotlib.pyplot as plt

def graficar_datos(nombre_archivo_csv):
    # Leer los datos del archivo CSV
    datos = pd.read_csv(nombre_archivo_csv)
    
    # Configurar la gráfica
    plt.figure(figsize=(10, 5))  # Configura el tamaño de la gráfica
    plt.plot(datos['Numero_de_Fila'], datos['Septima_Columna'], marker='o', linestyle='-', color='b')
    plt.title('Gráfica de Séptima Columna vs Número de Fila')
    plt.xlabel('Número de Fila')
    plt.ylabel('Séptima Columna')
    plt.grid(True)
    
    # Mostrar la gráfica
    plt.show()

# Usar la función con el nombre de archivo que quieras
#graficar_datos('cora_ger.csv')


def graficar_ecg(nombre_archivo_csv):
    # Leer los datos del archivo CSV
    datos = pd.read_csv(nombre_archivo_csv)
    
    # Configurar la gráfica
    plt.figure(figsize=(20, 4))  # Configura el tamaño de la gráfica para que sea más ancha
    plt.plot(datos['Numero_de_Fila'], datos['Septima_Columna'], linestyle='-', color='black')
    plt.title('Electrocardiograma Simulado')
    plt.xlabel('Número de Fila')
    plt.ylabel('Séptima Columna')
    plt.grid(True)
    plt.tight_layout()
    
    # Ajustar los límites del eje Y para acercarse más a los valores del ECG
    plt.ylim(min(datos['Septima_Columna']) - 10, max(datos['Septima_Columna']) + 10)
    
    # Eliminar los ticks del eje Y para emular la apariencia de un ECG
    plt.yticks([])
    
    # Mostrar la gráfica
    plt.show()

# Usar la función con el nombre de archivo que quieras
graficar_ecg('cora_ger.csv')
