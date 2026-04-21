resu = 0

def key_press(event, etr):
    k = event.char
    press(k, etr)

def enter_press(event, etr):
    calcular(etr)

def back_press(event, etr):
    delete(etr)

def esc_press(event, etr):
    press('c', etr)    

def delete(etr):
    etr.config(state='normal')
    etr.delete(len(etr.get()) - 1)
    etr.config(state='readonly')

def pow(etr):
    press('^', etr)
    press('2', etr)

def raiz(etr):
    from math import sqrt
    global resu
    etr.config(state='normal')
    resu = sqrt(resu)
    etr.delete(0, 'end')
    etr.insert(0, resu)
    etr.config(state='readonly')

def calcular(etr):
    global resu
    etr.config(state='normal')
    try:
        resu = eval(etr.get().replace('x', '*').replace('^', '**'))
    except:
        resu = 'error'
        etr.delete(0, 'end')
        etr.insert('end', resu)
        resu = 0
    else:
        etr.delete(0, 'end')
        etr.insert('end', resu)
    etr.config(state='readonly')

def press(n, etr):
    global resu
    etr.config(state='normal')
    if n == 'c':
            resu = 0
            etr.delete(0, 'end')
    elif resu != 0 and n not in 'x/+-.%^' and etr.get()[-1] not in 'x/+-.%^()':
        resu = 0 
        etr.delete(0, 'end')
        etr.insert('end', n)
    else:
        if n in 'x/+-.%()^' or n.isnumeric() == True:
            if etr.get() == '':
                if n not in 'x/+-.%^':
                    etr.insert('end', n)
            elif etr.get()[-1] in 'x/+-.%^' and n in 'x/+-.%^':
                resu=0
            else:
                etr.insert('end', n)
    etr.config(state='readonly')