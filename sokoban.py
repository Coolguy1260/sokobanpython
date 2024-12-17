import curses
# command line sokoban game for fun and profit :)
# 0 = open, 1 = wall, 2 = player start, 3 = box start, 4 = goal
level1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,2,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
level2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,2,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
    [0,1,0,0,3,0,0,1,0,0,0,1,0,0,0,1,0,0,0,4,1,0],
    [0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
level3 = [
    [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,1,2,0,3,0,0,0,0,1,0,0,0,0,0,0,0,0,0,4,1,0],
    [0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
level4 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,2,1,0,1,0,1,0,1,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,1,3,1,0,1,0,1,0,0,4,1,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
levelsdatabase = [level1,level2,level3,level4]
screen = curses.initscr()
def drawGame(level, playerpos, boxpos):
    screen.erase()
    for i in range(len(level)):
        for g in range(len(level[i])):
            if level[i][g] == 0:
                screen.addstr(i,g,"-",curses.color_pair(1))
            elif level[i][g] == 1:
                screen.addstr(i,g,"#",curses.color_pair(0))
            elif level[i][g] == 2:
                screen.addstr(i,g,"P",curses.color_pair(2))
                playerpos = [g,i]
            elif level[i][g] == 3:
                screen.addstr(i,g,'☐',curses.color_pair(3))
                boxpos = [g,i]
            elif level[i][g] == 4:
                screen.addstr(i,g,'G',curses.color_pair(4))
        screen.refresh()
    return playerpos, boxpos
def main():
    playerpos = [0,0]
    boxpos = [0,0]
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_GREEN,curses.COLOR_BLACK)
    screen.keypad(True)
    for currentlevel in levelsdatabase:
        playerpos, boxpos = drawGame(currentlevel, playerpos, boxpos)
        victory = False
        while not victory:
            key = screen.getkey()
            playerTarget = [0,0]
            modifier = [0,0]
            if(key == "KEY_RIGHT"):
                modifier = [1,0]
            elif(key == "KEY_LEFT"):
                modifier = [-1,0]
            elif(key == "KEY_UP"):
                modifier = [0,-1]
            elif(key == "KEY_DOWN"):
                modifier = [0,1]
            playerTarget = [playerpos[0] + modifier[0], playerpos[1] + modifier[1]]
            objectAtLoc = currentlevel[playerTarget[1]][playerTarget[0]]
            if objectAtLoc == 0:
                currentlevel[playerTarget[1]][playerTarget[0]] = 2
                currentlevel[playerpos[1]][playerpos[0]] = 0
                playerpos, boxpos = drawGame(currentlevel, playerpos, boxpos)
            elif objectAtLoc == 3:
                boxTarget = [playerTarget[0] + modifier[0], playerTarget[1] + modifier[1]]
                objectAtLoc = currentlevel[boxTarget[1]][boxTarget[0]]
                if objectAtLoc == 0:
                    currentlevel[playerTarget[1]][playerTarget[0]] = 2
                    currentlevel[playerpos[1]][playerpos[0]] = 0
                    currentlevel[boxTarget[1]][boxTarget[0]] = 3
                    playerpos, boxpos = drawGame(currentlevel, playerpos, boxpos)
                elif objectAtLoc == 4:
                    victory = True
            # other cases are walls
        screen.clear()
        screen.addstr("You Win! Press any key to move on to the next level!", curses.color_pair(4))
        screen.refresh()
        screen.getstr()
main()