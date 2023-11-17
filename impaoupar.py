#Par ou impar com Funções:

def par_impar(x):
    if (x % 2 == 0):
        return 'par'
    else:
        return 'impar'
    
print(par_impar(int(input('Digite o valor inteiro:'))))