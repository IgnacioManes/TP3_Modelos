#!/usr/bin/env python
# -*- coding: latin-1 -*-
import unicodedata
import datetime
from dateutil import parser
from colorama import Fore, init
init()
import csv

print(Fore.GREEN + "Iniciando")

def funcionClaveNachoCrudo():
	fileEntrada = open('disney.csv', 'r') 

	encabezado = fileEntrada.readline().replace('\n','')
	fecha_inicial=datetime.datetime(2018,4,21,13,14,52,0,None)
	juego = ''
	i = 0
	j = 0
	magia = ''
	tiempo_por_juego = {}
	#Inicializacion tiempos por juego
	for line in fileEntrada:
		line = line.replace('Z\r\n','')
		arrayArch = line.split(',')
		if ((juego != arrayArch[1] ) or (j == 22 and i == 746)):
			#print i
			i = 0
			
			if (j != 0):
				tiempo_por_juego['Juego'+str(j)]=map(int,magia.split(','))
			magia = ''
			juego = arrayArch[1]
			j = j +1
		else:
			i = i +1
			juego = arrayArch[1]
		if(magia==''):
			magia =  arrayArch[2]
		else:
			magia =  magia + ',' + arrayArch[2]
	tiempo_por_juego['Juego'+str(j)]=map(int,magia.split(','))
	array_pizza = []
	for j in range(0, 746-1):
		array_pizza.append(40)
		#if(j<):
		#else:
		#	array_pizza(j)=0
	tiempo_por_juego['Juego23']=array_pizza
	fileEntrada.close()
	#inicializacion indispensables
	indispensables=(3,4,5,6,9,14,15,18,19,22,23)
	horarios_ocupados={}
	horarios_juegos={}
	"""
	for i in (tiempo_por_juego):
		print str(i)+' '+str(len(tiempo_por_juego[i]))
	"""
	for juego in sorted(indispensables):
		juego_str='Juego'+str(juego)
		#print len(tiempo_por_juego[juego])
		maximo=max(tiempo_por_juego[juego_str])
		asignar=False
		cotaSuperior=0
		cotaInferior=0
		tiempo_juego=1
		horario=0
		while(tiempo_juego<=maximo):
			aux=0
			for i in range(0, len(tiempo_por_juego[juego_str])-1):
				if(tiempo_por_juego[juego_str][i]==tiempo_juego and i not in horarios_ocupados.keys()):
					asignar=True
					if(tiempo_juego==0):
						cota=0
					else:
					 	cota=tiempo_juego-1
					for j in range(1, tiempo_juego-1):
						if(i+j in horarios_ocupados.keys()):
							asignar=False
							break
					if(asignar):
						for j in range(0,cota):
							horarios_ocupados[i+j]=juego_str
						horarios_juegos[i]=(juego_str,tiempo_juego)
						break
			if(not asignar):
				tiempo_juego=tiempo_juego+1
			else:
				tiempo_juego=maximo+1
	
	for i in sorted(horarios_ocupados):
		print str(i)+" "+str(horarios_ocupados[i])
	for i in sorted(horarios_juegos):
		print str(i)+str(horarios_juegos[i])
	#puntajes por juego
	puntaje_juegos={}

	puntaje_juegos['Juego1']=3
	puntaje_juegos['Juego2']=4
	puntaje_juegos['Juego3']=5
	puntaje_juegos['Juego4']=10
	puntaje_juegos['Juego5']=7
	puntaje_juegos['Juego6']=2
	puntaje_juegos['Juego7']=3
	puntaje_juegos['Juego8']=4
	puntaje_juegos['Juego9']=6
	puntaje_juegos['Juego10']=1
	puntaje_juegos['Juego11']=9
	puntaje_juegos['Juego12']=2
	puntaje_juegos['Juego13']=0
	puntaje_juegos['Juego14']=6
	puntaje_juegos['Juego15']=2
	puntaje_juegos['Juego16']=4
	puntaje_juegos['Juego17']=2
	puntaje_juegos['Juego18']=6
	puntaje_juegos['Juego19']=1
	puntaje_juegos['Juego20']=0
	puntaje_juegos['Juego21']=1
	puntaje_juegos['Juego22']=2
	puntaje_juegos['Juego23']=0


	puntaje=0
	for i in sorted(horarios_juegos):
		puntaje= puntaje+puntaje_juegos[horarios_juegos[i][0]]
	print "Puntaje "+str(puntaje)
"""
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