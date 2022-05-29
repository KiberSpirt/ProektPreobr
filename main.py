import tkinter as tk
from tkinter import messagebox

import data_transfer

SQUARE_SIZE = 40
play_map = ['*'] * 100
enemy_map = []
state = num = 0

data_transfer.window.geometry("225x175")
data_transfer.window.title("SeaBattle")
c = tk.Canvas(data_transfer.window)
c2 = tk.Canvas(data_transfer.window)
lb = tk.Label(data_transfer.window)
lb_ban = tk.Label(data_transfer.window)
lb_nab = tk.Label(data_transfer.window)
my_field = enemy_field = []
winner = 2
button1 = button2 = tk.Button(data_transfer.window)
my_ship_pos = my_ship_h = my_ships = enemy_ship_pos = enemy_ship_h = enemy_ships = []
my_ships_h = en_health = 10


def state1():
    pass


button = tk.Button(data_transfer.window, text="Начать игру", width=15, height=3, command=state1)
button.place(x=50, y=30)
rules = tk.Button(data_transfer.window, text="Правила игры", width=15, height=3,
               command=lambda: messagebox.showinfo("SeaBattle: правила игры", "Привет! Ты решил почитать правила игры. "
                                                                              "Когда игра начнётся, справа ты сможешь "
                                                                              "увидеть поле соперника, слева своё. "
                                                                              "Естественно, с самого начала игры ты "
                                                                              "не сможешь увидеть корабли соперника, "
                                                                              "так же как и "
                                                                              "сопреник твои. Чтобы выстрелить в поле "
                                                                              "соперника, нажми левой клавишей мыши "
                                                                              "на то поле, на "
                                                                              "которое желаешь. Ествественно, все "
                                                                              "выстрелы необходимо совершать по "
                                                                              "очереди. После выстрела по полю с "
                                                                              "кораблём, оно станет тёмно-зелёным. "
                                                                              "Если там ничего не было, оно станет "
                                                                              "тёмно-синим. А если мы убили корабль "
                                                                              "противника, весь корабль станет "
                                                                              "красным. Тоже самое и на твоём "
                                                                              "поле. В случае, если игрок попадает на "
                                                                              "поле с кораблём, ход сопернику не "
                                                                              "передаётся, а он ходит ещё раз.\n\nЭто "
                                                                              "всё. Удачи :)"))
rules.place(x=50, y=90)

data_transfer.window.mainloop()
