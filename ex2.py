n = int(input("Digite um número para saber se ele existe: "))

anterior = 0
seguinte = 1 
soma = 1
flag = False
i = 0

# loop para fazer a sequência de Fibonacci 
# Obs: Coloquei "+3" porque se por acaso o valor inserido for 2, o loop vai chegar até o numero 1 que, na sequencia, ocupa posição 2.
while i <= (n + 3): 

    #Checagem para ver se o número pertece a sequência de Fibonacci
    if anterior == n:
        flag = True
    #Checagem para ver se devemos continuar ou não
    if soma > n:
        break;

    
    soma = seguinte + anterior 
    anterior = seguinte 
    seguinte = soma
    i += 1



if flag == True: 
    print(f"O número {n} pertece a sequência de fibonacci e ocupa a {i}º posição ")
else:
    print(f"O número {n} não pertece a sequência de fibonacci!")