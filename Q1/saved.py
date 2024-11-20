#Буква А и расположение
lbl_A = tk.Label(frame, text='A', font=('Arial', 30), bg='blue', fg='white')
lbl_A.grid(column=0, row=0, padx=10, pady=15)

#Создание окна аргумента А
arg_A = tk.Entry(frame, width=10)
arg_A.insert(0, '1')

#Расположение окна аргумента А
arg_A.grid(column=0, row=1, padx=10, pady=15)

#Буква В и расположение
lbl_B = tk.Label(frame, text='B', font=('Arial', 30))
lbl_B.grid(column=1, row=0, padx=10, pady=15)

#Создание окна аргумента В
arg_B = tk.Entry(frame, width=10)
arg_B.insert(0, '0')

#Расположение окна аргумента В
arg_B.grid(column=1, row=1, padx=10, pady=15)

#Буква С и расположение
lbl_C = tk.Label(frame, text='C', font=('Arial', 30))
lbl_C.grid(column=2, row=0, padx=10, pady=15)

#Создание окна аргумента С
arg_C = tk.Entry(frame, width=10)
arg_C.insert(0, '0')

#Расположение окна аргумента С
arg_C.grid(column=2, row=1, padx=10, pady=15) 

#Слово Result в сетке
lbl_roots = tk.Label(frame, text='Result:')
lbl_roots.grid(column=1, row=2)

#Слово None yet в сетке
lbl_result = tk.Label(frame, text='None yet.', font=('Arial', 10))
lbl_result.grid(column=2, row=2) 

#showinfo(title= "keys", message= keys_var)



def generate():
    
    p=int(arg_number_keys.get())
    k=0
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


    for fragment11 in alf:
        for fragment12 in alf:
            for fragment13 in alf:
                for fragment14 in alf:
                    for fragment15 in alf:
                        el3 = fragment11 + fragment12 + fragment13 + fragment14 + fragment15
                        if el3.count("0")+el3.count("1")+el3.count("2")+el3.count("3")+el3.count("4")+el3.count("5")+el3.count("6")+el3.count("7")+el3.count("8")+el3.count("9") == 2:
                            for fragment6 in alf:
                                for fragment7 in alf:
                                    for fragment8 in alf:
                                        for fragment9 in alf:
                                            for fragment10 in alf:
                                                el2 = fragment6+fragment7+fragment8+fragment9+fragment10
                                                if el2.count("0")+el2.count("1")+el2.count("2")+el2.count("3")+el2.count("4")+el2.count("5")+el2.count("6")+el2.count("7")+el2.count("8")+el2.count("9") == 2:
                                                    for fragment1 in alf: 
                                                        for fragment2 in alf:
                                                            for fragment3 in alf:
                                                                for fragment4 in alf:
                                                                    for fragment5 in alf:
                                                                        el1 = fragment1+fragment2+fragment3+fragment4+fragment5
                                                                        if el1.count("0")+el1.count("1")+el1.count("2")+el1.count("3")+el1.count("4")+el1.count("5")+el1.count("6")+el1.count("7")+el1.count("8")+el1.count("9") == 2:
                                                                            key=el1 + "-" + el2 + "-" + el3
                                                                            k+=1
                                                                            keys.append(key)
                                                                            if k == p:
                                                                                continue
    return keys




def show_keys():
    keys_var = Variable(value=keys)
    window = Tk()
    window.title("Keys")
    window.geometry("250x200")

    label=ttk.Label(window, text=keys_var)
    label.pack(anchor=NW, padx=1, pady=1)
    
    
    
    
    
    
    
    
         
        """ for i in range(3):
            random_alf = random.choice(alf)
            element0.append(random_alf)
        for j in range(2):
            random_figure = random.choice(figure)
            element0.append(random_figure)
        random.shuffle(element0)

        for i in range(3):
            random_alf = random.choice(alf)
            element1.append(random_alf)
        for j in range(2):
            random_figure = random.choice(figure)
            element1.append(random_figure)
        random.shuffle(element1)

        for i in range(3):
            random_alf = random.choice(alf)
            element2.append(random_alf)
        for j in range(2):
            random_figure = random.choice(figure)
            element2.append(random_figure)
        random.shuffle(element2)

        key = element0 + ['-'] + element1 + ['-'] + element2 """

        """ keys.append(''.join(key))
    return keys """