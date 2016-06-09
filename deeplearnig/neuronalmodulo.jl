Capa = (()->begin

  #global neuronas=0
  neuronas=0
  neuronash=0
  neuronasp=0
  w=[]
  Δw=[]
  a=[]
  valordeseado=[]
  error=[]
  bias=[]
  pesobias=[]
  learningrate=0.0
  padre=nothing
  hija=nothing
  haypadre=false
  hayhija=false

  fa=(x)-> 1.0/(1+e^(-x))

  _cantidadneuronas =(()-> begin
  Dict(
    "set"=> (v)->neuronas=v,
    "get"=> neuronas
  )
end)

  _cantidadneuronashija =(()-> begin
  Dict(
    "set"=> (v)->neuronash=v,
    "get"=> neuronash
  )
  end)

  _cantidadneuronaspadre =(()-> begin
  Dict(
    "set"=> (v)->neuronasp=v,
    "get"=> neuronasp
  )
  end)

  _proporcionaprendizaje =(()-> begin
  Dict(
    "set"=> (v)->learningrate=v
    #"get"=> learningrate
  )
  end)

	_colocapadre = (ppadre::Capa)->begin
		padre=ppadre
    haypadre=true
    neuronasp=padre["cantidadneuronas"]()["get"]
    w=[0.0 for i=1:neuronas, j=1:neuronasp]
    Δw=[0.0 for i=1:neuronas, j=1:neuronasp]
	end

  _colocahija = (phija::Capa)->begin
		hija=phija
    hayhija=true
    neuronash=hija["cantidadneuronas"]()["get"]
	end

  _valor =(()-> begin
  Dict(
    "set"=> (v,d)->a[v]=d,
    "get"=> (v)->a[v]
  )
  end)
  _valordeseado =(()-> begin
  Dict(
    "set"=> (v,d)->valordeseado[v]=d,
    "get"=> (v)->valordeseado[v]
  )
  end)

  _error =(()-> begin
  Dict(
    "set"=> (v,d)->error[v]=d,
    "get"=> (v)->error[v]
  )
  end)

  _pesos =(()-> begin
  Dict(
    "set"=> (i,j,d)->w[i,j]=d,
    "get"=> (i,j)->w[i,j]
  )
  end)

  _inicializacapa = ()->begin
      if(haypadre==true)
        Δw=[0.0 for i=1:neuronas, j=1:neuronap ]
      end

      a = [0.0 for n=1:neuronas]
      valordeseado = [0.0 for n=1:neuronas]
      error= [0.0 for n=1:neuronas]
      bias=[-1.0 for n=1:neuronas]
	end

  _inicializapesos = ()->begin
      w=[rand(-1.0:1.0) for i=1:neuronas, j=1:neuronap ]
      pesobias=[rand(-1.0:1.0) for i=1:neuronas]
	end

  _calculaneuronas = ()->begin
      if haypadre==true
        valor=0.0
        for n=1:neuronas
          for m=1:neuronasp
            valor+=padre["valor"]()["get"](m)*w[n,m]
          end

          valor+=bias[n]*pesobias[n]

          a[n]=fa(valor)

        end
      end
	end

  _calculaerrorsalida= ()-> begin
    for n=1:neuronas
      error[n]=(valordesado[n]-a[n])*a[n]*(1.0-a[n])
    end
  end

  _calculaerrorentrada= ()-> begin
    for n=1:neuronas
      error[n]=0.0
    end
  end

  _calculaerroroculta= ()-> begin
    sumatoria=0.0
    for n=1:neuronash
      for m=1:neuronash
        sumatoria+=hija["error"]()["get"](m)*hija["pesos"]()["get"](n,m)
      end
    end

    for n=1:neuronas
      error[n]=sumatoria*a[n]*(1.0-a[n])
    end
  end

  _ajustapesos= ()-> begin
    for n=1:neuronas
      for m=1:neuronasp
        delta=learningrate*error[n]*padre["valor"]()["get"](m)
        Δw[n,m]=delta
        pesos[n,m]+=delta
      end
    end
  end

	return Dict(
		"inicializacapa"=> _inicializacapa,
    "colocapadre"=> _colocapadre,
    "colocahija"=> _colocahija,
    "cantidadneuronas"=> _cantidadneuronas,
    "cantidadneuronashija"=> _cantidadneuronashija,
    "cantidadneuronaspadre"=> _cantidadneuronaspadre,
    "proporcionaprendizaje"=> _proporcionaprendizaje,
    "inicializapesos"=> _inicializapesos,
    "valor"=> _valor,
    "valordeseado"=> _valordeseado,
    "error"=> _error,
    "calculaneuronas"=> _calculaneuronas,
    "calculaerrorsalida"=> _calculaerrorsalida,
    "calculaerrorentrada"=> _calculaerrorentrada,
    "calculaerroroculta"=> _calculaerroroculta,
    "ajustapesos"=> _ajustapesos
	)

end)


#c= Capa()
#c["cantidadneuronas"]()["set"](10)
#c["cantidadneuronas"]()["get"]
#c["calculaneuronas"]()


Red = (()->begin

entrada= Capa()
oculta= Capa()
salida= Capa()

  function _inicializa (nentrada,noculta,nsalida)
    entrada["cantidadneuronas"]()["set"](nentrada)
    entrada["cantidadneuronashija"]()["set"](noculta)

    oculta["cantidadneuronas"]()["set"](noculta)
    oculta["cantidadneuronashija"]()["set"](nsalida)
    oculta["cantidadneuronaspadre"]()["set"](nentrada)

    salida["cantidadneuronas"]()["set"](nsalida)
    salida["cantidadneuronaspadre"]()["set"](noculta)

    entrada["colocahija"](oculta)

    oculta["colocapadre"](entrada)
    oculta["colocahija"](salida)

    salida["colocapadre"](oculta)

    entrada["inicializacapa"]()
    oculta["inicializacapa"]()
    salida["inicializacapa"]()

    oculta["inicializapesos"]()
    salida["inicializapesos"]()
  end

	_colocaentrada = (neurona, valor)->begin
    if neurona>=1 && neurona<=entrada["cantidadneuronas"]()["get"]
      entrada["valor"]()["set"](neurona,valor)
    end
	end

  _obtensalida = (neurona)->begin
  if neurona>=1 && neurona<=salida["cantidadneuronas"]()["get"]
    return salida["valor"]()["get"](neurona)
  else
    return 0.0
	end
end

  _colocasalidadeseada = (neurona, valor)->begin
    if neurona>=1 && neurona<=salida["cantidadneuronas"]()["get"]
      salida["valordeseado"]()["set"](neurona,valor)
    end
	end

  _feedforward = ()->begin
    entrada["calculaneuronas"]()
    oculta["calculaneuronas"]()
    salida["calculaneuronas"]()
  end

  _backpropagate= ()-> begin
    salida["calculaerrorsalida"]()
    salida["ajustapesos"]()
    oculta["calculaerroroculta"]()
    oculta["ajustapesos"]()
  end

  _valormasalto= ()-> begin
    indice=0
    maximo=salida["valor"]()["get"](1)
    for n=1:salida["cantidadneuronas"]()["get"]
      if salida["valor"]()["get"](n)>maximo
        maximo=salida["valor"]()["get"](n)
        indice=n
      end
    end
    return indice
  end

  _calculaerror= ()-> begin
    error=0.0

    for n=1:salida["cantidadneuronas"]()["get"]
        error=(salida["valor"]()["get"](n)-salida["valordesado"]()["get"](n))*(salida["valor"]()["get"](n)-salida["valordesado"]()["get"](n))
        indice=n
    end
    error=error/salida["cantidadneuronas"]()["get"]
    return error
  end



	return Dict(
		"inicializa"=> _inicializa,
    "colocaentrada"=>_colocaentrada,
    "colocasalidadeseada"=>_colocasalidadeseada,
    "feedforward"=>_feedforward,
    "backpropagate"=>_backpropagate,
    "valormasalto"=>_valormasalto,
    "calculaerror"=>_calculaerror
	)

end)



ia= Red()

ia["inicializa"](3,4,2)   #!!!! ERROR: TypeError: typeassert: expected Type{T} !!!!
