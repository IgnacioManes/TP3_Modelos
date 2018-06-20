#!/usr/bin/env python
# -*- coding: latin-1 -*-
import unicodedata
import datetime
from HorariosDIsponibles import *
from SeleccionadorJuegos import *
from dateutil import parser
from colorama import Fore, init
import time
init()
import csv
import random


print(Fore.GREEN + "Iniciando")


class TimeSlot:
    minuto = -1
    duracion = -1

    def __init__(self, minuto, duracion):
        self.minuto = minuto
        self.duracion = duracion

    def __str__(self):
        return str(self.minuto) + ":" + str(self.duracion)

    def __unicode__(self):
        return str(self.minuto) + ":" + str(self.duracion)

    def __repr__(self):
        return str(self.minuto) + ":" + str(self.duracion)

    def __lt__(self, other):
        return self.duracion < other.duracion





def AnalizoArchivo():
    fileEntrada = open('disney.csv', 'r')

    juego = ''
    i = 0
    j = 0
    magia = ''
    tiempo_por_juego = {}
    # Inicializacion tiempos por juego
    for line_number, line in enumerate(fileEntrada):
        if (line_number == 0):
            continue

        line = line.replace('Z\r\n', '')
        arrayArch = line.split(',')
        if ((juego != arrayArch[1]) or (j == 22 and i == 746)): # si es encabezado o la linea final
            # print i
            i = 0

            if (j != 0):
                #print(magia)
                #print("asd")

                slots = []
                for key,value in enumerate(map(int, magia.split(','))):
                    timeSlot = TimeSlot(key,int(value))
                    slots.append(timeSlot)

                tiempo_por_juego['Juego' + str(j)] = slots
            magia = ''
            juego = arrayArch[1]
            #print(juego)
            j = j + 1
        else:
            i = i + 1
            juego = arrayArch[1]

        if (magia == ''):
            magia = arrayArch[2]
        else:
            magia = magia + ',' + arrayArch[2]

    slots = []
    for key, value in enumerate(map(int, magia.split(','))):
        timeSlot = TimeSlot(key, int(value))
        slots.append(timeSlot)

    tiempo_por_juego['Juego' + str(j)] = slots
    array_pizza = []
    slots = []
    for j in range(0, 746 - 1):
    	if(j<46):
        	timeSlot = TimeSlot(j, 40)
        	slots.append(timeSlot)
        else:
        	timeSlot = TimeSlot(j, 400000)
        	slots.append(timeSlot)
    # if(j<):
    # else:
    #	array_pizza(j)=0
    tiempo_por_juego['Juego23'] = slots
    fileEntrada.close()


    return tiempo_por_juego


def SeteoPuntajes():
    puntaje_juegos= {}
    puntaje_juegos['Juego1'] = 1
    puntaje_juegos['Juego2'] = 4
    puntaje_juegos['Juego3'] = 6
    puntaje_juegos['Juego4'] = 6
    puntaje_juegos['Juego5'] = 0
    puntaje_juegos['Juego6'] = 3
    puntaje_juegos['Juego7'] = 5
    puntaje_juegos['Juego8'] = 2
    puntaje_juegos['Juego9'] = 2
    puntaje_juegos['Juego10'] = 4
    puntaje_juegos['Juego11'] = 4
    puntaje_juegos['Juego12'] = 1
    puntaje_juegos['Juego13'] = 6
    puntaje_juegos['Juego14'] = 0
    puntaje_juegos['Juego15'] = 7
    puntaje_juegos['Juego16'] = 10
    puntaje_juegos['Juego17'] = 9
    puntaje_juegos['Juego18'] = 3
    puntaje_juegos['Juego19'] = 2
    puntaje_juegos['Juego20'] = 1
    puntaje_juegos['Juego21'] = 2
    puntaje_juegos['Juego22'] = 2
    puntaje_juegos['Juego23'] = 0
    return puntaje_juegos


def MinutosDelJuegoConMenorWaittime(duraciones):
    min_duracion= 200
    resultado=[]
    for dato in duraciones:
        if(dato.duracion<min_duracion):
            resultado=[dato.minuto]
            min_duracion=dato.duracion
        elif(dato.duracion ==min_duracion):
            resultado.append(dato.minuto)
    for dato in duraciones:
    	if dato.duracion==min_duracion:
    		duraciones.remove(dato)
    return resultado

def main():
    duraciones_juegos = AnalizoArchivo()
    horarios_disponibles=HorariosDIsponibles(1000)
     # inicializacion indispensables
    indispensables = [1,3,4,7,9,13,15,16,21,22]
    minuto_disponible = 0 
    minutos_zapi=range(45)

    minutos_zapi=sorted(minutos_zapi, key=lambda k: random.random()) 
    horarios_disponibles.AgregarActivdad("Juego23", 45, 40)


    for juego in sorted(indispensables, key=lambda k: random.random()):
        sigo_buscando=True
        nombre_juego = 'Juego' + str(juego)

        time_slots_juego_actual= duraciones_juegos[nombre_juego]
        minutos_minimos=MinutosDelJuegoConMenorWaittime(time_slots_juego_actual)
        print minutos_minimos
        minuto= minutos_minimos.pop(0) #Agarro alguno que es minimo podria ser random
        minuto_disponible= horarios_disponibles.EncontrarMinutoDisponible(minuto)

        #minuto_disponible = horarios_disponibles.EncontrarMinutoDisponible(minuto_disponible)


        while(minuto_disponible!=None and sigo_buscando): #si no recorro en orden voy a tener que modificar eso
            print nombre_juego+" "+str(minuto_disponible)
            duracion_juego_min_actual= duraciones_juegos[nombre_juego][minuto_disponible].duracion
            if(horarios_disponibles.EstanDisponiblesMinutos(minuto_disponible , duracion_juego_min_actual)):
                sigo_buscando=False
                """if (juego==14):
            		print str(nombre_juego )+" "+str( minuto_disponible)+" "+ str(duracion_juego_min_actual)
            	"""
                horarios_disponibles.AgregarActivdad(nombre_juego, minuto_disponible, duracion_juego_min_actual)

            else:
                if len(minutos_minimos)==0:
                    minutos_minimos = MinutosDelJuegoConMenorWaittime(time_slots_juego_actual)
                print minutos_minimos
                minuto = minutos_minimos.pop()
                minuto_disponible= horarios_disponibles.EncontrarMinutoDisponible(minuto)
                #minuto_disponible = horarios_disponibles.EncontrarMinutoDisponible(minuto_disponible)

    
    puntaje_juegos = SeteoPuntajes()
    
    seleccionador_juegos = SeleccionadorJuegos(duraciones_juegos,puntaje_juegos, horarios_disponibles )
	
    print(horarios_disponibles)
    
    if seleccionador_juegos.chequearResticciones(horarios_disponibles) :
    	"""
    	print(horarios_disponibles.MinutosLibres())
    	"""
    	print("Puntaje: "+str(horarios_disponibles.Puntaje(puntaje_juegos)))
	

#tiempo =  int(round(time.time() * 1000))
main()
#print"Tiempo transcurrido " + str( int(round(time.time() * 1000))-tiempo) +" ms"