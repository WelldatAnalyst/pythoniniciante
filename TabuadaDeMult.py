num =int(input('Digite o numero para calcular a tabuada:'))

print(f'TABUADA DO {num}:')

for i in range (1,11,1):
  print(f'{i} x {num} = {i * num}')