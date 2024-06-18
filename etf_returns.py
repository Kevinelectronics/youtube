import os
import yfinance as yf
import pandas as pd
import numpy as np

# Lista de los principales 30 ETFs en US
etfs = [
    'SPY', 'IVV', 'VOO', 'QQQ', 'VTI', 'VEA', 'VWO', 'IEMG', 'AGG', 'GLD',
    'IWM', 'VUG', 'IJR', 'VNQ', 'BND', 'VIG', 'DIA', 'IEFA', 'EFA', 'LQD',
    'EEM', 'HYG', 'VXUS', 'BNDX', 'XLK', 'XLF', 'XLY', 'XLE', 'XLV', 'XLP'
]

# Fecha de inicio para obtener los datos históricos (5 años atrás desde hoy)
start_date = '2018-06-18'
end_date = '2023-06-18'

# DataFrame para almacenar los resultados
results = pd.DataFrame(columns=['ETF', 'Annualized Return', 'Standard Deviation'])

def calculate_annualized_return_and_std(etf):
    # Descargar los datos históricos del ETF
    print(f"Descargando datos para {etf}")
    data = yf.download(etf, start=start_date, end=end_date)
    
    if data.empty:
        print(f"No se encontraron datos para {etf}")
        return None, None
    
    # Calcular los retornos diarios
    data['Daily Return'] = data['Adj Close'].pct_change()
    
    # Calcular el retorno anualizado
    cumulative_return = (1 + data['Daily Return']).prod() - 1
    annualized_return = (1 + cumulative_return) ** (252 / len(data['Daily Return'].dropna())) - 1
    
    # Calcular la desviación estándar anualizada
    std_dev = data['Daily Return'].std() * np.sqrt(252)
    
    return annualized_return, std_dev

# Calcular los valores para cada ETF y almacenar los resultados
for etf in etfs:
    annualized_return, std_dev = calculate_annualized_return_and_std(etf)
    if annualized_return is not None and std_dev is not None:
        results = results.append({
            'ETF': etf,
            'Annualized Return': annualized_return,
            'Standard Deviation': std_dev
        }, ignore_index=True)

# Especificar la carpeta donde se guardará el archivo
folder_path = './output'  # Carpeta en la misma ubicación del script
print(f"Creando carpeta en: {folder_path}")
os.makedirs(folder_path, exist_ok=True)  # Crear la carpeta si no existe

# Guardar los resultados en un archivo Excel en la carpeta especificada
file_path = os.path.join(folder_path, 'ETF_Annualized_Return_and_Std.xlsx')
print(f"Guardando archivo en: {file_path}")
results.to_excel(file_path, index=False)

# Verificar si el archivo se ha creado correctamente
if os.path.isfile(file_path):
    print(f"Archivo Excel generado exitosamente en {file_path}.")
else:
    print("Error: El archivo Excel no se pudo generar.")
