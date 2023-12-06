personas_imserso = []

from faker import Faker
import pandas as pd
from gender_guesser.detector import Detector
from datetime import datetime, timedelta
import numpy as np
import random
from scipy.stats import skewnorm
import random
import pandas as pd

def generar_identidad():
  nombre = fake.first_name()
  apellido_1 = fake.last_name()
  apellido_2 = fake.last_name()

  genero_estimado = gender_detector.get_gender(nombre.split()[0])

  if genero_estimado == "male":
    sexo = "Masculino"
  elif genero_estimado == "female":
    sexo = "Femenino"
  else:
    sexo = random.choice(["Masculino", "Femenino"])

  nacionalidad = 'España'
  return{
      "Nombre": nombre,
      "Primer_apellido": apellido_1,
      "Segundo_apellido": apellido_2,
      "Sexo": sexo,
      "Nacionalidad": nacionalidad
  }

def calcular_letra_dni(numero_dni):
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    indice_letra = int(numero_dni) % 23
    letra = letras_dni[indice_letra]
    return letra

def calcular_letra_nie(nie):
  letras = {'X': 0, 'Y': 1, 'Z': 2}
  primera_letra = nie[0]
  valor_letra = str(letras[primera_letra])
  nie_numeros = valor_letra + nie[1:8]
  letras = "TRWAGMYFPDXBNJZSQVHLCKE"
  indice_letra = int(nie_numeros) % 23
  letra = letras[indice_letra]
  return letra

def generar_dni(fila):
        dni = str(random.randint(1, 99999999)).zfill(8)
        letra_dni = calcular_letra_dni(dni)
        return dni + letra_dni

def generar_NIE(fila):
    letra1_nie = random.choice(['X', 'Y', 'Z'])
    numeros_nie = str(random.randint(1,9999999)).zfill(7)
    nie = letra1_nie + numeros_nie
    letra2_nie = calcular_letra_nie(nie)
    nie = nie + letra2_nie
    return nie

def generar_numero_telefono():
  codigo_pais = "+34"
  prefijo_operadora = random.choices(["6", "7"], weights=[0.9, 0.1])[0]
  resto_numero = ''.join(random.choice('0123456789') for i in range(8))
  numero_telefono = f"{codigo_pais}{prefijo_operadora}{resto_numero}"
  return numero_telefono

def generar_fecha_nacimiento():
    fecha_actual = datetime.now()
    edad_minima = 50
    edad_maxima = 85
    dias_de_edad = random.randint(edad_minima * 365, edad_maxima * 365)
    fecha_nacimiento = fecha_actual - timedelta(days=dias_de_edad)
    return fecha_nacimiento.strftime("%Y-%m-%d")


def generar_provincia():
  faker = Faker('es_ES')
  provincia = faker.region()
  return provincia

def generar_estado_civil():
  estado_civil = random.choices(["Casado", "Soltero", "Viudo", "Divorciado"], weights = [0.65, 0.05, 0.15, 0.15])[0]
  return estado_civil

def acompanamiento_pareja(estado_civil):
  if estado_civil == "Casado":
    pareja = random.choices([True, False], weights=[0.9, 0.1])[0]
  else:
    pareja = random.choices([True, False], weights = [0.1, 0.9])[0]
  return pareja == True

def hijo_discapacidad():
  hijo = random.choices([True, False], weights=[0.01, 0.99])[0]
  return hijo == True

def discapacidad():
  discapacidad = random.choices([True, False], weights=[0.03, 0.99])[0]
  return discapacidad == True

def tipo_discapacidad():
  tipo_discapacidad = random.choice(["Fisica", "Auditiva", "Visual", "Sordoceguera", "Intelectual", "Psicosocial", "Multiple"])
  return tipo_discapacidad

def grado_discapacidad():
  grado_discapacidad = random.randint(1, 4)
  return grado_discapacidad

def numero_participaciones():
  numero_participaciones = np.random.normal(2, 1)
  numero_participaciones = max(0,numero_participaciones)
  numero_participaciones = int(numero_participaciones)
  return numero_participaciones

def renta():
  renta = skewnorm.rvs(1.5, loc=25000, scale=15000)
  renta = max(6700,renta)
  renta = int(renta)
  return renta

def personas_dependientes(hijo_discapacidad):
  personas_dependientes = np.random.normal(0, 0.5)
  personas_dependientes = max(0,personas_dependientes)
  personas_dependientes = int(personas_dependientes)
  if hijo_discapacidad:
    personas_dependientes = personas_dependientes+1
  return personas_dependientes

def calcular_edad(fecha_nacimiento):
  hoy = datetime.now()
  edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
  return edad

def pensionista (estado_civil, edad, pais_residencia):
  pensionista = None
  if random.random() < 0.13:
    pensionista = "Desempleo/Otros subsidios"
  if edad > 64 and random.random() < 0.9:
    pensionista = "Jubilacion"
  if estado_civil == "Viudo":
    pensionista = "Viuedad"
  if pais_residencia != "España" and edad > 64 and random.random() < 0.9:
    pensionista = "Extranjero"
  if pensionista == None:
    pensionista = "Titular SS"
  return pensionista

def obras_sociales():
    if random.random() <= 0.32:
        obras_sociales = random.choices(["1-6 dias", "7-30 dias", "1-3 meses", "+3 meses"], weights=[0.5, 0.25, 0.125, 0.125])[0]
    else:
        obras_sociales = "No"
    return obras_sociales

def vive_solo(estado_civil):
    if estado_civil == "Casado":
        vive_solo = False
    else:
        vive_solo = random.choices([True, False], weights=[0.3, 0.7])[0]
    return vive_solo

def elegir_preferencias():
  preferencia = random.choice(["Montaña", "Cultural", "Rural", "Islas", "Playa", "Gastronómico"])
  return preferencia

def elegir_preferencia_2(preferencia_1):
    preferencias = ["Montaña", "Cultural", "Rural", "Islas", "Playa", "Gastronómico"]
    preferencias.remove(preferencia_1) 
    return random.choice(preferencias)

def elegir_meses(fechas_seleccionadas):
    meses_disponibles = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    for fecha in fechas_seleccionadas:
        meses_disponibles.remove(fecha) 
    return random.choice(meses_disponibles)

fake = Faker('es_ES')
gender_detector = Detector()

personas_imserso = [generar_identidad() for _ in range(3000)]
numero_extranjeros = random.randint(0,50)
for i in range(3000 - numero_extranjeros, 3000):
  fake = Faker()
  personas_imserso[i]["Segundo_apellido"] = None
  personas_imserso[i]["Nombre"] = fake.first_name()
  personas_imserso[i]["Primer_apellido"] = fake.last_name()
  genero_estimado = gender_detector.get_gender(personas_imserso[i]["Nombre"])
  if genero_estimado == "male":
    personas_imserso[i]["Sexo"] = "Masculino"
  elif genero_estimado == "female":
    personas_imserso[i]["Sexo"] = "Femenino"
  else:
    personas_imserso[i]["Sexo"] = random.choice(["Masculino", "Femenino"])
  personas_imserso[i]["Nacionalidad"] = fake.country()

print("-------------------------------------------------------------\n"
      "Generando Database...\n"
      "-------------------------------------------------------------")

personas_imserso = pd.DataFrame(personas_imserso)

personas_imserso['Segundo_apellido'] = personas_imserso['Segundo_apellido'].fillna('')

personas_imserso['DNI'] = personas_imserso.apply(lambda fila: generar_dni(fila) if fila['Nacionalidad'] == 'España' else generar_NIE(fila), axis=1)

personas_imserso['Telefono'] = personas_imserso.apply(lambda fila: generar_numero_telefono(), axis=1)

personas_imserso['Pais_residencia'] = "España"

personas_imserso = personas_imserso[::-1]

numero_no_residentes = random.randint(0, 50)

indices_seleccionados = personas_imserso.index[-numero_no_residentes:]
paises_generados = [fake.country() for _ in range(numero_no_residentes)]

if len(indices_seleccionados) == len(paises_generados):
    personas_imserso.loc[indices_seleccionados, 'Pais_residencia'] = paises_generados
    personas_imserso = personas_imserso.sample(frac=1).reset_index(drop=True)
    print("Valores asignándose correctamente...")
else: 
    print("La longitud de los indices seleccionados no coincide con la lista de paises generados")

personas_imserso['Fecha_nacimiento'] = personas_imserso.apply(lambda fila: generar_fecha_nacimiento(), axis=1)

personas_imserso['Edad'] = pd.to_datetime(personas_imserso['Fecha_nacimiento'], format='%Y-%m-%d', errors='coerce').apply(calcular_edad)

personas_imserso['Provincia'] = personas_imserso.apply(lambda fila: generar_provincia() if fila['Pais_residencia'] == 'España' else None, axis=1)
personas_imserso['Provincia'] = personas_imserso['Provincia'].fillna('')


personas_imserso['Estado_civil'] = personas_imserso.apply(lambda fila: generar_estado_civil(), axis=1)

personas_imserso['Acompanamiento_pareja'] = personas_imserso['Estado_civil'].apply(acompanamiento_pareja)

personas_imserso['Hijo_discapacidad'] = personas_imserso.apply(lambda fila: hijo_discapacidad(), axis=1)

personas_imserso['Discapacidad'] = personas_imserso.apply(lambda fila: discapacidad(), axis=1)

personas_imserso['Tipo_discapacidad'] = personas_imserso.apply(lambda fila: tipo_discapacidad() if fila['Discapacidad'] == True else None, axis=1)
personas_imserso['Tipo_discapacidad'] = personas_imserso['Tipo_discapacidad'].fillna('')


personas_imserso['Grado_discapacidad'] = personas_imserso.apply(lambda fila: grado_discapacidad() if fila['Discapacidad'] == True else None, axis=1)
personas_imserso['Grado_discapacidad'] = personas_imserso['Grado_discapacidad'].fillna(0)


personas_imserso['Numero_participaciones'] = personas_imserso.apply(lambda fila: numero_participaciones(), axis = 1)

personas_imserso['Renta'] = personas_imserso.apply(lambda fila: renta(), axis = 1)

personas_imserso['Personas_dependientes'] = personas_imserso['Hijo_discapacidad'].apply(personas_dependientes)

personas_imserso["Pension"] = personas_imserso.apply(lambda fila: pensionista(fila["Estado_civil"], fila["Edad"], fila["Pais_residencia"]), axis=1)

personas_imserso['Obras_sociales'] = personas_imserso.apply(lambda fila: obras_sociales(), axis=1)

personas_imserso['Vive_solo'] = personas_imserso['Edad'].apply(vive_solo)

personas_imserso['Preferencia_1'] = personas_imserso.apply(lambda x: elegir_preferencias(), axis=1)

personas_imserso['Preferencia_2'] = personas_imserso.apply(lambda x: elegir_preferencia_2(x['Preferencia_1']), axis=1)

personas_imserso['Fecha_1'] = personas_imserso.apply(lambda x: elegir_meses([]), axis=1)

personas_imserso['Fecha_2'] = personas_imserso.apply(lambda x: elegir_meses([x['Fecha_1']]), axis=1)

personas_imserso['Fecha_3'] = personas_imserso.apply(lambda x: elegir_meses([x['Fecha_1'], x['Fecha_2']]), axis=1)


print("-------------------------------------------------------------\n"
      "Database Creada Correctamente\n"
      "-------------------------------------------------------------")