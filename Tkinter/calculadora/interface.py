import tkinter as tk
import funcoes as fun

root = tk.Tk()
root.geometry('198x307')
root.title('Calculadora')
root.resizable(width = False, height = False)


### Mostrador ###

etr_result = tk.Entry(root, width = 12, font=('Arial', 20), justify='right', state='readonly', bd = 3)
etr_result.place(x = 5, y = 5)

### botões do teclado###

root.bind('<Key>', lambda event: fun.key_press(event, etr_result))
root.bind('<Return>', lambda event: fun.enter_press(event, etr_result))
root.bind('<BackSpace>', lambda event: fun.back_press(event, etr_result))
root.bind('<Escape>', lambda event: fun.esc_press(event, etr_result))

### números ###

btn_7 = tk.Button(root, text = '7', width = 3, font = ('Arial', 16), command= lambda: fun.press('7', etr_result))
btn_7.place(x = 5, y = 134)

btn_8 = tk.Button(root, text = '8', width = 3, font = ('Arial', 16), command= lambda: fun.press('8', etr_result))
btn_8.place(x = 52, y = 134)

btn_9 = tk.Button(root, text = '9', width = 3, font = ('Arial', 16), command= lambda: fun.press('9', etr_result))
btn_9.place(x = 99, y = 134)

btn_4 = tk.Button(root, text = '4', width = 3, font = ('Arial', 16), command= lambda: fun.press('4', etr_result))
btn_4.place(x = 5, y = 176)

btn_5 = tk.Button(root, text = '5', width = 3, font = ('Arial', 16), command= lambda: fun.press('5', etr_result))
btn_5.place(x = 52, y = 176)

btn_6 = tk.Button(root, text = '6', width = 3, font = ('Arial', 16), command= lambda: fun.press('6', etr_result))
btn_6.place(x = 99, y = 176)

btn_1 = tk.Button(root, text = '1', width = 3, font = ('Arial', 16), command= lambda: fun.press('1', etr_result))
btn_1.place(x = 5, y = 218)

btn_2 = tk.Button(root, text = '2', width = 3, font = ('Arial', 16), command= lambda: fun.press('2', etr_result))
btn_2.place(x = 52, y = 218)

btn_3 = tk.Button(root, text = '3', width = 3, font = ('Arial', 16), command= lambda: fun.press('3', etr_result))
btn_3.place(x = 99, y = 218)

btn_0 = tk.Button(root, text = '0', width = 7, font = ('Arial', 16), command= lambda: fun.press('0', etr_result))
btn_0.place(x = 5, y = 260)

### Operadores ###

btn_som = tk.Button(root, text = '+', width = 3, font = ('Arial', 16), command= lambda: fun.press('+', etr_result))
btn_som.place(x = 146, y = 92)

btn_sub = tk.Button(root, text = '-', width = 3, font = ('Arial', 16), command= lambda: fun.press('-', etr_result))
btn_sub.place(x = 146, y = 134)

btn_div = tk.Button(root, text = '/', width = 3, font = ('Arial', 16), command= lambda: fun.press('/', etr_result))
btn_div.place(x = 146, y = 176)

btn_mul = tk.Button(root, text = 'x', width = 3, font = ('Arial', 16), command= lambda: fun.press('x', etr_result))
btn_mul.place(x = 146, y = 218)

btn_igu = tk.Button(root, text = '=', width = 3, font = ('Arial', 16), bg = '#00A8FF', command= lambda: fun.calcular(etr_result))
btn_igu.place(x = 146, y = 260)

btn_c = tk.Button(root, text = 'C', width = 3, font = ('Arial', 16), command= lambda: fun.press('c', etr_result))
btn_c.place(x = 5, y = 50)

btn_dot = tk.Button(root, text = '.', width = 3, font = ('Arial', 16), command = lambda: fun.press('.', etr_result))
btn_dot.place(x = 99, y = 260)

btn_del = tk.Button(root, text = '\u232B', width = 3, font = ('Arial', 16), command= lambda: fun.delete(etr_result))
btn_del.place(x = 52, y = 50)

btn_powy = tk.Button(root, text = 'x^y', width = 3, font = ('Arial', 16), command= lambda: fun.press('^', etr_result))
btn_powy.place(x = 5, y = 92)

btn_pow = tk.Button(root, text = 'x^2', width = 3, font = ('Arial', 16), command= lambda: fun.pow(etr_result))
btn_pow.place(x = 52, y = 92)

btn_sqrt = tk.Button(root, text = '\u221Ax', width = 3, font = ('Arial', 16), command= lambda: fun.raiz(etr_result))
btn_sqrt.place(x = 99, y = 92)

btn_bracel = tk.Button(root, text = '(', width = 3, font = ('Arial', 16), command= lambda: fun.press('(', etr_result))
btn_bracel.place(x = 99, y = 50)

btn_bracer = tk.Button(root, text = ')', width = 3, font = ('Arial', 16), command= lambda: fun.press(')', etr_result))
btn_bracer.place(x = 146, y = 50)

root.mainloop()