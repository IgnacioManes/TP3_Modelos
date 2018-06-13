#!/usr/bin/env python
# -*- coding: latin-1 -*-
import unicodedata
import datetime
from HorariosDIsponibles import *
from SeleccionadorJuegos import *
from dateutil import parser
from colorama import Fore, init

init()
import csv

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
        timeSlot = TimeSlot(j, 40)
        slots.append(timeSlot)
    # if(j<):
    # else:
    #	array_pizza(j)=0
    tiempo_por_juego['Juego23'] = slots
    fileEntrada.close()


    return tiempo_por_juego


def SeteoPuntajes():
    puntaje_juegos= {}
    puntaje_juegos['Juego1'] = 3
    puntaje_juegos['Juego2'] = 4
    puntaje_juegos['Juego3'] = 5
    puntaje_juegos['Juego4'] = 10
    puntaje_juegos['Juego5'] = 7
    puntaje_juegos['Juego6'] = 2
    puntaje_juegos['Juego7'] = 3
    puntaje_juegos['Juego8'] = 4
    puntaje_juegos['Juego9'] = 6
    puntaje_juegos['Juego10'] = 1
    puntaje_juegos['Juego11'] = 9
    puntaje_juegos['Juego12'] = 2
    puntaje_juegos['Juego13'] = 0
    puntaje_juegos['Juego14'] = 6
    puntaje_juegos['Juego15'] = 2
    puntaje_juegos['Juego16'] = 4
    puntaje_juegos['Juego17'] = 2
    puntaje_juegos['Juego18'] = 6
    puntaje_juegos['Juego19'] = 1
    puntaje_juegos['Juego20'] = 0
    puntaje_juegos['Juego21'] = 1
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
    return resultado

def funcionClaveNachoCrudo():
    duraciones_juegos = AnalizoArchivo()
    horarios_disponibles=HorariosDIsponibles(1000)
     # inicializacion indispensables
    indispensables = (3, 4, 5, 6, 9, 14, 15, 18, 19, 22, 23)
    minuto_disponible = 0

    for juego in sorted(indispensables):
        sigo_buscando=True
        nombre_juego = 'Juego' + str(juego)

        time_slots_juego_actual= duraciones_juegos[nombre_juego]
        minutos_minimos=MinutosDelJuegoConMenorWaittime(time_slots_juego_actual)
        minuto= minutos_minimos.pop(0) #Agarro alguno que es minimo podria ser random
        minuto_disponible= horarios_disponibles.EncontrarMinutoDisponible(minuto)
        #minuto_disponible = horarios_disponibles.EncontrarMinutoDisponible(minuto_disponible)


        while(minuto_disponible!=None and sigo_buscando): #si no recorro en orden voy a tener que modificar eso

            duracion_juego_min_actual= duraciones_juegos[nombre_juego][minuto_disponible].duracion
            if(horarios_disponibles.EstanDisponiblesMinutos(minuto_disponible , duracion_juego_min_actual)):
                sigo_buscando=False
                """if (juego==14):
            		print str(nombre_juego )+" "+str( minuto_disponible)+" "+ str(duracion_juego_min_actual)
            	"""
                horarios_disponibles.AgregarActivdad(nombre_juego, minuto_disponible, duracion_juego_min_actual)

            else:
            	"""	if (juego==14):
            		print len(minutos_minimos)
            	"""
                if len(minutos_minimos)==0:
                    minutos_minimos = MinutosDelJuegoConMenorWaittime(time_slots_juego_actual)

                minuto = minutos_minimos.pop()
                minuto_disponible= horarios_disponibles.EncontrarMinutoDisponible(minuto)
                #minuto_disponible = horarios_disponibles.EncontrarMinutoDisponible(minuto_disponible)

    


    puntaje_juegos = SeteoPuntajes()
    seleccionador_juegos=SeleccionadorJuegos(duraciones_juegos,puntaje_juegos, horarios_disponibles )

    print(horarios_disponibles)
    print(horarios_disponibles.MinutosLibres())
    print("Puntaje"+str(horarios_disponibles.Puntaje(puntaje_juegos)))








    """
        horarios_ocupados = {}
        horarios_juegos = {}        
        tiempos_por_juego = map(lambda x: x.duracion, duraciones_juegos[nombre_juego])
        maximo = max(tiempos_por_juego)
        asignar = False
        cotaSuperior = 0
        cotaInferior = 0
        tiempo_juego = 1 # no deberia ser 0 ?
        horario = 0
        while (tiempo_juego <= maximo):
            aux = 0
            for i in range(0, len(tiempos_por_juego) - 1):
                if (tiempos_por_juego[i] == tiempo_juego and i not in horarios_ocupados.keys()):
                    asignar = True
                    if (tiempo_juego == 0):
                        cota = 0
                    else:
                        cota = tiempo_juego - 1
                    for j in range(1, tiempo_juego - 1):
                        if (i + j in horarios_ocupados.keys()):
                            asignar = False
                            break
                    if (asignar):
                        for j in range(0, cota):
                            horarios_ocupados[i + j] = nombre_juego
                        horarios_juegos[i] = (nombre_juego, tiempo_juego)
                        break
            if (not asignar):
                tiempo_juego = tiempo_juego + 1
            else:
                tiempo_juego = maximo + 1

    for i in sorted(horarios_ocupados):
        print str(i) + " " + str(horarios_ocupados[i])
    for i in sorted(horarios_juegos):
        print str(i) + str(horarios_juegos[i])

    # puntajes por juego
    puntaje_juegos = SeteoPuntajes()

    puntaje = 0
    for i in sorted(horarios_juegos):
        puntaje = puntaje + puntaje_juegos[horarios_juegos[i][0]]
    print "Puntaje " + str(puntaje)



		while(tiempo_juego<=maximo):
			aux=0
			for i in range(0, len(tiempo_por_juego[juego])-1):
				if(tiempo_por_juego[juego][i]==tiempo_juego and i not in horarios_ocupados.keys()):
					asignar=True
					for j in horarios_ocupados.keys():
						cotaSuperior=j*10+(horarios_ocupados[j][1])
						cotaInferior=j*10
						horarioAAsignar=i*10
						if(horarioAAsignar<cotaSuperior and horarioAAsignar>=cotaInferior):
							asignar=False
							break
					if(asignar):
						print juego
						print i*10
						print cotaInferior
						print cotaSuperior
						horario=i
						break
			if(not asignar):
				tiempo_juego=tiempo_juego+5
			else:
				aux=tiempo_juego
				tiempo_juego=maximo+1
		horarios_ocupados[horario]=(juego,aux)

	for i in (horarios_ocupados):
		print str(i)+str(horarios_ocupados[i])
"""
funcionClaveNachoCrudo()
