import random
from tkinter import *
mines = []
board = [[0 for i in range(8)] for j in range(8)]
r = Tk()
fake_board = [[0 for i in range(8)] for j in range(8)]

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

def play():
    global mines,board
    x = True
    while x:
        x_in,y_in = input('Enter coordinates : ').split()
        x_in = int(x_in)
        y_in = int(y_in)
        if board[x_in][y_in] == 1:
            x = False
            print('GameOver!!!')
        else:
            board[x_in][y_in] = 9
            for i in board:
                print(i)

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
    #for i in board:
        #print(i)

AddMines()
Assign()

def disp(k):
    Bts[k[0]*8+k[1]].config(text=board[k[0]][k[1]])

Bts=list()
for i in range(8):
    f = Frame(r)
    f.pack()
    for j in range(8):
        b = Button(f,height='2',width='4',text=' ',font=('Arial',15),command=lambda k=[i,j]:disp(k))
        Bts.append(b)
        b.pack(side='left')

print(mines)
r.mainloop()