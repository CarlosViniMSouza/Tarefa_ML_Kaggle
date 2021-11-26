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

# Contadores:
quantSim = 0
quantNao = 0

"""
Formula: [P(Calafrios = "s" | GRIPE = "s") * P(Coriza = "n" | GRIPE = "s") * P(Cefaleia = f | GRIPE = "s") * P(Febre = "s" | GRIPE = "n")]/P(x | GRIPE = "s") 
"""

# Laco FOR para a coluna "Calafrios"
for i in range(0, len(tabela['Calafrios'])):

  if (tabela['Calafrios'][i] == "s"):
    quantSim += 1
  else:
    quantNao += 1

print("Quantidade de SIM: ", quantSim)
print("Quantidade de NAO: ", quantNao)

# Laco FOR para a coluna "Cefaleia"