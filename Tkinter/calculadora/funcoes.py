valor = '0'
ans = 0

def key_press(event, label):
    k = event.char
    press(k, label)

def enter_press(event, label):
    calcular(label)

def back_press(event, label):
    delete(label)

def esc_press(event, label):
    press('c', label)

def press(n, label):
    global valor
    global ans
    valor = label['text']
    copia = valor.replace('.', '')   # exclui a pontuação do valor 
    if n == 'c':
        valor = '0'
    elif valor == '0':
        valor = f'{n}'
    elif ans != 0 and copia.isnumeric() == True:
        valor = f'{n}'
        ans = 0
    else:
        valor += f'{n}'
    label['text'] = valor

def delete(label):
    global valor
    if valor != '0':
        valor = valor[:-1]
        if valor == '':
            valor = '0'
            label['text'] = f'{valor}'
        label['text'] = f'{valor}'
    else:
        valor = '0'
        label['text'] = f'{valor}'

def operador(n, label):
    global valor
    global ans
    if valor == '0':
        valor = valor
    elif '%' in valor:
        valor = valor
    elif valor[len(valor)-1] not in '+-x/.%':
        valor += f'{n}'
        label['text'] = valor
    else:
        valor = valor

def ponto(label):
    global valor
    global ans
    if ans != 0:
        valor = '0.'
        ans = 0
        label['text'] = valor
    elif valor[len(valor)-1] not in '+-x/.' and '.' not in valor:
        valor += '.'
        label['text'] = valor
    else:
        valor = valor

def raiz(label):
    from math import sqrt
    global valor
    calcular(label)
    resu = sqrt(float(valor))
    valor = f'{resu:.9}'
    label['text'] = valor

def calcular(label):
    global valor
    global ans
    operadores = list(filter(lambda x: x.isnumeric() == False and x != '.', valor))
    numeros = ''.join(list(map(lambda x: ' ' if x.isnumeric()==False and x != '.' else x, valor))).split()
    while len(operadores) > 0:
        for i, e in enumerate(operadores):
            if e == '/':
                resu = float(numeros[i])
                resu /= float(numeros[i+1])
                operadores.pop(i)
                numeros.insert(i, resu)
                numeros.pop(i+1)
                numeros.pop(i+1)
        for i, e in enumerate(operadores):
            if e == 'x':
                resu = float(numeros[i])
                resu *= float(numeros[i+1])
                operadores.pop(i)
                numeros.insert(i, resu)
                numeros.pop(i+1)
                numeros.pop(i+1)
        for i, e in enumerate(operadores):
            if e == '+':
                resu = float(numeros[i])
                resu += float(numeros[i+1])
                operadores.pop(i)
                numeros.insert(i, resu)
                numeros.pop(i+1)
                numeros.pop(i+1)
        for i, e in enumerate(operadores):
            if e == '-':
                resu = float(numeros[i])
                resu -= float(numeros[i+1])
                operadores.pop(i)
                numeros.insert(i, resu)
                numeros.pop(i+1)
                numeros.pop(i+1)
        for i, e in enumerate(operadores):
            if e == '%':
                resu = float(numeros[i])
                resu = float(numeros[i+1]) * resu/100
                operadores.pop(i)
                numeros.insert(i, resu)
                numeros.pop(i+1)
                numeros.pop(i+1)
    ans = resu
    valor = f'{resu:.9}'
    label['text'] = valor
