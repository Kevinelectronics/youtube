import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar datos
data = pd.read_csv('C:/Users/kevin/OneDrive/Desktop/youtube_scripts/datos_ventas_crm_actualizados.csv', parse_dates=['Fecha de Venta'])

# Preprocesamiento para agregar columna de mes
data['Mes de Venta'] = data['Fecha de Venta'].dt.to_period('M')

# Título del Dashboard
st.title('Dashboard de Ventas CRM')

# Selector de país para filtrar datos
# Asumiendo que 'datos_filtrados' es tu DataFrame filtrado por país
# Agrupar por 'Mes de Venta', sumar solo columnas numéricas, y luego resetear el índice
pais_seleccionado = st.selectbox('Seleccione un país:', options=data['País de Venta'].unique())
datos_filtrados = data[data['País de Venta'] == pais_seleccionado]

# Agrupar los datos filtrados por 'Mes de Venta', sumar solo las columnas numéricas y resetear el índice
ventas_por_mes = datos_filtrados.groupby('Mes de Venta').sum(numeric_only=True).reset_index()

# Ahora, convertir solo la columna 'Mes de Venta' a string para compatibilidad con Plotly
ventas_por_mes['Mes de Venta'] = ventas_por_mes['Mes de Venta'].astype(str)

# Crear el gráfico con Plotly
fig_ventas_mes = px.line(ventas_por_mes, x='Mes de Venta', y='Cantidad', title='Ventas por Mes')
st.plotly_chart(fig_ventas_mes)

# Gráfico de donut para segmento de clientes
ventas_por_segmento = data.groupby('Tipo de Cliente')['Cantidad'].sum().reset_index()
fig_segmento = px.pie(ventas_por_segmento, values='Cantidad', names='Tipo de Cliente', title='Ventas por Segmento de Cliente', hole=0.3)
st.plotly_chart(fig_segmento)

# KPI de Facturación Total
facturacion_total = data['Importe del Producto'].sum()
st.metric(label="Facturación Total", value=f"${facturacion_total:,.2f}")

