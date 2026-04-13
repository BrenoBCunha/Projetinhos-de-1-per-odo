import tkinter as tk

valor = '0'
ans = 0

def pressc():
    global valor
    valor = '0'
    lbl_result['text'] = f'{valor}'

def press1():
    global valor
    global ans
    valor = lbl_result['text']
    copia = valor.replace('.', '')   # exclui a pontuação do valor 
    if valor == f'{0}':
        valor = '1'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '1'
        ans = 0
    else:
        valor += '1'
    lbl_result['text'] = f'{valor}'

def press2():
    global valor
    global ans
    copia = valor.replace('.', '')
    valor = lbl_result['text']
    if valor == f'{0}':
        valor = '2'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '2'
        ans = 0
    else:
        valor += '2'
    lbl_result['text'] = f'{valor}'

def press3():
    global valor
    global ans
    copia = valor.replace('.', '')
    valor = lbl_result['text']
    if valor == f'{0}':
        valor = '3'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '3'
        ans = 0
    else:
        valor += '3'
    lbl_result['text'] = f'{valor}'

def press4():
    global valor
    global ans
    copia = valor.replace('.', '')
    valor = lbl_result['text']
    if valor == f'{0}':
        valor = '4'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '4'
        ans = 4
    else:
        valor += '4'
    lbl_result['text'] = f'{valor}'

def press5():
    global valor
    global ans
    copia = valor.replace('.', '')
    valor = lbl_result['text']
    if valor == f'{0}':
        valor = '5'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '5'
        ans = 0
    else:
        valor += '5'
    lbl_result['text'] = f'{valor}'

def press6():
    global valor
    global ans
    copia = valor.replace('.', '')
    valor = lbl_result['text']
    if valor == f'{0}':
        valor = '6'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '6'
        ans = 0
    else:
        valor += '6'
    lbl_result['text'] = f'{valor}'

def press7():
    global valor
    global ans
    copia = valor.replace('.', '')
    valor = lbl_result['text']
    if valor == f'{0}':
        valor = '7'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '7'
        ans = 0
    else:
        valor += '7'
    lbl_result['text'] = f'{valor}'

def press8():
    global valor
    global ans
    copia = valor.replace('.', '')
    valor = lbl_result['text']
    if valor == f'{0}':
        valor = '8'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '8'
        ans = 0
    else:
        valor += '8'
    lbl_result['text'] = f'{valor}'

def press9():
    global valor
    global ans
    copia = valor.replace('.', '')
    valor = lbl_result['text']
    if valor == f'{0}':
        valor = '9'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '9'
        ans = 0
    else:
        valor += '9'
    lbl_result['text'] = f'{valor}'

def press0():
    global valor
    global ans
    copia = valor.replace('.', '')
    valor = lbl_result['text']
    if valor == f'{0}':
        valor = '0'
    elif ans != 0 and copia.isnumeric() == True:
        valor = '0'
        ans = 0
    else:
        valor += '0'
    lbl_result['text'] = f'{valor}'

def press_som():
    global valor
    if valor == '0':
        valor = valor
    elif '%' in valor:
        valor = valor
    elif valor[len(valor)-1] not in '+-x/.%':
        valor += '+'
        lbl_result['text'] = f'{valor}'
    else:
        valor = valor

def press_sub():
    global valor
    if valor == '0':
        valor = '-'
        lbl_result['text'] = f'{valor}'
    elif '%' in valor:
        valor = valor
    elif valor[len(valor)-1] not in '+-x/.%':
        valor += '-'
        lbl_result['text'] = f'{valor}'
    else:
        valor = valor

def press_mul():
    global valor
    if valor == '0':
        valor = valor
    elif '%' in valor:
        valor = valor
    elif valor[len(valor)-1] not in '+-x/.%':
        valor += 'x'
        lbl_result['text'] = f'{valor}'
    else:
        valor = valor

def press_div():
    global valor
    if valor == '0':
        valor = valor
    elif '%' in valor:
        valor = valor
    elif valor[len(valor)-1] not in '+-x/.%':
        valor += '/'
        lbl_result['text'] = f'{valor}'
    else:
        valor = valor

def press_pct():
    global valor
    if valor == '0':
        valor = valor
    elif '%' in valor:
        valor = valor
    elif valor[len(valor)-1] not in '+-x/.%':
        valor += '%'
        lbl_result['text'] = f'{valor}'
    else:
        valor = valor

def press_dot():
    global valor
    global ans
    if ans != 0:
        valor = '0.'
        ans = 0
        lbl_result['text'] = f'{valor}'
    elif valor[len(valor)-1] not in '+-x/.' and '.' not in valor:
        valor += '.'
        lbl_result['text'] = f'{valor}'
    else:
        valor = valor

def press_del():
    global valor
    if valor != '0':
        valor = valor[:-1]
        if valor == '':
            valor = '0'
            lbl_result['text'] = f'{valor}'
        lbl_result['text'] = f'{valor}'
    else:
        valor = '0'
        lbl_result['text'] = f'{valor}'

def press_sqrt():
    from math import sqrt
    global valor
    global ans
    operador = list()
    operacao = list()
    result = 0
    for e in valor:
        if e == '.':
            e = e
        elif e == valor[0] and valor[0] == '-':
            e = e
        elif e.isnumeric() == False:
            operador.append(e)
    for e in valor:
        if e == '.':
            e = e
        elif e == valor[0] and valor[0] == '-':
            e = e
        elif e.isnumeric() == False:
            valor = valor.replace(e, ' ')
    numeros = valor.split()
    if operador == []:
        result = float(numeros[0])
        result = sqrt(result)
    else:
        for e in operador:
            if e == operador[0]:
                result = float(numeros[0])
            if e == '/':
                result = result / float(numeros[1])
                numeros.pop(0)
            elif e == 'x':
                result = result * float(numeros[1])
                numeros.pop(0)
            elif e == '+':
                result = result + float(numeros[1])
                numeros.pop(0)
            elif e == '-':
                result = result - float(numeros[1])
                numeros.pop(0)
            elif e == '%':
                result = (result * float(numeros[1])) / 100
                numeros.pop(0)
            if len(numeros) == 1:
                break
        result = sqrt(result)
    ans = result
    result = f'{result:.10}'
    valor = result
    lbl_result['text'] = f'{valor}'

def key_press(event):
    k = event.char
    if k == '1':
        press1()
    elif k == '2':
        press2()
    elif k == '3':
        press3()
    elif k == '4':
        press4()
    elif k == '5':
        press5()
    elif k == '6':
        press6()
    elif k == '7':
        press7()
    elif k == '8':
        press8()
    elif k == '9':
        press9()
    elif k == '0':
        press0()
    elif k == '+':
        press_som()
    elif k == '-':
        press_sub()
    elif k == 'x' or k == '*':
        press_mul()
    elif k == '/':
        press_div()
    elif k == '.' or k == ',':
        press_dot()
    elif k == '=':
        press_igu()
    elif k == '%':
        press_pct()

def enter_press(event):
    press_igu()

def back_press(event):
    press_del()

def esc_press(event):
    pressc()

def press_igu():
    global valor
    global ans
    operador = list()
    operacao = list()
    result = 0
    for e in valor:
        if e == '.':
            e = e
        elif e == valor[0] and valor[0] == '-':
            e = e
        elif e.isnumeric() == False:
            operador.append(e)
    for e in valor:
        if e == '.':
            e = e
        elif e == valor[0] and valor[0] == '-':
            e = e
        elif e.isnumeric() == False:
            valor = valor.replace(e, ' ')
    numeros = valor.split()
    for e in operador:
        if e == operador[0]:
            result = float(numeros[0])
        if e == '/':
            result = result / float(numeros[1])
            numeros.pop(0)
        elif e == 'x':
            result = result * float(numeros[1])
            numeros.pop(0)
        elif e == '+':
            result = result + float(numeros[1])
            numeros.pop(0)
        elif e == '-':
            result = result - float(numeros[1])
            numeros.pop(0)
        elif e == '%':
            result = (result * float(numeros[1])) / 100
            numeros.pop(0)
        if len(numeros) == 1:
            break
    ans = result
    result = f'{result:.10}'
    valor = result
    lbl_result['text'] = f'{valor}'
        


### Interface Tkinter ###

root = tk.Tk()
root.geometry('198x265')
root.title('Calculadora')
root.bind('<Key>', key_press)
root.bind('<Return>', enter_press)
root.bind('<BackSpace>', back_press)
root.bind('<Escape>', esc_press)
root.resizable(width = False, height = False)

### números ###

btn_1 = tk.Button(root, text = '7', width = 3, font = ('Arial', 16), command = press7)
btn_1.place(x = 5, y = 92)

btn_2 = tk.Button(root, text = '8', width = 3, font = ('Arial', 16), command = press8)
btn_2.place(x = 52, y = 92)

btn_3 = tk.Button(root, text = '9', width = 3, font = ('Arial', 16), command = press9)
btn_3.place(x = 99, y = 92)

btn_4 = tk.Button(root, text = '4', width = 3, font = ('Arial', 16), command = press4)
btn_4.place(x = 5, y = 134)

btn_5 = tk.Button(root, text = '5', width = 3, font = ('Arial', 16), command = press5)
btn_5.place(x = 52, y = 134)

btn_6 = tk.Button(root, text = '6', width = 3, font = ('Arial', 16), command = press6)
btn_6.place(x = 99, y = 134)

btn_7 = tk.Button(root, text = '1', width = 3, font = ('Arial', 16), command = press1)
btn_7.place(x = 5, y = 176)

btn_8 = tk.Button(root, text = '2', width = 3, font = ('Arial', 16), command = press2)
btn_8.place(x = 52, y = 176)

btn_9 = tk.Button(root, text = '3', width = 3, font = ('Arial', 16), command = press3)
btn_9.place(x = 99, y = 176)

btn_0 = tk.Button(root, text = '0', width = 3, font = ('Arial', 16), command = press0)
btn_0.place(x = 52, y = 218)

### Operadores ###

btn_som = tk.Button(root, text = '+', width = 3, font = ('Arial', 16), command = press_som)
btn_som.place(x = 146, y = 50)

btn_sub = tk.Button(root, text = '-', width = 3, font = ('Arial', 16), command = press_sub)
btn_sub.place(x = 146, y = 92)

btn_div = tk.Button(root, text = '/', width = 3, font = ('Arial', 16), command = press_div)
btn_div.place(x = 146, y = 134)

btn_mul = tk.Button(root, text = 'x', width = 3, font = ('Arial', 16), command = press_mul)
btn_mul.place(x = 146, y = 176)

btn_igu = tk.Button(root, text = '=', width = 3, font = ('Arial', 16), bg = '#00A8FF', command = press_igu)
btn_igu.place(x = 146, y = 218)

btn_c = tk.Button(root, text = 'C', width = 3, font = ('Arial', 16), command = pressc)
btn_c.place(x = 5, y = 50)

btn_dot = tk.Button(root, text = '.', width = 3, font = ('Arial', 16), command = press_dot)
btn_dot.place(x = 99, y = 218)

btn_del = tk.Button(root, text = '\u232B', width = 3, font = ('Arial', 16), command = press_del)
btn_del.place(x = 52, y = 50)

btn_pct = tk.Button(root, text = '%', width = 3, font = ('Arial', 16), command = press_pct)
btn_pct.place(x = 99, y = 50)

btn_sqrt = tk.Button(root, text = '\u221A', width = 3, font = ('Arial', 16), command = press_sqrt)
btn_sqrt.place(x = 5, y = 218)

### Mostrador ###

fm_tela = tk.Frame(root, width = 188, height = 50, bd = 3, relief =tk.RIDGE)
fm_tela.place(x = 5, y = 0)
fm_tela.pack_propagate(False)

lbl_result = tk.Label(fm_tela, text = f'{valor}', font = ('Arial', 22), anchor = 'e')
lbl_result.pack(expand=True, fill=tk.BOTH)

root.mainloop()