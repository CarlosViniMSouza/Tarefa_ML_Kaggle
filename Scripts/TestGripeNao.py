"""
Tabela da Aula em formato de Dicio"n"ario:

1 - SIM ="s
2 - NAO = "n"
3 - MEDIA = m
4 - FORTE = f

Onde:
Calafrio"s" = "N"ao
Coriza = Nao
Cefaleia = Forte
Febre = SIM
"""

tabela = {
  "Calafrios": ["s", "s", "s", "n", "n", "n", "n", "s"],
  "Cefaleia": ["m", "n", "f", "m", "n", "f", "f", "m"],
  "Coriza": ["n", "s", "n", "s", "n", "s", "s", "s"],
  "Febre": ["s", "n", "s", "s", "n", "s", "n", "s"],
  "GRIPE": ["n", "s", "s", "s", "n", "s", "n", "s"]
}

"""
Formula: (P(Calafrios = "s" | GRIPE = "s") * P(Coriza = "n" | GRIPE = "s") * P(Cefaleia = f | GRIPE = "s") * P(Febre = "s" | GRIPE = "n"))/P(x | GRIPE = "s")
"""

# Separando a coluna gripe entre "SIM" e "NAO":
# Contadores:
quantGripeSim = 0
quantGripeNao = 0

for i in range(len(tabela['GRIPE'])):

  if(tabela['GRIPE'][i] == "s"):
    quantGripeSim += 1
  else:
    quantGripeNao += 1

# Agora vamos dividir cada coluna nas respectivas respostas:

# Laco FOR para a coluna "Calafrios"
# Contadores:
quantCalafrios = 0

for i in range(0, len(tabela['Calafrios'])):

  if (tabela['Calafrios'][i] == "s" and tabela["GRIPE"][i] == "n"):
    quantCalafrios += 1

print("Quantidade procurada de Calafrios: ", quantCalafrios) #3


# Laco FOR para a coluna "Cefaleia"
# Contadores:
quantCefaleia = 0

for i in range(0, len(tabela['Cefaleia'])):

  if (tabela['Cefaleia'][i] == "m" and tabela["GRIPE"][i] == "n"):
    quantCefaleia += 1

print("Quantidade procurada de Cefaleia: ", quantCefaleia) #3


# Laco FOR para a coluna "Coriza"
# Contadores:
quantCoriza = 0

for i in range(0, len(tabela['Coriza'])):

  if (tabela['Coriza'][i] == "s" and tabela["GRIPE"][i] == "n"):
    quantCoriza += 1

print("Quantidade procurada de Coriza: ", quantCoriza) #5


# Laco FOR para a coluna "Febre"
# Contadores:
quantFebre = 0

for i in range(0, len(tabela['Febre'])):

  if (tabela['Febre'][i] == "s" and tabela["GRIPE"][i] == "n"):
    quantFebre += 1

print("Quantidade Procurada de Febre: ", quantFebre) #5


# Aplicando a Formula
ProbGripeNao = ((quantCalafrios/quantGripeNao) * (quantCefaleia/quantGripeNao) * (quantCoriza/quantGripeNao) * (quantFebre/quantGripeNao))/(quantGripeNao/len(tabela['GRIPE']))

print("O resultado de P(x|GRIPE = SIM) eh: ", ProbGripeNao)

# Agora vamos calcular o P(x | GRIPE = NAO):