import random
from tkinter import *
mines = []
board = [[0 for i in range(8)] for j in range(8)]
pressed = []
coordinates = [[a,b] for a in range(8) for b in range(8)]
r = Tk()
game_start = 0
sec = 0
min = 0
mst = 0
lbt = Label(r,text='00:00',font=('Arial',25),bg='white',background='#FF8000')
lbt.pack()
unflag = []

def game_win():
    global mines,board,pressed,coordinates,game_start,min,sec,unflag
    unflag = []
    mines = []
    board = [[0 for i in range(8)] for j in range(8)]
    pressed = []
    coordinates = [[a,b] for a in range(8) for b in range(8)]
    game_start = 0
    for i in Bts:
        i.config(text=' ',relief=RAISED,background='#D1EEEE')
    l = Tk()
    l.geometry('350x150')
    l.configure(background='#FF8000')
    ss=f'{sec}' if sec>9 else f'0{sec}'
    ms=f'{min}' if min>9 else f'{min}'
    bbl = Label(l,text='YOU WIN!!!\n YOUR TIME IS\n'+str(ms)+'mins and '+str(ss)+'secs',font=('Arial',25),background='#FF8000',justify='center')
    bbl.pack()
    min = 0
    sec = 0

def game_res():
    global mines,board,pressed,coordinates,game_start,min,sec,unflag
    mines = []
    unflag = []
    board = [[0 for i in range(8)] for j in range(8)]
    pressed = []
    coordinates = [[a,b] for a in range(8) for b in range(8)]
    game_start = 0
    for i in Bts:
        i.config(text=' ',relief=RAISED,background='#D1EEEE')
    k = Tk()
    k.geometry('250x100')
    k.configure(background='#FF8000')
    bbk = Label(k,text='YOU LOSE!!!\n TRY AGAIN',font=('Arial',25),background='#FF8000',justify='center')
    bbk.pack()
    min = 0
    sec = 0

def AddMines():
    global mines
    while True:
        x = random.choice([0,1,2,3,4,5,6,7])
        y = random.choice([0,1,2,3,4,5,6,7])
        if ([x,y] not in mines) and ([x,y] not in pressed):
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
    for i in board:
        print(i)

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
        if board[i[0]][i[1]] == 0:
            Bts[i[0]*8+i[1]].config(text=' ',relief=SUNKEN,bg='#CDC8B1')
        else:
            Bts[i[0]*8+i[1]].config(text=board[i[0]][i[1]],relief=SUNKEN,bg='#CDC8B1')
        pressed.append(i)
        unflag.append(i)

def disp(k):
    global game_start,mst,unflag
    
    def inner1():
        global sec,min,mst
        sec+=1
        if sec == 60:
            sec = 0
            min+=1
        ss=f'{sec}' if sec>9 else f'0{sec}'
        ms=f'{min}' if min>9 else f'{min}'
        lbt.config(text=ms+':'+ss)
        if mst == 1:
            lbt.config(text='00:00')
        else:
            global ko
            ko=lbt.after(1000,inner1)
    
    if game_start == 0:
        mst = 0
        inner1()

    if game_start != 0:
        x_in = k[0]
        y_in = k[1]
        if k not in pressed:
            if board[x_in][y_in] == '@':
                mst = 1
                print('GameOver!!!')
                Bts[x_in*8+y_in].config(text=board[x_in][y_in],relief=SUNKEN,bg='#CDC8B1',background = 'red')
                pressed.append(k)
                unflag = []
                game_res()
            elif board[x_in][y_in] != 0:
                Bts[x_in*8+y_in].config(text=board[x_in][y_in],relief=SUNKEN,bg='#CDC8B1')
                pressed.append(k)
                unflag.append(k)
                #checking for game completion
                if len(unflag) == 54:
                    mst = 1
                    game_win()
            else:
                group(k)
                #checking for game completion
                if len(unflag) == 54:
                    mst = 1
                    game_win()

    elif game_start == 0:
        game_start = 1
        unflag = []
        pressed.append(k)
        AddMines()
        Assign()
        x_in = k[0]
        y_in = k[1]
        if board[x_in][y_in] != 0:
            Bts[x_in*8+y_in].config(text=board[x_in][y_in],relief=SUNKEN,bg='#CDC8B1')
            unflag.append(k)
        else:
            Bts[x_in*8+y_in].config(text=' ',relief=SUNKEN,bg='#CDC8B1')
            group(k)

def right_click(eff,p):
    cd = Bts.index(p)
    cd_x = cd//8
    cd_y = cd%8    
    if [cd_x,cd_y] not in pressed:
        p.config(background='red',relief=SUNKEN)
        pressed.append([cd_x,cd_y])
    else:
        p.config(background='#D1EEEE',relief=RAISED)
        pressed.remove([cd_x,cd_y])

Bts=list()
for i in range(8):
    f = Frame(r)
    f.pack()
    for j in range(8):
        b = Button(f,height='2',width='4',text=' ',font=('Arial',15),
                   command=lambda k=[i,j]:disp(k),relief=RAISED,background='#D1EEEE')
        Bts.append(b)
        b.pack(side='left')

for i in Bts:
    i.bind("<Button-2>", lambda eff,p=i: right_click(eff,p))
    i.bind("<Button-3>", lambda eff,p=i: right_click(eff,p))

r.mainloop()