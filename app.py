import streamlit as st

# Título de la aplicación
st.title("Calculadora de Ahorro Económico y Emisiones")
st.write("Este aplicativo estima el ahorro económico, tiempo de retorno de inversión y reducción de emisiones por el cambio de equipos de aire acondicionado.")

# Datos iniciales
consumo_actual_kwh_dia = 12
consumo_actual_kwh_mes = consumo_actual_kwh_dia * 30

consumo_nuevo_kwh_dia = 6
consumo_nuevo_kwh_mes = consumo_nuevo_kwh_dia * 30

tarifa_sin_subsidio = 800
subsidio = 0.60
tarifa_con_subsidio = tarifa_sin_subsidio * (1 - subsidio)

consumo_subsidio = 175

# Cálculo de costos actuales
costo_actual_con_subsidio = consumo_subsidio * tarifa_con_subsidio
consumo_fuera_subsidio = consumo_actual_kwh_mes - consumo_subsidio if consumo_actual_kwh_mes > consumo_subsidio else 0
costo_actual_sin_subsidio = consumo_fuera_subsidio * tarifa_sin_subsidio
costo_total_actual = costo_actual_con_subsidio + costo_actual_sin_subsidio

# Cálculo de costos nuevos
costo_nuevo_con_subsidio = consumo_subsidio * tarifa_con_subsidio
consumo_nuevo_fuera_subsidio = consumo_nuevo_kwh_mes - consumo_subsidio if consumo_nuevo_kwh_mes > consumo_subsidio else 0
costo_nuevo_sin_subsidio = consumo_nuevo_fuera_subsidio * tarifa_sin_subsidio
costo_total_nuevo = costo_nuevo_con_subsidio + costo_nuevo_sin_subsidio

# Ahorro económico
ahorro_mensual = costo_total_actual - costo_total_nuevo

# Costo total de cambio de equipos
costo_total_equipos = 3000000 * 2

# Tiempo de retorno de la inversión
tiempo_retorno_inversion = costo_total_equipos / ahorro_mensual

# Reducción de emisiones de GEI
emisiones_actuales = consumo_actual_kwh_mes * 0.2
emisiones_nuevas = consumo_nuevo_kwh_mes * 0.2
reduccion_emisiones = emisiones_actuales - emisiones_nuevas

# Display results
st.write(f"Ahorro económico mensual: {ahorro_mensual:.2f} $")
st.write(f"Tiempo de retorno de la inversión: {tiempo_retorno_inversion:.2f} meses")
st.write(f"Reducción mensual de emisiones de GEI: {reduccion_emisiones:.2f} kg CO2e")

# Cálculo de subsidio alternativo
st.write("-------------")
st.write("Cálculo de subsidio alternativo")

subsidio_compra = 3000000 * 2 * 0.50
inversion_restante = 3000000 * 2 - subsidio_compra
tiempo_retorno_inversion_alternativa = inversion_restante / ahorro_mensual

# Ahorro del gobierno en subsidio de electricidad en 10 años
costo_subsidio_electrico_mensual = 180 * tarifa_con_subsidio
ahorro_gobierno_10_anios = (57_600 * 120)

st.write(f"Subsidio del gobierno para equipos: {subsidio_compra:.2f} $")
st.write(f"Tiempo de retorno de la inversión con subsidio del 50%: {tiempo_retorno_inversion_alternativa:.2f} meses")
st.write(f"Ahorro del gobierno en 10 años: {ahorro_gobierno_10_anios:.2f} $")
