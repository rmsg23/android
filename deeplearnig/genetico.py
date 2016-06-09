from random import random , randint , sample
from collections import namedtuple

#Calcula el capital invertido por un individuo
def capitalInvertido(individuo):
	return sum(map(lambda x,y: x*y.precio,individuo,inversiones))

#Calculaelrendimientoobtenidoporunindividuo
def rendimiento(individuo):
	return sum(map(lambda x,y: x*y.precio*y.rendim,individuo,inversiones))

#Si un individuo gastamas capital del disponible,se eliminan
#aleatoriamente inversiones hasta que se ajusta al capital

def ajustaCapital(individuo):
	ajustado=individuo[:]
	while capitalInvertido(ajustado)>capital:
		pos=randint(0,len(ajustado)-1)
		if ajustado[pos]>0:
			ajustado[pos]-=1
	return ajustado

#Crea un individuo al azar,en este caso una seleccion de
#inversiones que no excedan el capital disponible

def creaIndividuo(inversiones,capital):
	individuo=[0]*len(inversiones)
	while capitalInvertido(individuo)<capital:
		eleccion=randint(0,len(inversiones)-1)
		individuo[eleccion]+=1
	return ajustaCapital(individuo)

#Crea un nuevo individuo cruzando otros dos(cuyas posiciones se
#indican en el segundo parametro)
def cruza(poblacion,posiciones):
	L=len(poblacion[0])
	#Toma los genes del primer progenitor y luego toma al azar
	#un segmento de entre 1 y L genes del segundo progenitor
	hijo=poblacion[posiciones[0]][:]
	inicio=randint(0,L-1)
	fin=randint(inicio+1,L)
	hijo[inicio:fin]=poblacion[posiciones[1]][inicio:fin]
	return ajustaCapital(hijo)

#Aplica mutaciones a un individuo segun una tasa dada;garantiza
#que cumple las restricciones de capital e inversiones
def muta(individuo,tasaMutacion):
	mutado=[]
	for i in range(len(individuo)):
		if random()>tasaMutacion:
			mutado.append(individuo[i])
		else:
			mutado.append(randint(0,inversiones[i].cantidad))
	return ajustaCapital(mutado)

#Hace evolucionar el sistema durante un numero de generaciones

def evoluciona(poblacion,generaciones):
	#Ordena la poblacion inicial por rendimiento producido
	poblacion.sort(key=lambda x: rendimiento(x))
	#Algunos valores utiles
	N=len(poblacion)
	tasaMutacion=0.01
	#Genera una lista del tipo [0,1,1,2,2,2,3,3,3,3,...] para
	#representar las probabilidades de reproducirse de cada
	#individuo (el primero 1 posibilidad, elsegundo 2,etc.)
	reproduccion=[x for x in range(N) for y in range(x+1)]
	for i in range (generaciones):
		#Se generan N-1 nuevos individuos cruzando los existentes
		#(sin que se repitan los padres)
		padres=sample(reproduccion,2)
		while padres[0]==padres[1]:
			padres=sample(reproduccion,2)
		hijos=[cruza(poblacion,padres)for x in range(N-1)]
		#Se aplican mutaciones con una cierta probabilidad
		hijos=[muta(x,tasaMutacion)for x in hijos]
		#Se anade el mejor individuo de la poblacion anterior
		#(elitismo)
		hijos.append(poblacion[-1])
		poblacion=hijos
		#Se ordenan los individuos por rendimiento
		poblacion.sort(key=lambda x: rendimiento(x))
	
	#Devuelve el mejor individuo encontrado
	return poblacion[-1]

#------------------main():--------------------------------------------

#Declara una tupla con nombres para representar cada inversion
Inversion=namedtuple("Inversion",["precio","cantidad","rendim"])
numInver=100
maxPrecio=1000
maxCant=10
maxRend=0.2
#Genera una lista de tuplas Inversion
inversiones=[Inversion(random()*maxPrecio,randint(1,maxCant),random()*maxRend)for i in range(numInver)]
print(inversiones)


generaciones=1000
capital=50000
individuos=20
print("\n\ngenerando la poblacion..\n\n")
poblacion=[creaIndividuo(inversiones,capital) for i in range(individuos)]
#Nota:para simplificar el programa se accede a inversiones y
#capital de forma global(solo se leen,no se modifican)

print("corriendo evolucion de ",generaciones," generaciones....")
mejor=evoluciona(poblacion,generaciones)
print(mejor,capitalInvertido(mejor),rendimiento(mejor))
