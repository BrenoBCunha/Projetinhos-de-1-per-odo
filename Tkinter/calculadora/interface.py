import tkinter as tk
import funcoes as fun

root = tk.Tk()
root.geometry('198x265')
root.title('Calculadora')
root.resizable(width = False, height = False)


### Mostrador ###

fm_tela = tk.Frame(root, width = 188, height = 50, bd = 3, relief =tk.RIDGE)
fm_tela.place(x = 5, y = 0)
fm_tela.pack_propagate(False)

lbl_result = tk.Label(fm_tela, text = '0', font = ('Arial', 22), anchor = 'e')
lbl_result.pack(expand=True, fill=tk.BOTH)

### botões do teclado###

root.bind('<Key>', lambda event: fun.key_press(event, lbl_result))
root.bind('<Return>', lambda event: fun.enter_press(event, lbl_result))
root.bind('<BackSpace>', lambda event: fun.back_press(event, lbl_result))
root.bind('<Escape>', lambda event: fun.esc_press(event, lbl_result))

### números ###

btn_7 = tk.Button(root, text = '7', width = 3, font = ('Arial', 16), command= lambda: fun.press(7, lbl_result))
btn_7.place(x = 5, y = 92)

btn_8 = tk.Button(root, text = '8', width = 3, font = ('Arial', 16), command= lambda: fun.press(8, lbl_result))
btn_8.place(x = 52, y = 92)

btn_9 = tk.Button(root, text = '9', width = 3, font = ('Arial', 16), command= lambda: fun.press(9, lbl_result))
btn_9.place(x = 99, y = 92)

btn_4 = tk.Button(root, text = '4', width = 3, font = ('Arial', 16), command= lambda: fun.press(4, lbl_result))
btn_4.place(x = 5, y = 134)

btn_5 = tk.Button(root, text = '5', width = 3, font = ('Arial', 16), command= lambda: fun.press(5, lbl_result))
btn_5.place(x = 52, y = 134)

btn_6 = tk.Button(root, text = '6', width = 3, font = ('Arial', 16), command= lambda: fun.press(6, lbl_result))
btn_6.place(x = 99, y = 134)

btn_1 = tk.Button(root, text = '1', width = 3, font = ('Arial', 16), command= lambda: fun.press(1, lbl_result))
btn_1.place(x = 5, y = 176)

btn_2 = tk.Button(root, text = '2', width = 3, font = ('Arial', 16), command= lambda: fun.press(2, lbl_result))
btn_2.place(x = 52, y = 176)

btn_3 = tk.Button(root, text = '3', width = 3, font = ('Arial', 16), command= lambda: fun.press(3, lbl_result))
btn_3.place(x = 99, y = 176)

btn_0 = tk.Button(root, text = '0', width = 3, font = ('Arial', 16), command= lambda: fun.press(0, lbl_result))
btn_0.place(x = 52, y = 218)

### Operadores ###

btn_som = tk.Button(root, text = '+', width = 3, font = ('Arial', 16), command= lambda: fun.operador('+', lbl_result))
btn_som.place(x = 146, y = 50)

btn_sub = tk.Button(root, text = '-', width = 3, font = ('Arial', 16), command= lambda: fun.operador('-', lbl_result))
btn_sub.place(x = 146, y = 92)

btn_div = tk.Button(root, text = '/', width = 3, font = ('Arial', 16), command= lambda: fun.operador('/', lbl_result))
btn_div.place(x = 146, y = 134)

btn_mul = tk.Button(root, text = 'x', width = 3, font = ('Arial', 16), command= lambda: fun.operador('x', lbl_result))
btn_mul.place(x = 146, y = 176)

btn_igu = tk.Button(root, text = '=', width = 3, font = ('Arial', 16), bg = '#00A8FF', command= lambda: fun.calcular(lbl_result))
btn_igu.place(x = 146, y = 218)

btn_c = tk.Button(root, text = 'C', width = 3, font = ('Arial', 16), command= lambda: fun.press('c', lbl_result))
btn_c.place(x = 5, y = 50)

btn_dot = tk.Button(root, text = '.', width = 3, font = ('Arial', 16), command = lambda: fun.ponto(lbl_result))
btn_dot.place(x = 99, y = 218)

btn_del = tk.Button(root, text = '\u232B', width = 3, font = ('Arial', 16), command= lambda: fun.delete(lbl_result))
btn_del.place(x = 52, y = 50)

btn_pct = tk.Button(root, text = '%', width = 3, font = ('Arial', 16), command= lambda: fun.operador('%', lbl_result))
btn_pct.place(x = 99, y = 50)

btn_sqrt = tk.Button(root, text = '\u221A', width = 3, font = ('Arial', 16), command= lambda: fun.raiz(lbl_result))
btn_sqrt.place(x = 5, y = 218)

root.mainloop()