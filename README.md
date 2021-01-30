#BancoPy - Sistema de gerenciamento bancário

###Introdução
O BancoPy é um mini-sistema de gerenciamento bancário que utiliza POO e executado pelo terminal.

###Funções
O sistema conta com 5 funções principais
- Criar conta: possibilita a criação de uma conta bancária com os seguintes parâmetros: nome do cliente, 
email do cliente,  CPF do cliente, data de nascimento do cliente. Em seguida, o sistema retorna os dados cadastrados.  

- Efetuar saque: possibilita que o cliente efetue um saque da sua conta bancária. Por padrão, toda conta cadastrada 
inicia com um saldo de R$ 100,00, e ele só pode sacar o valor total do seu saldo + os R$ 100,00 de limite.

- Efetuar depósito: possibilita que o cliente efetue um depósito na sua conta.

- Efetuar transferência: possibilita que o cliente faça uma transferência para outra conta existente cadastrada. Os 
valores de ambas as contas são ajustados ao término da operação

- Listar contas: lista com todas as contas cadastradas no sistema.