#inventario
identificador=[]
resposta="S"
while resposta=="S":
      identificador.append(input("Equipamento: "))
      identificador.append(float(input("Valor: "))) #.append é adc na lista
      identificador.append(int(input("Número Serial: "))) #é convertido em ponto flutuante, e adicionado na lista "inventario"
      identificador.append(input("Departamento: "))
      resposta=input("Digite \"S\"  para continuar: ").upper() #serve para caso o usuario coloque o S em minusculo (prevenção de erro.

for elemento in identificador:
    print(elemento) #mostra os dados que foram adcionados
