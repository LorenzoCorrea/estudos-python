import statistics


# 1 - Aplicar a média
print(statistics.mean([3, 2, 5, 8, 9])) #soma dos numeros dividios pelos numeros

# 2 - Aplicar a mediana (valor que esta ao meio)
print(statistics.median([1, 2, 3, 8, 9])) 
print(statistics.median([1, 2, 3, 7, 8, 9])) 


# 3 - Aplicar a moda
print(statistics.mode([2, 5, 3, 8, 8, 4, 2 , 7, 2, 6]))



# Aplicar o desvio padrão
"""
Medida de dispersão do conjunto, ou seja, uma medida 
que indica quão uniformes são os dados do conjunto.

- Quanto mais próximo de 0, significa que os dados
do conjunto estão menos dispersos
"""

print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]))