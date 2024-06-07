import streamlit as st

# Título principal de la aplicación
st.title("Análisis de costo y ahorro por cambio de equipos de aire acondicionado")

# Sección del sidebar para ingresar los datos básicos
st.sidebar.header("Datos Básicos")

estrato = st.sidebar.number_input("Estrato (1)", min_value=1, max_value=1, value=1)
precio_nuevos = st.sidebar.number_input("Precio por unidad de nuevos equipos inverter (\$)", value=3000000)
hrs_diarias = st.sidebar.number_input("Horas de uso diario", min_value=1, max_value=24, value=4)
tarifa_kwh = st.sidebar.number_input("Tarifa de energía (\$/kWh)", value=800)
subsidiado_pct = st.sidebar.number_input("Porcentaje de subsidio estatal (%)", min_value=0, max_value=100, value=60) / 100
consumo_subsistencia = st.sidebar.number_input("Consumo de subsistencia (kWh/mes)", value=175)
equipos_antiguos_cons = st.sidebar.number_input("Consumo equipos antiguos (kWh/TR)", value=1.5)
equipos_nuevos_cons = st.sidebar.number_input("Consumo equipos nuevos (kWh/TR)", value=0.75)
num_equipos = st.sidebar.number_input("Número de equipos de aire acondicionado", min_value=2, max_value=2, value=2)
dias_mes = st.sidebar.number_input("Días por mes", value=30)
subsidio_retiro = st.sidebar.number_input("Porcentaje del costo subvencionado para nuevos equipos (%)", min_value=0, max_value=100, value=50) / 100

# Cálculos

subsidiado_pct = 1-subsidiado_pct

consumo_antiguos_mensual = equipos_antiguos_cons * 1 * hrs_diarias * num_equipos * dias_mes
consumo_nuevos_mensual = equipos_nuevos_cons * 1 * hrs_diarias * num_equipos * dias_mes
ahorro_energia_mensual = consumo_antiguos_mensual - consumo_nuevos_mensual

subsidio_estatal = subsidiado_pct * tarifa_kwh * consumo_subsistencia

costo_mensual_antiguo = (consumo_antiguos_mensual - consumo_subsistencia) * tarifa_kwh
costo_mensual_antiguo += subsidio_estatal

costo_mensual_nuevos = (consumo_nuevos_mensual - consumo_subsistencia) * tarifa_kwh
costo_mensual_nuevos += subsidio_estatal

ahorro_costo_mensual = costo_mensual_antiguo - costo_mensual_nuevos

total_nuevos_equipos = num_equipos * precio_nuevos

tiempo_retorno = total_nuevos_equipos / ahorro_costo_mensual

subsidio_subporcionado = subsidio_retiro * total_nuevos_equipos
nuevo_tiempo_retorno = (total_nuevos_equipos - subsidio_subporcionado) / ahorro_costo_mensual

ahorro_gobierno_anual = consumo_subsistencia * tarifa_kwh * (1 - subsidiado_pct) * 12
ahorro_gobierno_total = ahorro_gobierno_anual * 10

st.subheader("Enunciado del ejercicio")
st.markdown("""
**Una familia de estrato 1 tiene instalados 2 aires acondicionados minisplit de 1 TR (12,000 Btu/h) de baja eficiencia que consumen 1.5 kWh/TR aproximadamente. Los equipos operan diariamente 4 horas en promedio. Su tarifa de energía es 800 \$/kWh y es subsidiada por el estado en un 60%. El consumo de subsistencia es de 175 kWh/mes y hasta este valor de consumo cubre el subsidio.
Se les propone cambiar estos sistemas de aire acondicionado por equipos inverter de alta eficiencia, que tienen una eficiencia de 0.75 kWh/TR y que cada uno tiene un precio de 3,000.000 \$.
Teniendo en cuenta el ahorro de energía y el ahorro económico que genera este cambio, determine:**
1. ¿Cuál es ahorro económico que se genera por el cambio de equipos y cuál es el tiempo de retorno simple de la inversión?
2. ¿Cuál es la reducción de emisiones de GEI por la renovación de los equipos?
3. ¿Qué valor de subsidio en la compra de los equipos les podría dar el estado para que la familia pueda cambiar los equipos?
4. Si el gobierno retira el subsidio a la tarifa de energía eléctrica y en su lugar da un subsidio del 50% del costo de compra de los equipos, ¿cuál sería el tiempo de retorno de la inversión para la familia y cuánto dinero ahorraría el gobierno en plazo de 10 años de vida útil de los equipos?
""")


# Resultados
st.subheader("Resultados")
st.write(f"Consumo mensual con equipos antiguos: {consumo_antiguos_mensual:,.2f} kWh")
st.write(f"Consumo mensual con nuevos equipos: {consumo_nuevos_mensual:,.2f} kWh")
st.write(f"Ahorro mensual en energía: {ahorro_energia_mensual:,.2f} kWh")
st.write(f"Costo mensual con equipos antiguos: {costo_mensual_antiguo:,.2f} \$")
st.write(f"Costo mensual con nuevos equipos: {costo_mensual_nuevos:,.2f} \$")
st.write(f"Ahorro mensual en costo: {ahorro_costo_mensual:,.2f} \$")
st.write(f"Total inversión en nuevos equipos: {total_nuevos_equipos:,.2f} \$")
st.write(f"Tiempo de retorno simple de la inversión: {tiempo_retorno:,.2f} meses")

# Descripción de los cálculos con valores numéricos
st.subheader("Descripción de los cálculos")

st.markdown(f"""
### Consumo mensual de energía:
- **Consumo equipos antiguos**: 
  \[
  {equipos_antiguos_cons:,.2f} kWh/TR × 1 TR × {hrs_diarias} horas/día × {num_equipos} equipos × {dias_mes} días = {consumo_antiguos_mensual:,.2f} kWh/mes
  \]
- **Consumo equipos nuevos**:
  \[
  {equipos_nuevos_cons:,.2f} kWh/TR × 1 TR × {hrs_diarias} horas/día × {num_equipos} equipos × {dias_mes} días = {consumo_nuevos_mensual:,.2f} kWh/mes
  \]

### Costos:
- **Subsidio estatal**: 
  \[
  {subsidiado_pct:,.2f} × {tarifa_kwh} \$/kWh × {consumo_subsistencia} kWh/mes = {subsidio_estatal:,.2f} \$
  \]
- **Costo mensual con equipos antiguos**: 
  \[
  ({consumo_antiguos_mensual:,.2f} - {consumo_subsistencia} kWh/mes) × {tarifa_kwh} \$/kWh + {subsidio_estatal:,.2f} \$ = {costo_mensual_antiguo:,.2f} \$
  \]
- **Costo mensual con nuevos equipos**:
  \[
  ({consumo_nuevos_mensual:,.2f} - {consumo_subsistencia} kWh/mes) × {tarifa_kwh} \$/kWh + {subsidio_estatal:,.2f} \$ = {costo_mensual_nuevos:,.2f} \$
  \]

### Ahorro mensual y tiempo de retorno:
- **Ahorro de costos mensuales**: 
  \[
  {costo_mensual_antiguo:,.2f} \$ - {costo_mensual_nuevos:,.2f} \$ = {ahorro_costo_mensual:,.2f} \$
  \]
- **Tiempo de retorno simple**: 
  \[
  {total_nuevos_equipos:,.2f} \$ / {ahorro_costo_mensual:,.2f} \$/mes = {tiempo_retorno:,.2f} meses
  \]
- **Subsidio en la compra**: 
  \[
  {subsidio_retiro:,.2f} × {total_nuevos_equipos:,.2f} \$ = {subsidio_subporcionado:,.2f} \$
  \]

### Cálculos adicionales (con subsidio aplicable):
- **Nuevo costo tarifa**: 
  \[
  {consumo_nuevos_mensual:,.2f} \$ × {tarifa_kwh:,.2f} \$ = {consumo_nuevos_mensual * tarifa_kwh:,.2f} $/mes
  \]
- **Nuevo tiempo de retorno simple**: 
  \[
  ({total_nuevos_equipos:,.2f} \$ - {subsidio_subporcionado:,.2f} \$) / {consumo_nuevos_mensual * tarifa_kwh:,.2f} \$/mes = {(total_nuevos_equipos - subsidio_subporcionado ) / (consumo_nuevos_mensual * tarifa_kwh):,.2f} meses
  \]
- **Ahorro anual del gobierno**: 
  \[
  {consumo_subsistencia:,.2f} \$ × {tarifa_kwh:,.2f} × {1 - subsidiado_pct:,.2f} \$ = {consumo_subsistencia * tarifa_kwh * (1 - subsidiado_pct):,.2f} kWh/mes × 12 = {ahorro_gobierno_anual:,.2f} \$/año
  \]
- **Ahorro total del gobierno en 10 años**:
  \[
  {ahorro_gobierno_anual:,.2f} \$/año × 10 = {ahorro_gobierno_total:,.2f} \$
  \]
""")

# Resultados adicionales
st.subheader("Información adicional")
st.write(f"El estado proporciona un subsidio de: {subsidio_subporcionado:,.2f} \$")
st.write(f"Nuevo tiempo de retorno simple de la inversión: {nuevo_tiempo_retorno:,.2f} meses")
st.write(f"Ahorro anual del gobierno: {ahorro_gobierno_anual:,.2f} \$")
st.write(f"Ahorro total a 10 años del gobierno: {ahorro_gobierno_total:,.2f} \$")

st.write(f"Teniendo en cuenta los datos anteriores, un valor del subsidio de los equipos del 100% y retirando los subsidios estatales en la tarifa, permitiría un retorno de inversión en {(total_nuevos_equipos ) / (ahorro_gobierno_anual):.2f} años, teniendo en cuenta el ahorro anual del gobierno. Es decir que en 6 años recupera lo que se le esta subsidiando a una familia. Siendo la vida util de 10 años de un equipo el gobierno se estaría ahorrando esta diferencia ({ahorro_gobierno_total - num_equipos * precio_nuevos:,.2f}) en terminos de un cambio de legal y aplicar un subsidio.")

st.write(f"La reducción de emisiones de GEI por la renovación de los equipos equivale a {(consumo_antiguos_mensual - consumo_nuevos_mensual) * 100 / consumo_antiguos_mensual:,.2f} %")