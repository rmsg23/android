type Capa
    neuronas::Int64
    neuronash::Int64
    neuronap::Int64
    w::Array{Float64}
    Δw::Array{Float64}
    a::Array{Float64}
    valordeseado::Array{Float64}
    error::Array{Float64}
    bias::Array{Float64}
    pesobias::Array{Float64}
    learningrate::Float64
    padre::Any
    hija::Any
    haypadre::Bool
    hayhija::Bool
    inicializacapa::Function
    Capa()=new(0,0,0,[],[],[],[],[],[],[],0.0,nothing,nothing,false,false,()->begin
    if(haypadre==true)
    w=[1.0 for i=2:neuronas, j=1:neuronap ]
    Δw=[0.0 for i=2:neuronas, j=1:neuronap ]
    end

    a = [0.0 for n=1:neuronas]
    valordeseado = [0.0 for n=1:neuronas]
    error= [0.0 for n=1:neuronas]
    bias=[-1.0 for n=1:neuronas]
    pesobias=[0.0 for n=1:neuronas]
  end)
end

Capa()
