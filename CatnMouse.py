import random
import msvcrt
"""             *     *
        .--      *  *  *
  -...  .-        ** *
  -.--  ...      * **       ### #% %
        ---      * *       #%% %# #%##
        -.       T^^T   %% %####% %#%% %#%%
                 |  | %%#% %% #% #%%   %#
    _____________|__|__   %## %# #%##
   /___________________\   ### %%# #
   T^^^^^^^^^^^^^^^^^^^T   \ V/  V/
   |  ___         ___  |    \  | /
   | |_|_|       |_|_| |    ||  T
   | |_|_| |TTT| |_|_| |    | | |
   |       |||o|       |    |  ||
   |       |||||       |    ||  |
   ^*** **^ ^ *^*^*^ *^*^*^ *^*^*^
      **^* ^^^ *^*   ^* ^^^ *^^
       ** *^^^^* *^** *^**   
        *** ^ *^ ^*^^
         **** * *^* *
"""


def mg(n):
    if n == 0:
        return "░"
    elif n == 1:
        return " "
    elif n == 2:
        return "Δ"
    elif n == 3:
        return "C"
    else:
        return "!"


def checker(num):
    if num == 0:
        note = "You encountered a wall."
        t = [False, False, False]  # [movable, trap, cheese]
    elif num == 1:
        note = "You moved 1 space"
        t = [True, False, False]
    elif num == 2:
        note = "You got a cheese!"
        t = [True, False, True]
    elif num == 3:
        note = "You got caught!"
        t = [False, True, False]
    else:
        note = "Invalid"
        t = [False, False, False]
    return note, t


def graphics(maze, position, points):
    graph = list()
    for a in range(-2, 3):
        temp = list()
        for b in range(-2, 3):
            if a == 0 and b == 0:
                g = "M"
            elif a in [-2,2] and b in [-2,2]:
                g = "X"
            else:
                g = mg(maze[position[0] + a][position[1] + b])
            temp.append(g)
        graph.append(temp[:])
    BORDER = ["╝", "╚", "╗", "╔"]
    Ca = ["╔", "╗", "╚", "╝"]
    print(" ╔═══╗")
    Bb = 0
    Cb = 0
    for c in range(0, 5):
        if c in [0,4]:
            print(Ca[Cb], end='')
            Cb += 1
        else:
            print("║", end='')
        for d in range(0, 5):
            if graph[c][d] == "X":
                print(BORDER[Bb], end='')
                Bb += 1
            else:
                print(graph[c][d], end='')
        if c in [0,4]:
            print(Ca[Cb], "\n", end='')
            Cb += 1
        else:
            print("║\n", end='')
    print(" ╚═══╝\nPoints: {}".format(points))


def cheese(n):
    global maze
    while n < 3:
        x = random.randint(0, 23)
        y = random.randint(0, 23)
        if maze[x][y] == 1:
            maze[x][y] = 2
            n += 1
    return n


def catplace(n, points, cat):
    global maze
    while n < points / 5:
        x = random.randint(0, 23)
        y = random.randint(0, 23)
        if maze[y][x] == 1:
            maze[y][x] = 3
            z = [y, x]
            cat.append(z)
            n += 1
    return n, cat


def catmove(cat, maze, position):
    caught = False
    for n in range(0, len(cat)):
        m = 0
        move = False
        while move is False and m < 5:
            m += 1
            x = random.randint(0, 3)
            if x == 0:
                v, t = checker(maze[cat[n][0]][cat[n][1]-1])
                if t[0] is True:
                    maze[cat[n][0]][cat[n][1]] = 1
                    maze[cat[n][0]][cat[n][1]-1] = 3
                    cat[n][1] -= 1
                    move = True
            elif x == 1:
                v, t = checker(maze[cat[n][0]-1][cat[n][1]])
                if t[0] is True:
                    maze[cat[n][0]][cat[n][1]] = 1
                    maze[cat[n][0]-1][cat[n][1]] = 3
                    cat[n][0] -= 1
                    move = True
            elif x == 2:
                v, t = checker(maze[cat[n][0]][cat[n][1]+1])
                if t[0] is True:
                    maze[cat[n][0]][cat[n][1]] = 1
                    maze[cat[n][0]][cat[n][1]+1] = 3
                    cat[n][1] += 1
                    move = True
            else:
                v, t = checker(maze[cat[n][0]+1][cat[n][1]])
                if t[0] is True:
                    maze[cat[n][0]][cat[n][1]] = 1
                    maze[cat[n][0]+1][cat[n][1]] = 3
                    cat[n][0] += 1
                    move = True
        if cat[n][0] == position[0] and cat[n][1] == position[1]:
            caught = True
    return cat, caught


maze = [  # 20(+4 padding)x20(+4 padding) maze
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 00
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 01
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 02
    [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],  # 03
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # 04
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],  # 05
    [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],  # 06
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # 07
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],  # 08
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],  # 09
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],  # 10
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],  # 11
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],  # 12
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],  # 13
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 14
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],  # 15
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 16
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],  # 17
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],  # 18
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],  # 19
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],  # 20
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],  # 21
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 22
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 23
#    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23

'''
000000000011111111112222
012345678901234567890123
XXXXXXXXXXXXXXXXXXXXXXXX 00
XXXXXXXXXXXXXXXXXXXXXXXX 01
XX X XX X X   X XXXXXXXX 02
XX X    X   X X X     XX 03
XX   X XX XXX X X XXX XX 04
XXXXXX    X X   X     XX 05
XX    X X X   X    XX XX 06
XX XX   X X XXX XXXXX XX 07
XX   X X    X   X   X XX 08
XX XXX   XXXX XXX X X XX 09
XX X   X          X   XX 10
XX   XXX X XXXX X X XXXX 11
XX X   X X   X  X X X XX 12
XX  X XXXX X X XX     XX 13
XX X  X    X   XXXXX XXX 14
XX   XXX XXX X X     XXX 15
XXX XX   XX  X X XXXXXXX 16
XXX    XX X XXXX    XXXX 17
XX  XXXXX   XXX XXX XXXX 18
XX XXX   XX       X XXXX 19
XX   X X  XXX XXX X   XX 20
XXXX   XX     XX    XXXX 21
XXXXXXXXXXXXXXXXXXXXXXXX 22
XXXXXXXXXXXXXXXXXXXXXXXX 23
'''
GAME = True
while GAME is True:
    input("Get as many cheese as possible, and avoid the cats!")
    caught = False
    points = 0
    t = [False, False, False]
    n = 0
    c = 0
    mouse = [2, 2]  # [Y, X]
    cat = list()
    ROUND = True
    while ROUND is True:
        m = 0
        message = ""
        if n < 3:
            n = cheese(n)
        if c < 10:
            c, cat = catplace(c, points, cat)
        # print(mouse)
        # print(cat)
        N = mouse[0] - 1
        S = mouse[0] + 1
        W = mouse[1] - 1
        E = mouse[1] + 1
        graphics(maze, mouse, points)
        print("\n"*5, "Which way?(WASD)")
        usrin = msvcrt.getch().decode("utf-8")
        # print(usrin)
        if usrin == 'w':
            message, t = checker(maze[N][mouse[1]])
            if t[0] is True:
                mouse[0] -= 1
        elif usrin == 's':
            message, t = checker(maze[S][mouse[1]])
            if t[0] is True:
                mouse[0] += 1
        elif usrin == 'a':
            message, t = checker(maze[mouse[0]][W])
            if t[0] is True:
                mouse[1] -= 1
        elif usrin == 'd':
            message, t = checker(maze[mouse[0]][E])
            if t[0] is True:
                mouse[1] += 1
        else:
            message = "Invalid input"
        if points > 0:
            while m < 2:
                cat, caught = catmove(cat, maze, mouse)
                m += 1
        if t[1] is True or caught is True:
            print("You got caught!")
            ROUND = False
            break
        if t[2] is True:
            n -= 1
            maze[mouse[0]][mouse[1]] = 1
            points += 1
        print(message)


"""Changelog
Planned:
0.8: Blind spots
0.7: Cat has BRAINS?!?!
0.6: Leap!
0.5: Map power!
0.4: Radar toggle!
Current:
0.3.7: Made graphic more distinguishable from text
Past:
0.3.6: Increase the interval where a cat would spawn
0.3.5: Less processing needed now
0.3.4: Fixed bug where cat invisible
0.3.3: Fixed bug where cat would always catch mouse
0.3.2: Controls improved, let the enter key rest now.
0.3.1: Cat moves in random directions
0.3: Cat? CAT?! CAAAAT!!!
0.2.1: Cheese gives points
0.2: Working model with cheese
0.1.2: Cheese.
0.1.1: Changed graphics
0.1: First working model
0.0.3: Added movement
0.0.2: Graphic generator added
0.0.1: Map added
0.0: Project started
"""
