from models.cliente import Cliente
from models.conta import Conta


applegate: Cliente = Cliente('AJ Applegate', 'ajapplegate@gmail.com', '123.456.789-01', '23/09/1989')
remy: Cliente = Cliente('Remy LaCroix', 'remylacroix@gmail.com', '987.654.321-99', '26/06/1988')

# print(applegate)
# print(remy)

contaa: Conta = Conta(applegate)
contar: Conta = Conta(remy)

print(contaa)
print(contar)





