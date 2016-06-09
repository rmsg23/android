 
import math
import cPickle
from Tkinter import *
from tkMessageBox import *
def crear():
        db = []
        cPickle.dump(db,open("memoria.mem","wb"))
 
matriz = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

try:
    memoria = cPickle.load(open("memoria.mem","rb"))
except IOError:
    print("Archivo no encontrado..... Creando archivo de memoria")
    crear()
    memoria = cPickle.load(open("memoria.mem","rb"))

 
def imp(que,rango):#imprimir matriz
        ac = 0
        if ac==1:
                c = 0
                c1 = rango
               
                print "=================="
                for i in range(0,rango):
                        a = que[c:c1]
                        k =  "       ".join(str(o)for o in a)
                        print ""
                        print k
                        c +=rango
                        c1+=rango
                print "========================"
        else:
                pass
def imp2(que,rango):#imprimir matriz auxiliar
        ac = 1
        if ac==1:
                c = 0
                c1 = rango
               
                print "=================="
                for i in range(0,rango):
                        a = que[c:c1]
                        k =  "       ".join(str(o)for o in a)
                        print ""
                        print k
                        c +=rango
                        c1+=rango
                print "========================"
        else:
                pass
 
def neurona(entrada,peso):#Valores de entradas y valores de "peso"
        c = 0                                                            #conteo
        multiplicados = []                               #buffer 1
        for entrada1 in entrada:                         #intera sobre la entradas
                analisis1 = entrada1 * peso[c]   #multiplica las entradas por los pesos
                multiplicados.append(analisis1)  #la aniade al buffer
                c +=1                                                    #esto aumenta el conteo para ver el peso a medida que se repite el bucle
        suma = 0                                                         #buffer de suma       
        for i in multiplicados:                          #intera sobre
                suma+=i                                                  #va sumando a suma para sacar el resultado
        peso = math.tanh(suma)               #calculo funcional para reprimir el valor de suma
        if suma == len(entrada):             #si la suma es igual a la cantidad de valores entrada
                return suma                      #devolver la suma
        return peso
 
def final():
        global candidatos,y
        candidatos = {}
        z = 0
        for i in memoria:
                peso = neurona(memoria[z],matriz)
                print "peso:",peso
                if peso <= 0.9999999999:
                        pass
                else:
                        candidatos[peso] = memoria[z]
                z+=1
               
        y = 0
        for m in candidatos:
                if m > y:
                        y = 0
                        y +=m
                else:
                        pass
                       
        if candidatos == {}:
                print "No se que es"
        else:
                print "Comparado ",matriz," con ",candidatos[y]
                print "asd:",matriz
                print "RESULTA:"
                imp2(candidatos[y],5)
        print candidatos
def aprender():
        def memorizar(palabra,lon):
                matriz=[]
                c = 0
                c1= 0
                for i in range(0,len(palabra)):
                        for i in palabra:
                                matriz.append(palabra[c1]*palabra[c])
                                c+=1
                        c = 0
                        c1+=1
                imp(matriz,lon)
                return matriz
        a =  memorizar(matriz,25)
        memoria.append(a[0:25])
        memoria.reverse()
        print "Matriz aprendida:"
        for t in memoria:
                print t
        cPickle.dump(memoria,open("memoria.mem","wb"))
        resetear_tabla()
 
def analizar():
        final()
        resetear_tabla()
        rellenar()
 
               
#################INTERFAZ GRAFIC
ventana = Tk()
class  nume:
        def una(self):
                matriz[0] = 1
                button1.config(bg="#5BADFF")
                imp(matriz,5)
        def dos(self):
                matriz[1] = 1
                button2.config(bg="#5BADFF")
                imp(matriz,5)
        def tres(self):
                matriz[2] = 1
                button3.config(bg="#5BADFF")
                imp(matriz,5)
        def cuatro(self):
                matriz[3] = 1
                button4.config(bg="#5BADFF")
                imp(matriz,5)
        def cinco(self):
                matriz[4] = 1
                button5.config(bg="#5BADFF")
                imp(matriz,5)
        def seis(self):
                matriz[5] = 1
                button6.config(bg="#5BADFF")
                imp(matriz,5)
        def siete(self):
                matriz[6] = 1
                button7.config(bg="#5BADFF")
                imp(matriz,5)
        def ocho(self):
                matriz[7] = 1
                button8.config(bg="#5BADFF")
                imp(matriz,5)
        def nueve(self):
                matriz[8] = 1
                button9.config(bg="#5BADFF")
                imp(matriz,5)
        def diez(self):
                matriz[9] = 1
                button10.config(bg="#5BADFF")
                imp(matriz,5)
        def once(self):
                matriz[10] = 1
                button11.config(bg="#5BADFF")
                imp(matriz,5)
        def doce(self):
                matriz[11] = 1
                button12.config(bg="#5BADFF")
                imp(matriz,5)
        def trece(self):
                matriz[12] = 1
                button13.config(bg="#5BADFF")
                imp(matriz,5)
 
        def catorce(self):
                matriz[13] = 1
                button14.config(bg="#5BADFF")
                imp(matriz,5)
               
        def quince(self):
                matriz[14] = 1
                button15.config(bg="#5BADFF")
                imp(matriz,5)
 
        def diesiseis(self):
                matriz[15] = 1
                button16.config(bg="#5BADFF")
                imp(matriz,5)
 
        def diesisiete(self):
                matriz[16] = 1
                button17.config(bg="#5BADFF")
                imp(matriz,5)
 
        def diesiocho(self):
                matriz[17] = 1
                button18.config(bg="#5BADFF")
                imp(matriz,5)
               
        def diesinueve(self):
                matriz[18] = 1
                button19.config(bg="#5BADFF")
                imp(matriz,5)
        def veinte(self):
                matriz[19] = 1
                button20.config(bg="#5BADFF")
                imp(matriz,5)
 
        def veintiuno(self):
                matriz[20] = 1
                button21.config(bg="#5BADFF")
                imp(matriz,5)
        def veintidos(self):
                matriz[21] = 1
                button22.config(bg="#5BADFF")
                imp(matriz,5)
               
        def veintitres(self):
                matriz[22] = 1
                button23.config(bg="#5BADFF")
                imp(matriz,5)
               
        def veinticuatro(self):
                matriz[23] = 1
                button24.config(bg="#5BADFF")
                imp(matriz,5)
 
        def veinticinco(self):
                matriz[24] = 1
                button25.config(bg="#5BADFF")
                imp(matriz,5)
core = nume()
def resetear_tabla():
        c = 0
        for i in matriz:
                matriz[c] = -1
                c+=1
        for t in botones:
                t.config(bg="#FFFFFF")
def borrarmem():
        memoria = []
        cPickle.dump(memoria,open("memoria.mem","wb"))
 
def rellenar():
        c = 0
        if candidatos == {}:
                return 0
        for i in candidatos[y]:
               
                if c == len(botones):
                        break
                if i == 1:
                        botones[c].config(bg="#01D826")
                if i == -1:
                        pass
                c+=1
     
     
     
     
     
     
     
     
     
#def grafica()    
###botones interac
ventana2 = Tk()
ventana.title("Red neuronal")
ventana.config(bg="#ECFFFF")
ventana2.geometry("180x200+450+350")
ventana2.title("Panel")
 
ventana.geometry("300x300+100+100")
aprender=Button(ventana2,text='Aprender',command=aprender,width=455).pack()
aprender=Button(ventana2,text='Analizar',command=analizar,width=455).pack()
aprender=Button(ventana2,text='Resetear valores',command=resetear_tabla,width=455).pack()
Label(ventana2,text="_____________________________").pack()
aprender=Button(ventana2,text='Borrar memoria',command=borrarmem,width=455).pack()
#######5
button25=Button(ventana,text='25',command=core.veinticinco,bg="#FFFFFF")
button25.place(relx=0.73, rely=0.77, relwidth=0.13, relheight=0.15)
button24=Button(ventana,text='24',command=core.veinticuatro,bg="#FFFFFF")
button24.place(relx=0.58, rely=0.77, relwidth=0.13, relheight=0.15)
button23=Button(ventana,text='23',command=core.veintitres,bg="#FFFFFF")
button23.place(relx=0.43, rely=0.77, relwidth=0.13, relheight=0.15)
button22=Button(ventana,text='22',command=core.veintidos,bg="#FFFFFF")
button22.place(relx=0.28, rely=0.77, relwidth=0.13, relheight=0.15)
button21=Button(ventana,text='21',command=core.veintiuno,bg="#FFFFFF")
button21.place(relx=0.12, rely=0.77, relwidth=0.13, relheight=0.15)
#######4
button20=Button(ventana,text='20',command=core.veinte,bg="#FFFFFF")
button20.place(relx=0.73, rely=0.60, relwidth=0.13, relheight=0.15)
button19=Button(ventana,text='19',command=core.diesinueve,bg="#FFFFFF")
button19.place(relx=0.58, rely=0.60, relwidth=0.13, relheight=0.15)
button18=Button(ventana,text='18',command=core.diesiocho,bg="#FFFFFF")
button18.place(relx=0.43, rely=0.60, relwidth=0.13, relheight=0.15)
button17=Button(ventana,text='17',command=core.diesisiete,bg="#FFFFFF")
button17.place(relx=0.28, rely=0.60, relwidth=0.13, relheight=0.15)
button16=Button(ventana,text='16',command=core.diesiseis,bg="#FFFFFF")
button16.place(relx=0.12, rely=0.60, relwidth=0.13, relheight=0.15)
#######3
button15=Button(ventana,text='15',command=core.quince,bg="#FFFFFF")
button15.place(relx=0.73, rely=0.43, relwidth=0.13, relheight=0.15)
button14=Button(ventana,text='14',command=core.catorce,bg="#FFFFFF")
button14.place(relx=0.58, rely=0.43, relwidth=0.13, relheight=0.15)
button13=Button(ventana,text='13',command=core.trece,bg="#FFFFFF")
button13.place(relx=0.43, rely=0.43, relwidth=0.13, relheight=0.15)
button12=Button(ventana,text='12',command=core.doce,bg="#FFFFFF")
button12.place(relx=0.28, rely=0.43, relwidth=0.13, relheight=0.15)
button11=Button(ventana,text='11',command=core.once,bg="#FFFFFF")
button11.place(relx=0.12, rely=0.43, relwidth=0.13, relheight=0.15)
#######2
diez = button10=Button(ventana,text='10',command=core.diez,bg="#FFFFFF")
button10.place(relx=0.73, rely=0.26, relwidth=0.13, relheight=0.15)
nueve = button9=Button(ventana,text='9',command=core.nueve,bg="#FFFFFF")
button9.place(relx=0.58, rely=0.26, relwidth=0.13, relheight=0.15)
ocho = button8=Button(ventana,text='8',command=core.ocho,bg="#FFFFFF")
button8.place(relx=0.43, rely=0.26, relwidth=0.13, relheight=0.15)
siete = button7=Button(ventana,text='7',command=core.siete,bg="#FFFFFF")
button7.place(relx=0.28, rely=0.26, relwidth=0.13, relheight=0.15)
seis = button6=Button(ventana,text='6',command=core.seis,bg="#FFFFFF")
button6.place(relx=0.12, rely=0.26, relwidth=0.13, relheight=0.15)
#######1
cinco1 = button5=Button(ventana,text='5',command=core.cinco,bg="#FFFFFF")
button5.place(relx=0.73, rely=0.09, relwidth=0.13, relheight=0.15)
cuatro1 = button4=Button(ventana,text='4',command=core.cuatro,bg="#FFFFFF")
button4.place(relx=0.58, rely=0.09, relwidth=0.13, relheight=0.15)
tres1 = button3=Button(ventana,text='3',command=core.tres,bg="#FFFFFF")
button3.place(relx=0.43, rely=0.09, relwidth=0.13, relheight=0.15)
dos1 = button2=Button(ventana,text='2',command=core.dos,bg="#FFFFFF")
button2.place(relx=0.28, rely=0.09, relwidth=0.13, relheight=0.15)
uno1 = button1=Button(ventana,text='1',command=core.una,bg="#FFFFFF")
button1.place(relx=0.12, rely=0.09, relwidth=0.13, relheight=0.15)
botones = [button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25]
ventana2.mainloop()
ventana.mainloop()