###Serve para criptografia

import hashlib

# 1 - verificar os algoritmos 
print(hashlib.algorithms_available)

# 2 - Algoritimos disponivel pelo sistema operacional
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "Eu odeio meu serviço e quero vencer".encode()
algorithm.update(message)
print(algorithm.hexdigest())


# 5 - utilizando o md5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
