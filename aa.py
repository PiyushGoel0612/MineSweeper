import random
from tkinter import *
mines = []
board = [[0 for i in range(8)] for j in range(8)]
pressed = []
coordinates = [[a,b] for a in range(8) for b in range(8)]
r = Tk()

def AddMines():
    global mines
    while True:
        x = random.choice([0,1,2,3,4,5,6,7])
        y = random.choice([0,1,2,3,4,5,6,7])
        if [x,y] not in mines:
            mines.append([x,y])
        if len(mines) == 10:
            break
    #print(mines)
    for i in mines:
        board[i[0]][i[1]] = "@"

def Assign():
    global mines,board
    tbd = []
    coordinates = [[a,b] for a in range(8) for b in range(8)]
    for i in coordinates:
        if i not in mines:
            tbd.append(i)
    for i in tbd:
        count_mines = 0
        x0 = i[0]
        y0 = i[1]
        check = [[x0+1,y0],[x0+1,y0+1],[x0+1,y0-1],
                [x0-1,y0],[x0-1,y0+1],[x0-1,y0-1],
                [x0,y0+1],[x0,y0-1]]
        for i in check:
            if i in mines:
                count_mines+=1
        board[x0][y0] = count_mines

AddMines()
Assign()

def group(k):
    global board,mines,pressed,coordinates
    grp = []
    checked = []
    def inner(c):
        nonlocal grp
        mini_grp = list()
        mini_grp.append(c)
        x0 = c[0]
        y0 = c[1]
        check = [[x0+1,y0],[x0+1,y0+1],[x0+1,y0-1],
                [x0-1,y0],[x0-1,y0+1],[x0-1,y0-1],
                [x0,y0+1],[x0,y0-1]]
        for i in check:
            if i not in coordinates:
                check.remove(i)
        mini_grp.extend(check)
        grp.extend(mini_grp)
        checked.append(c)
        for i in check:
            if (i in coordinates) and (i not in checked):
                if board[i[0]][i[1]] == 0:
                    inner(i)
    inner(k)
    ind = 0
    while ind<len(grp):
        if grp.count(grp[ind]) > 1:
            grp.remove(grp[ind])
        else:
            ind+=1
    ind = 0
    while ind<len(grp):
        if grp[ind] not in coordinates:
            grp.remove(grp[ind])
        else:
            ind+=1
    ind = 0
    while ind<len(grp):
        if grp[ind] in pressed:
            grp.remove(grp[ind])
        else:
            ind+=1
    #print(grp)
    for i in grp:
        Bts[i[0]*8+i[1]].config(text=board[i[0]][i[1]],relief=SUNKEN)
        pressed.append(i)

def disp(k):
    x_in = k[0]
    y_in = k[1]
    if k not in pressed:
        if board[x_in][y_in] == '@':
            print('GameOver!!!')
            Bts[x_in*8+y_in].config(text=board[x_in][y_in],relief=SUNKEN)
            pressed.append(k)
        elif board[x_in][y_in] != 0:
            Bts[x_in*8+y_in].config(text=board[x_in][y_in],relief=SUNKEN)
            pressed.append(k)
        else:
            group(k)

Bts=list()
for i in range(8):
    f = Frame(r)
    f.pack()
    for j in range(8):
        b = Button(f,height='2',width='4',text=' ',font=('Arial',15),command=lambda k=[i,j]:disp(k),relief=RAISED)
        Bts.append(b)
        b.pack(side='left')

print(mines)
for i in board:
    print(i)
r.mainloop()