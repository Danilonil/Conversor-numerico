from funções import *

janela = True
while janela == True:

    loop = True
    while loop == True:
        loop = False
        print('\n Escolha a base numérica do seu número: \n')
        base = escolha_base()
        if base == 'binário':
            base = 2

        elif base == 'decimal':
            base = 10

        elif base == 'octodecimal':
            base = 8

        elif base == 'hexadecimal':
            base = 16

        else:
            loop = True
            print('\n\n\t*** Base invalido ***')
            
    linha()
    loop = True
    while loop == True:
        loop = False
        n = input('\n Digite aqui o número que quer converter: \t').upper().strip().split()
        n = ''.join(n)
        resultado = verifica(n, base) 
        if resultado == True:
            linha()

        else:
            loop = True
            print('\n\n\t*** Número invalido ***')

            

    linha()
    if base == 'binário' or 'octodecimal' or 'hexadecimal':
        n_dec = converte_dec(n, base)

    loop = True
    while loop == True:
        loop = False
        print(f'\n O número {n} está na base {base}.')
        print('\n Para qual base você quer converter ele? \n')
        base_convert = escolha_base()
        if base_convert == 'binário':
            base_convert = 2
            linha()
            print(f' O número {n}, na base {base} = {converte(n_dec, base_convert)}, na base {base_convert}')

        elif base_convert == 'decimal':
            base_convert = 10
            linha()
            print(f' O número {n}, na base {base} = {n_dec}, na base {base_convert}')

        elif base_convert == 'octodecimal':
            base_convert = 8
            linha()
            print(f' O número {n}, na base {base} = {converte(n_dec, base_convert)}, na base {base_convert}')

        elif base_convert == 'hexadecimal':
            base_convert = 16
            linha()
            print(f' O número {n}, na base {base} = {converte(n_dec, base_convert)}, na base {base_convert}')

        else:
            loop = True
            print('\n\n\t*** Base invalido ***')
        
    linha()
    loop = True
    while loop == True:
        print('\n Deseja continuar? ')
        resposta = input('\n\t Digite [S] PARA CONTINUAR \n\t Digite [N] PARA FECHAR O PROGRAMA \n\t\t\t').upper().strip()

        if resposta == 'S':
            loop = False
            pass
        
        elif resposta == 'N':
            loop = False
            janela = False
            pass
        
        linha()

print(' \n Fim do programa')
linha()

