""" from tkinter import *

from tkinter import ttk
 
def show_message():
    label["text"] = entry.get()     # получаем введенный текст
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200") 
 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
  
btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6) """

""" from tkinter import *

from tkinter import ttk
  
keys = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go",
             "T-SQL", "PL-SQL", "Typescript"]
  
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
  
keys_var = StringVar(value=keys)
listbox = Listbox(listvariable=keys_var)
listbox.pack(expand=1, fill=BOTH)
# сдвигаем скрол на 1 элемент внизу
listbox.yview_scroll(number=1, what="units")
 
root.mainloop() """

""" import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)  
random_number = random.choice(numbers)
print(random_number) """
""" 
import random
for 
    keys = []
    p = 5
    k = 0
    alf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    figure = ['0','1','2','3','4','5','6','7','8','9']
    el0 = []
    el1 = []
    el2 = []
    for i in range(3):
        random_alf = random.choice(alf)
        el0.append(random_alf)
    for j in range(2):
        random_figure = random.choice(figure)
        el0.append(random_figure)
    random.shuffle(el0)

    for i in range(3):
        random_alf = random.choice(alf)
        el1.append(random_alf)
    for j in range(2):
        random_figure = random.choice(figure)
        el1.append(random_figure)
    random.shuffle(el1)

    for i in range(3):
        random_alf = random.choice(alf)
        el2.append(random_alf)
    for j in range(2):
        random_figure = random.choice(figure)
        el2.append(random_figure)
    random.shuffle(el2)

    key = el0 + ['-'] + el1 + ['-'] + el2

    print(''.join(key)) """


"""     

    p = int(arg_number_of_keys.get())
    k = 0
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    figure = "0123456789"
    el0 = []
    el1 = []
    el2 = []
    while p <= k:
        for ij in range(3):
            for i in range(3):
                fr = random.choince(alf)
                el0.append(fr) 
            for j in range(2):
                fr = random.choince(figure)
                el0.append(fr) 
        
        key = el0 + "-" + el1 + "-" + el2
        k += 1
        keys.append(key)
        if k == p:
            continue
    return keys """

""" from tkinter import *

keys = ["123","123","321"]

root = Tk()
root.title("KEYS")
root.geometry("250x200")

keys_var = StringVar(value=keys)
listbox = Listbox( listvariable=keys_var)
listbox.pack(expand=1, fill=BOTH)
listbox.yview_scroll(number=1, what="units")
    
root.mainloop() """

""" # подключаем модуль
import pygame

# Создаем окно
window = pygame.display.set_mode((300, 300))
# Озаглавливаем окно
pygame.display.set_caption("Music BOX")

#музыка
pygame.mixer.init()
pygame.mixer.music.load('8-bit_M.mp3')
pygame.mixer.music.play()

sound = pygame.mixer.Sound('8-bit_M.mp3')

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        sound.play()
    elif keys[pygame.K_s]:
        pygame.mixer.pause()
    pygame.display.update()
    pygame.time.delay(40) """
    
    
a = [1, 2, 3, 4]
print(map(str,a))