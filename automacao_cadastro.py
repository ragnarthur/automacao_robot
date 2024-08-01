import pandas as pd
import robot

# Lendo arquivo excel
df = pd.read_excel('cadastro_clientes.xlsx')

# Executando o cadastro
robot.cadastro_web(df)
