import tkinter as tk
from tkinter import messagebox

import data_transfer
import check_ship_position

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
    global state, c, button, num
    state = 1
    button['state'] = tk.DISABLED
    tk.messagebox.showinfo("SeaBattle: подбор игрока", "Привет. Скоро мы подберем тебе соперника, после чего ты"
                                                       "сможешь приступить к расстановке кораблей. Когда соперник"
                                                       "будет подобран, мы оповестим тебя.")
    data_transfer.start()

    button.destroy()
    rules.destroy()
    button = tk.Button(data_transfer.window, text="Продолжить", width=15, height=3, command=state2)
    button.place(x=172.5, y=450)

    data_transfer.window.geometry("475x550")
    c = tk.Canvas(data_transfer.window, width=SQUARE_SIZE * 10, height=SQUARE_SIZE * 10, bg="white")
    c.place(x=30, y=30)

    for i in range(10):
        for j in range(10):
            my_field.append(c.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE,
                                             j * SQUARE_SIZE + SQUARE_SIZE,
                                             i * SQUARE_SIZE + SQUARE_SIZE, fill="#0070A1"))
    tk.messagebox.showinfo("SeaBattle: расстановка кораблей", "    Привет снова. Надеюсь, ты ждал не очень долго и без "
                                                           "происшествий :)\n\n    Клетки можно заполнять частями "
                                                           "корабля, нажимая на них левой клавишей мыши. Удалять "
                                                           "часть - правой. Корабли представляют собой строку или "
                                                           "столбец, размером Nx1 и 1xN соответственно. Какие "
                                                           "корабли могут быть по размерам и количеству:\n\n    1. "
                                                           "Одноклеточные корабли (1x1), 4 корабля,"
                                                           "\n    2. Двуклеточные корабли (2x1), 3 корабля,"
                                                           "\n    3. Трёхклеточные корабли (3x1), 2 корабля,"
                                                           "\n    4. Четырёхклеточный корабль (4x1), 1 корабль.\n\n"
                                                           "    Корабли не должны пересекаться и(или) всячески "
                                                           "изгибаться. Всё абсолютно как в классическом морском бое. "
                                                           "Теперь ты можешь начинать создавать флот :) Когда "
                                                           "закончишь - нажимай на кнопку \"Продолжить\"")

    c.bind("<Button-1>", l_click)
    c.bind("<Button-3>", r_click)


def state2():
    if not check_ship_position.check_field(play_map):
        messagebox.showwarning("SeaBattle: расстановка кораблей", "Привет. Построенная карта кораблей является "
                                                                  "неправильной, так как какое-то из правил не было "
                                                                  "соблюдено:\n\n    1. Размеры кораблей не "
                                                                  "соблюдены\n "
                                                                  "  2. Количество кораблей отлично от 10\n    3. "
                                                                  "Корабли прикосаются друг к другу\n    4. Корабли "
                                                                  "неверной формы\n\nНапоминаю размеры и количество "
                                                                  "кораблей:\n\n    1. "
                                                                  "Одноклеточные корабли (1x1), 4 корабля,"
                                                                  "\n    2. Двуклеточные корабли (2x1), 3 корабля,"
                                                                  "\n    3. Трёхклеточные корабли (3x1), 2 корабля,"
                                                                  "\n    4. Четырёхклеточный корабль (4x1), "
                                                                  "1 корабль.\n\nПерепроверь и исправь своё поле, "
                                                                  "а затем нажми сюда ещё раз.")
        return

    global button, state, c, c2, lb_ban, lb_nab, lb, num
    state = 2
    button['state'] = tk.DISABLED
    messagebox.showinfo("SeaBattle: ожидание игрока", "И ещё раз привет! Ожидай, пока твой соперник не завершит "
                                                      "расстановку своих кораблей и нажмёт на эту же кнопку. После "
                                                      "этого сразу же начнётся игра.")


def l_click(event):
    idx = c.find_withtag(tk.CURRENT)[0]
    if state == 1:
        play_map[idx - 1] = '#'
        c.itemconfig(tk.CURRENT, fill="#12CE10")
    c.update()


def r_click(event):
    idx = c.find_withtag(tk.CURRENT)[0]
    if state == 1:
        play_map[idx - 1] = '*'
        c.itemconfig(tk.CURRENT, fill="#0070A0")
    c.update()


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
