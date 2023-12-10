import time

from scripts.criba_bbdd import criba 
from scripts.valoraciones import valoraciones 
from scripts.plazas_disponibles import plazas_disponibles 
from scripts.personas import personas
from scripts.asignacion_plazas import asignacion

personas()
time.sleep(2)  
plazas_disponibles()
time.sleep(2)  
criba()
time.sleep(2)  
valoraciones()
time.sleep(2)  
asignacion()