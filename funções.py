
def escolha_base():
    base_n = ('binário', 'decimal', 'octodecimal', 'hexadecimal')

    for i, base in enumerate(base_n):
        print(f'{i+1}- {base}')

    escolha = input('\n Use o teclado numérico: \t').strip()

    if escolha.isnumeric():
        escolha = int(escolha)
        if escolha in range(1, 5):
            for i, base in enumerate(base_n):
                if escolha == i+1:
                    return base


#-----------------------------------------------------------------------------------

def verifica(numero, base):
    if base == 16:
        numero = numero.replace('A', '10')
        numero = numero.replace('B', '11')  
        numero = numero.replace('C', '12') 
        numero = numero.replace('D', '13') 
        numero = numero.replace('E', '14') 
        numero = numero.replace('F', '15')
    for num in numero: 
        if not num.isnumeric() or int(num) >= base:
            return False


#------------------------------------------------------------------------------------

def converte(numero, base):
    resto_div = []  
    numero = int(numero)
    if numero < base:
        resto_div.append(str(numero))

    while numero >= base:
        resto = numero % base
        numero = numero // base
        resto_div.append(str(resto))

        if numero < base:
            resto_div.append(str(numero))

    if base == 16:
        num_convert = ''
        for resto in resto_div:
            resto = resto.replace('10', 'A')
            resto = resto.replace('11', 'B')  
            resto = resto.replace('12', 'C') 
            resto = resto.replace('13', 'D') 
            resto = resto.replace('14', 'E') 
            resto = resto.replace('15', 'F')
            num_convert += resto

        return num_convert[::-1]

    return ''.join(resto_div[::-1])


#-----------------------------------------------------------------------------------

def converte_dec(numero, base):

    num_dec = 0
    cont = 0
    for num in numero[::-1]:
        num = num.replace('A', '10')
        num = num.replace('B', '11')  
        num = num.replace('C', '12') 
        num = num.replace('D', '13') 
        num = num.replace('E', '14') 
        num = num.replace('F', '15')
        num = int(num)
        result = num * base ** cont
        num_dec += result
        cont += 1

    return num_dec

#-----------------------------------------------------------------------------------

def linha():
    print('\n', '---'*40, '\n')







