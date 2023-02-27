import json
import operator

#Abrindo o arquivo .json
with open('dados.json') as file:

    data = json.load(file)

#Descobrindo valor máximo
max = data[0]['valor']

for x in range(len(data)):

    if data[x]['valor'] > max:
        max = data[x]['valor']



#Descobrindo valor mínimo

min = data[0]['valor']

for x in range(len(data)):

    if data[x]['valor'] < min and data[x]['valor'] != 0:
        min = data[x]['valor']

# Média da receita mensal
m = 0
media = 0

for x in range(len(data)):
    if data[x]['valor'] != 0:
        media += data[x]['valor']
        m += 1
        
media = media / m

# Descobrindo dias que faturaram mais do que a média mensal
dias = 0
for x in range(len(data)):
    if media < data[x]['valor']:
        dias += 1


# Resultado:
print(f"O menor faturamento ocorrido no mês foi R${min:.2f}")
print(f"O maior faturamento ocorrido no mês foi R${max:.2f}")
print(f"O número de dias que faturaram mais do que a média de R${media:.2f} foi de {dias} dias")







