Salario = float (input('Qual seu salário?'))
Ano_Admissão =int (input('Ano de admissão'))
Ano_Atual = int(input('Em que ano estamos'))

tempo = Ano_Atual - Ano_Admissão
if(tempo > 10):
    Bonus = Salario * 0.3
else:
    if (tempo > 5):
        Bonus = Salario *0.2
    else:
        Bonus = Salario * 0.1
    
print(f'Você tem {tempo} anos dentro da empresa.')
print(f' Seu salario é de {Salario}.')
print(f' E sua bonificação é de {Bonus}')
print(f'Salario final:{Salario + Bonus}')