valorbs = valorc = valorbo = valorh = valorch = valorr = valort = 0
print('-'*50)
print('LANCHONETE'.center(50))
print('-'*50)
print('''
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
''')
print('-'*50)
# fazer pedido
while True:
    p = int(input('Digite o código do alimento[999 para sair]: '))
    if p == 100:
        q = int(input('Digite quantos Cachorros Quentes quer comprar: '))
        valorc += 1.20 * q
    if p == 101:
        q = int(input('Digite quantos Bauru Simples quer comprar: '))
        valorbs = 1.30 * q
    if p == 102:
        q = int(input('Digite quantos Bauru com Ovo quer comprar: '))
        valorbo = 1.50 * q
    if p == 103:
        q = int(input('Digite quantos Hambúrguer quer comprar: '))
        valorh = 1.20 * q
    if p == 104:
        q = int(input('Digite quantos Ceeseburguer quer comprar: '))
        valorch = 1.30 * q
    if p == 105:
        q = int(input('Digite quantos Refrigerante quer comprar: '))
        valorr = 1.00 * q
    if p == 999:
        break
    valort = valorc + valorbs + valorbo + valorh + valorch + valorr
print('-'*50)
print(f'O valor total a pagar é de R${valort:.2f}')
print('Obrigado, volte sempre!')