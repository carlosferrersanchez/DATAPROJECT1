import time

from scripts.criba_bbdd import criba 
from scripts.valoraciones import valoraciones 
from scripts.plazas_disponibles import plazas_disponibles 
from scripts.personas import personas
from scripts.asignacion_plazas import asignacion
from scripts.generador_csv import exportar_a_csv

personas()
time.sleep(2)  
plazas_disponibles()
time.sleep(2)  
criba()
time.sleep(2)  
valoraciones()
time.sleep(2)  
asignacion()
time.sleep(2)
exportar_a_csv('personas', 'personas.csv')
exportar_a_csv('lista_espera', 'lista_espera.csv')
exportar_a_csv('plazas_disponibles', 'plazas_disponibles.csv')
exportar_a_csv('viajes_asignados', 'viajes_asignados.csv')