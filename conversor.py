import pandas as pd

# Especifica la ruta del archivo Excel (.xlsx)
archivo_excel = 'default of credit card clients-1.xlsx'

# Lee el archivo Excel en un DataFrame de pandas
df = pd.read_excel(archivo_excel)

# Especifica la ruta donde deseas guardar el archivo CSV
archivo_csv = 'dataset.csv'

# Guarda el DataFrame en formato CSV
df.to_csv(archivo_csv, index=False)  # El argumento index=False evita que se escriba el índice en el archivo CSV
