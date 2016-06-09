from neuronal import Redneuronal
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn import metrics
#import matplotlib.pyplot as plt
from PIL import Image
from Tkinter import *

from PIL import ImageTk
import cv2
from sklearn import datasets
import numpy as np
import math
#from collections import Counter
import SocketServer
import threading 
import commands
#import imutils #usado para el cv2.moments(rect)
def histograma(imagen):
	ajuste = 0
	minimo_valor = np.min(imagen)
	if minimo_valor < 0:
		ajuste = minimo_valor
		rango = np.max(imagen).astype(np.int64) - minimo_valor
		ajuste_dtype = np.promote_types(np.min_scalar_type(rango),np.min_scalar_type(minimo_valor))
		if imagen.dtype != ajuste_dtype:
			imagen = imagen.astype(ajuste_dtype)
		imagen = imagen - ajuste
	hist = np.bincount(imagen.ravel())
	valores_centrales = np.arange(len(hist)) + ajuste
	idx = np.nonzero(hist)[0][0]
	return hist[idx:], valores_centrales[idx:]


def ejecuta():
	global estado
	estado=estado+1
	print ("es estado vale:  ",estado)

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # se lanza automaticamente al hacer un request
        self.data = self.request.recv(1024).strip()
        #datos de donde corre
        #print "{} wrote:".format(self.client_address[0])
        #print "-------------------------"
        #los datos
        #print self.data
        # responde al clienete con las mismas lineas que le envio pero en mayusculas
        ejecuta()
        self.request.sendall(self.data.upper())

class servidor(threading.Thread):
    def __init__(self,direccion, puerto):
        threading.Thread.__init__(self)  
        HOST, PORT = direccion,puerto
        global estado
        estado=1
        print ">>>>>>>>>>>Direccion: "+direccion
        print "\n"
        print ">>>>>>>>>>>Puerto: "+str(puerto)
        print "\n"

        global server
        server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    def run(self):
        # Lanzamos el server
        server.serve_forever()

def targetToVector(x):
	# Vector
	a = np.zeros([len(x),10])
	for i in range(0,len(x)):
		a[i,x[i]] = 1
	return a

def predice(roi):
	global red
	imag = np.array(roi)
	b=((imag.astype(int)*15)/255).astype(float)
	b=(b-15)*-1
	
	X_scaled = preprocessing.scale(b)
	nl=np.zeros(64)
	c=0
	for i in range(8):
		for j in range(8):
			nl[c]= X_scaled[i][j]
			c+=1
	mi_prediccion = red.prediccion(np.array([nl]))
	sl=np.argmax(mi_prediccion, axis=1).astype(int)
	
	porcentaje=mi_prediccion[0][sl[0]]*100

	return porcentaje,sl

def distribucion_acumulada(image):
    hist, valores_centrales = histograma(image.ravel())
    img_cdf = hist.cumsum()
    img_cdf = img_cdf / float(img_cdf[-1])
    return img_cdf, valores_centrales

def ecualiza(image):
    cdf, valores_centrales = distribucion_acumulada(image)
    out = np.interp(image.flat, valores_centrales, cdf)
    return (out.reshape(image.shape))

def ecualiza2(imageng):
	c=np.min(imageng.ravel())
	d=np.max(imageng.ravel())
	a=0
	b=255
	try:
		pxo=(((imageng-c)*((b-a)/(d-c)))+a)
	except Exception, e:
		pxo=imageng
	#pxo=pxo/255.0
	return pxo.reshape(imageng.shape)
	
def otsu(imagen):
	if(imagen.dtype!='int'):
		imagen=(imagen*255).astype(int)
	try:
		hist, valorcentral = histograma(imagen.ravel())
		hist = hist.astype(float)
		# probabilidades para todos los umbrales posibles
		valor1 = np.cumsum(hist)
		valor2 = np.cumsum(hist[::-1])[::-1]
		# para medias
		media1 = np.cumsum(hist * valorcentral) / valor1
		media2 = (np.cumsum((hist * valorcentral)[::-1]) / valor2[::-1])[::-1]
		# Clip termina para alinear las variables de clase 1 y clase 2 :
		# El ultimo valor de 'valor1' /' media1' debe emparejarse con valores cero en
		# ' valor2' /' media2' , que no existe.
		varianza = valor1[:-1] * valor2[1:] * (media1[:-1] - media2[1:]) ** 2
		idx = np.argmax(varianza)
		return valorcentral[:-1][idx]
	except Exception, e:
		print e
		return 50		
	
def etiquetaje(imagen):
	region=1
	print region
	nuevaimg=np.zeros((imagen.shape[1],imagen.shape[0]))
	print nuevaimg
	equivalencia=[]
	print equivalencia
	for i in range(1,imagen.shape[1]-1):
		for j in range(1,imagen.shape[0]-1):
			if(imagen[i][j]==1):
				valores=np.array([nuevaimg[i-1][j],nuevaimg[i][j-1],nuevaimg[i-1][j-1],nuevaimg[i-1][j+1],nuevaimg[i+1][j],nuevaimg[i][j+1],nuevaimg[i+1][j+1],nuevaimg[i+1][j-1]])
				# print "nuevaimg[j-1][i]: ",nuevaimg[j-1][i]
				# print "nuevaimg[j][i-1]: ",nuevaimg[j][i-1]
				# print "nuevaimg[j-1][i-1]: ",nuevaimg[j-1][i-1]
				# print "nuevaimg[j-1][i+1]: ",nuevaimg[j-1][i+1]
				# print "nuevaimg[j+1][i]: ",nuevaimg[j+1][i]
				# print "nuevaimg[j][i+1]: ",nuevaimg[j][i+1]
				# print "nuevaimg[j+1][i+1]: ",nuevaimg[j+1][i+1]
				# print "nuevaimg[j+1][i-1]: ",nuevaimg[j+1][i-1]
				print "valores: ",valores
				vecinos=np.bincount(valores.astype(int))
				print "vecinos: ",vecinos
				tempo=[]
				if(vecinos[0]==8):
					nuevaimg[i][j]=region
					region+=1
				if(vecinos[0]<=7):
					nuevaimg[i][j]=np.max(valores)
				# if(vecinos[0]<7):
				# 	va=np.argmax(vecinos[1:len(vecinos)])
				# 	va+=1
				# 	tempo=tempo+[va]
				# 	while va!=0:
				# 		vecinos[va]=0
				# 		va=np.argmax(vecinos[1:len(vecinos)])
				# 		va+=1
				# 		tempo=tempo+[va]
				# 	equivalencia=equivalencia+[tempo]
				# 	print equivalencia
	return nuevaimg
	
def binariza(imagen,umbral=0.128):
	if(umbral>1):
		umbral=umbral/255.0
	bz = (imagen<=umbral)*1.0
	return bz


def cerebro():
	
	digits = datasets.load_digits()
	
	
	X = preprocessing.scale(digits.data.astype(float))
	y = targetToVector(digits.target)
	#print(digits.data[0])
	#print(X[0])
	print "\n\tCargando los datos ", (len(y))
	print "\n\tExtrayendo los datos separando datos de identificadores"

	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)
	print "\n\tDatos para el aprendizaje: ",len(y_train)


	#se crea la red neuronal
	global red
	red = Redneuronal(64,60,10)
	print("\n\tIniciando la red neuronal y alimentandola...")
	red.ajuste(X_train,y_train, fases = 50, tasa_aprendizaje = .1, tasa_aprendizaje_decadencia = .01, imprimir = 1)

	print "\n\tAprendizaje terminado!!!\n"
	#-------------------------------------------------------Metricas---------------------------------------
	print "\n\tDatos para el testeo: ",len(y_test)

	y_predecida = red.prediccion(X_test)

	y_predecida = np.argmax(y_predecida, axis=1).astype(int)
	y_test = np.argmax(y_test, axis=1).astype(int)

	print("\n\tInforme de clasificacion de la red neuronal:\n\n%s\n"
	  % (metrics.classification_report(y_test, y_predecida)))
	print("Confusion matrix:\n\n%s" % metrics.confusion_matrix(y_test, y_predecida))
	#-------------------------------------------------------Prediccion de pueba--------------------------------------

	# X = np.array([[-0. , 2. , 4. ,-0. , 1. , 2. ,-0. ,-0.], #ESTO ES UN 2
 	#				[-0. ,-0. ,-0. ,-0. ,-0. , 4. ,-0. ,-0.],
 	#				[-0. ,-0. ,-0. ,-0. , 1. , 3. ,-0. ,-0.],
 	#				[-0. ,-0. ,-0. ,-0. , 4. , 1. ,-0. ,-0.],
 	#				[-0. ,-0. ,-0. , 1. , 4. ,-0. ,-0. ,-0.],
 	#				[-0. ,-0. , 1. , 4. , 1. ,-0. ,-0. ,-0.],
 	#				[-0. , 2. , 5. , 2. , 1. ,-0. ,-0. ,-0.],
 	#				[-0. , 1. , 2. , 3. , 4. , 4. , 3. ,-0.]])

	X = np.array([[ -0. , -0. , -0. ,  2. ,  5. ,  8. ,  9. ,  9.], #ESTO ES UNA RAYA
 [  1. ,  8. , 10. , 11. , 11. , 10. ,  9. ,  9.],
 [  9. ,  9. ,  9. ,  5. ,  3. , -0. , -0. , -0.],
 [  9. ,  4. , -0. , -0. , -0. , -0. , -0. , -0.],
 [  1. , -0. , -0. , -0. , -0. , -0. , -0. , -0.],
 [ -0. , -0. , -0. , -0. , -0. , -0. , -0. , -0.],
 [ -0. , -0. , -0. , -0. , -0. , -0. , -0. , -0.],
 [ -0. , -0. , -0. , -0. , -0. , -0. , -0. , -0.]])

	X_scaled = preprocessing.scale(X)
	nl=np.zeros(64)
	c=0
	for i in range(8):
		for j in range(8):
			nl[c]= X_scaled[i][j]
			c+=1
	print(np.array([nl]))
	mi_prediccion = red.prediccion(np.array([nl]))
	print("-------------Mi prediccion---------------\n")
	sl=np.argmax(mi_prediccion, axis=1).astype(int)
	print sl,"\n"
	
	porcentaje=mi_prediccion[0][sl[0]]*100

	print(porcentaje)
	print("----------------------------\n")
	#plt.imshow(X, cmap=plt.cm.gray_r, interpolation='nearest')
	#plt.show()

def oido():	
	print("levantando websoket")
	demonio=servidor(commands.getoutput("hostname -I").split(" ")[0],9999);
	demonio.start()

def ojo():
	cap = cv2.VideoCapture(0)

	while(True):
	    #leemos un frame y lo guardamos
	    ret, img = cap.read()
	    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    blur = cv2.GaussianBlur(gray,(5,5),0)
	    ecu=ecualiza(blur)
	    #print ecu
	    umbral=otsu(ecu)
	    print umbral
	    binary= binariza(ecu,umbral)
	    #print umbral
	   
	    
	    #rects = [cv2.boundingRect(ctr) for ctr in cnts]

	    #n = 0
	    #for rect in rects:
	        #M = cv2.moments(rect)
	        #cX = int(M["m10"] / M["m00"])
	        #print cX
	        #cY = int(M["m01"] / M["m00"])
	        #print cY
	        #print "\n"
	        # Draw the rectangles
	        #(imagen donde colocar el rectangulo,primer punto,segundo punto,color,grosor de la linea)
	        #dato = math.sqrt(math.pow(rect[2],2)+math.pow(rect[3],2))
	        #dato2= (rect[3])
	        #if(dato>=10 and dato<=280) or 
	        #if(dato2>=1 and dato2<=450):
	        # if(dato>=23 and dato<=540):
	        #     #cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2] , rect[1] + rect[3]), (255, 255, 0), 5)
	        #     #cv2.putText(img, str(int((rect[3])-(rect[0]))), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
	        #     # Make the rectangular region around the digit
	        #     leng = int(rect[3] * 1.1)
	        #     pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
	        #     pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
	        #     # Verificar si el contorno esta bien definido
	        #     if pt1 < 0 or pt2< 0 :
	        #         continue
	        #     roi = binary[pt1:pt1+leng, pt2:pt2+leng]
	        #     r = 8.0 / roi.shape[1]
	        #     dim_gray = (8, int(roi.shape[0] * r))
	        #     # # perform the actual resizing of the im_gray and show it
	        #     # 
	        #     #roi = cv2.resize(roi, dim_gray, interpolation = cv2.INTER_AREA)
	        #     roi = cv2.resize(roi, (8,8), interpolation=cv2.INTER_AREA)
	        #     roi = roi[0:8, 0:8]
	            
	        #     #por,pr=predice(roi)
	            
	        #     #se proyecta el numero en la pantalla numero y porcentaje de prediccion
	        #     #cv2.putText(img, str(int(pr[0]))+" "+str(int(por))+"%", (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
	        #     #if(por>98): #solo se muestran los numeros que  tengaN una seguridad del 98% 
	        #     cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2] , rect[1] + rect[3]), (255, 255, 0), 5)
	        #     cv2.drawContours(img, cnts, -1, (0,255,0), 3)
	        #         #cv2.circle(img, (rect[0]+cX, rect[1]+cY), 7, (255, 255, 255), -1)
	        #     	#cv2.putText(img, str(int(pr[0])), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)


	    #cv2.drawContours(img, cnts, -1, (0,255,0), 3)
	    cv2.imshow('PROYECTO',binary)
	    #con la tecla 'Esc' salimos del programa
	    k = cv2.waitKey(5) & 0xFF
	    if k == 27:
	        break
	#cap.release()
	#cv2.destroyAllWindows()


#root = Tk()
#root.title("Reconocedor de numeros y simbolos")

#cerebro()
ojo()
#root.mainloop()
