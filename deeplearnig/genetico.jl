#! /usr/bin/env julia

type Flor
	adaptacion::Float64
	cromosoma::Array
end


function calculaadaptacion(x::Flor)
	alturadeseada=2
	colordeseado=5
	tamañodesaedo=8
	fuerzadeseada=7

    altura= x.cromosoma[1]/alturadeseada
    altura=altura>1.0?1/altura:altura
    color= x.cromosoma[2]/colordeseado
    color=color>1.0?1/color:color
    tamaño= x.cromosoma[3]/tamañodesaedo
    tamaño=tamaño>1.0?1/tamaño:tamaño
    fuerza= x.cromosoma[4]/fuerzadeseada
    fuerza=fuerza>1.0?1/fuerza:fuerza

	x.adaptacion=(altura+color+tamaño+fuerza)/4
end

function seleccionapadres(padrea,padreb)

	for i=1:length(poblacion)
		if poblacion[i].adaptacion>poblacion[padrea].adaptacion
			padrea=i
		end
	end
	for i=1:length(poblacion)
		if poblacion[i].adaptacion>poblacion[padreb].adaptacion
			if(padreb!=padrea)
				padreb=i
			end
		end
	end
	return padrea, padreb
end

function crossover(padrea,padreb)
	pa= Flor(0.1,[0,0,0,0])
	pb= Flor(0.1,[0,0,0,0])
	for i=1:length(poblacion[padrea].cromosoma)
		pa.cromosoma[i]=poblacion[padrea].cromosoma[i]
		pb.cromosoma[i]=poblacion[padreb].cromosoma[i]
	end

    if rand(0:1)==0
		for i=1:length(poblacion)
			for c=1:length(poblacion[padrea].cromosoma)÷2
				poblacion[i].cromosoma[c]=pa.cromosoma[c]
			end
		end
    else
    	for i=1:length(poblacion)
			for c=1:length(poblacion[padrea].cromosoma)÷2
				poblacion[i].cromosoma[c]=pb.cromosoma[c]
			end
		end
	end

end

function mutacion()
	for i=rand(1:length(poblacion))
		poblacion[rand(1:length(poblacion))].cromosoma[rand(1:length(poblacion[i].cromosoma))]=rand(1:10)
	end
end

generaciones=10
padrea=1
padreb=1


poblacion = [Flor(0.1,[1,2,3,4]),Flor(0.8,[5,6,7,9]),Flor(0.6,[8,10,3,7]),Flor(1.4,[3,2,10,1])]


for generacion=1:generaciones
	map(x->calculaadaptacion(x), poblacion)
	padrea,padreb= seleccionapadres(padrea,padreb)
	crossover(padrea,padreb)
	mutacion()
	println(poblacion[padrea])
end


#=
*se determina la estructura de un individuo
*se crea una poblacion con n individuos
*se determina cual de los individuos esta mejor adaptado (cumple con la o las caracteristicas deseadas)
*se establecen los individuos mejor adaptados como padres de la siguente genracion
*se cruzan los cromosomas de los padres o alguno de ellos con el resto de la poblacion
*la mutacion agrega nuevos datos a la poblacion de forma aleatoria  y/o segun un indice de mutacion
**  el objetivo principal de los algoritmos geneticos es encontrar los datos optimos a un problema variando los parametros
	hasta alcanzar un n numero de generacion por ejemplo
=#
