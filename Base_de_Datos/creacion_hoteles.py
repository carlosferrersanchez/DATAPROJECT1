import pandas as pd
import numpy as np
import random

data = {'Provincia': [], 'Mes': [], 'Rating': [], 'Estrellas': []}

provincias = ['Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila', 'Badajoz', 'Barcelona', 'Burgos', 'Cáceres', 'Cádiz', 'Cantabria', 'Castellón', 'Ciudad Real', 'Córdoba', 'Cuenca', 'Gerona', 'Granada', 'Guadalajara', 'Guipúzcoa', 'Huelva', 'Huesca', 'Islas Balears', 'Jaén', 'La Coruña', 'La Rioja', 'Las Palmas', 'León', 'Lérida', 'Lugo', 'Madrid', 'Málaga', 'Murcia', 'Navarra', 'Orense', 'Palencia', 'Pontevedra', 'Salamanca', 'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Santa Cruz de Tenerife', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Vizcaya', 'Zamora', 'Zaragoza']
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

for provincia in provincias:
    rating = np.clip(round(np.random.normal(loc=3, scale=1), 1), 0.1, 5.0)
    estrellas = random.randint(3,5)
    for mes in meses:
        data['Provincia'].append(provincia)
        data['Mes'].append(mes)
        data['Rating'].append(rating)
        data['Estrellas'].append(estrellas)

df = pd.DataFrame(data)
print(df)