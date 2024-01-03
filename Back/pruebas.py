import pandas as pd

# Ruta al archivo Excel
ruta_archivo_excel = 'C:/Users/Jose/OneDrive - UCO/Desktop/proyecto funeraria/COLILLAS.xlsx'

# Nombre de la hoja y rango de celdas de la columna que deseas obtener
hoja = 'Hoja1'
rango_celdas = 'A2:A530'

# Leer el archivo Excel y obtener la columna especificada
data_frame = pd.read_excel(ruta_archivo_excel, sheet_name=hoja, usecols=[2], skiprows=3, nrows=10, header=None)
columna_especifica = data_frame[2].dropna().astype(int).tolist()

print(columna_especifica)
