import numpy as np
import time

class Redneuronal(object):

	def __init__(self, entradas, oculta, salidas, activation='tanh', output_act='softmax'):
		
		# funcion de activacion a usar en las capas de la red
		if activation == 'sigmoide':
			self.activation = sigmoide
			self.activation_derivada = sigmoide_derivada
		elif activation == 'tanh':
			self.activation = tanh
			self.activation_derivada = tanh_derivada
		elif activation == 'lineal':
			self.activation = lineal
			self.activation_derivada = lineal_derivada

		# funcion de activacion de la capa de salida
		if output_act == 'sigmoide':
			self.output_act = sigmoide
			self.derivada_salida = sigmoide_derivada
		elif output_act == 'tanh':
			self.output_act = tanh
			self.derivada_salida = tanh_derivada
		elif output_act == 'lineal':
			self.output_act = lineal
			self.derivada_salida = lineal_derivada
		elif output_act == 'softmax':
			self.output_act = softmax
			self.derivada_salida = lineal_derivada

		# inicializacion de los pesos
		self.wi = np.random.randn(entradas, oculta)/np.sqrt(entradas)
		self.wo = np.random.randn(oculta + 1, salidas)/np.sqrt(oculta)

		# inicalizacion de la variacion de los pesos
		self.updatei = 0
		self.updateo = 0


	def feedforward(self, X):

		# calculando la salida de la capa oculta
		ah = self.activation(np.dot(X, self.wi))
			
		# agregando el bias al resultado anterior
		ah = np.concatenate((np.ones(1).T, np.array(ah)))

		# salidas
		y = self.output_act(np.dot(ah, self.wo))

		# salida de la red
		return y


	def ajuste(self, X, y, fases=10, tasa_aprendizaje=0.2, tasa_aprendizaje_decadencia = 0 , momentum = 0, imprimir = 0):
		
		# tiempo
		startTime = time.time()

		# for de las fases 
		for k in range(fases):
	
			# induccion de los datos
			for i in range(X.shape[0]):

				#print("----------------------------\nX[i]:\n")
				#print(X[i])
				#print("======\nself.wi:\n")
				#print(self.wi)
				#print("----------------------------\n")

				# calculo de la salida de la capa oculta
				ah = self.activation(np.dot(X[i], self.wi))
			
				# agrega el bias a la capa oculta
				ah = np.concatenate((np.ones(1).T, np.array(ah))) 

				# calculo de la salida
				ao = self.output_act(np.dot(ah, self.wo))

				#-----------propagacion hacia atras--------------------------------------

				# Deltas	
				deltao = np.multiply(self.derivada_salida(ao),y[i] - ao)
				deltai = np.multiply(self.activation_derivada(ah),np.dot(self.wo, deltao))

				# actualizacion de los pesos con el momentum
				self.updateo = momentum*self.updateo + np.multiply(tasa_aprendizaje, np.outer(ah,deltao))
				self.updatei = momentum*self.updatei + np.multiply(tasa_aprendizaje, np.outer(X[i],deltai[1:]))

				# Weights update
				self.wo += self.updateo
				self.wi += self.updatei

			# Print training status
			if imprimir == 1:
				print 'Fase: {0:4d}/{1:4d}\t\tTasa de aprendizaje: {2:4f}\t\tTiempo (segundos): {3:5f}'.format(k,fases,tasa_aprendizaje, time.time() - startTime)
				
			# Learning rate update
			tasa_aprendizaje = tasa_aprendizaje * (1 - tasa_aprendizaje_decadencia)

	def prediccion(self, X): 

		# crear matrix de salida
		y = np.zeros([X.shape[0],self.wo.shape[1]])

		# ciclo sobre las entradas
		for i in range(0,X.shape[0]):
		# 	print("----------------------------\nentrada X[",i,"]:\n")
		# 	print(X[i])
		# 	print("----------------------------\n")
			y[i] = self.feedforward(X[i])

		# 	print("----------------------------\nsalida y[",i,"]:\n")
		# 	print(y[i])
		# 	print("----------------------------\n")

		# Return the results
		#print("----------------------------\nsalida y:\n")
		#print(y)
		#print("----------------------------\n")
		return y


# funciones de activacion
def sigmoide(x):
	return 1.0/(1.0 + np.exp(-x))

def sigmoide_derivada(x):
	return sigmoide(x)*(1.0-sigmoide(x))

def tanh(x):
	return np.tanh(x)

def tanh_derivada(x):
	return 1.0 - x**2

def softmax(x):
    return (np.exp(np.array(x)) / np.sum(np.exp(np.array(x))))

def softmax_derivada(x):
    return softmax(x)*(1.0-softmax(x))

def lineal(x):
	return x

def lineal_derivada(x):
	return 1
