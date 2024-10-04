import pyautogui as pg #importar libreria
import time 

veces = int(input("CUANTAS VECES SE REPITE: "))
mensaje = input("INGRESA EL MENSAJE: ")

time.sleep(3)

for i in range(veces):
    pg.write(f'{i+1}: {mensaje}')
    pg.press('enter')
