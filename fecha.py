import os, sqlite3
import text6 from Proyecto

text6 = fecha
def edad(fecha, mes):
    if fecha == 'ENE':
        mes = 1
    elif fecha == 'FEB':
        mes = 2
    elif fecha == 'MAR':
        mes = 3
    elif fecha == 'ABR':
        mes = 4
    elif fecha == 'MAY':
        mes = 5
    elif fecha == 'JUN':
        mes = 6
    elif fecha == 'JUL':
        mes = 7
    elif fecha == 'AGO':
        mes = 8
    elif fecha == 'SEP':
        mes = 9
    elif fecha == 'OCT':
        mes = 10
    elif fecha == 'NOV':
        mes = 11
    elif fecha == 'DIC':
        mes = 12
    return mes

Cursor.execute("COMPARE INTO CIUDADANOS EDAD ( TYPE EDAD('"+text6+mes"'))
    