cardinals = ["north", "east", "south", "west"]
facing = 0
dist = [0,0]


def goDirection(direction, steps):
    global dist
    xd = 0
    yd = 0
    if direction == "north":
        yd = steps
    elif direction == "south":
        yd = -steps
    elif direction == "east":
        xd = steps
    elif direction == "west":
        xd = -steps

    dist[0] += xd
    dist[1] += yd

def turnLeft(steps):
    global facing, cardinals
    facing -= 1
    if facing < 0:
        facing = 3
    goDirection(cardinals[facing], steps)

def turnRight(steps):
    global facing, cardinals
    facing += 1
    if facing > 3:
        facing = 0
    goDirection(cardinals[facing], steps)

def runMap(commands):
    for command in commands:
        if command[0].upper() == 'R' :
            turnRight(int(command[1:]))
        elif command[0].upper() == 'L':
            turnLeft(int(command[1:]))
        else:
            print "ERROR: something is wrong with command: " + command

    return abs(dist[0]) + abs(dist[1])

raw = raw_input("Enter the directions in the form of <turn><steps>*space*|<enter> (R1 L3)\n")
s="".join(i for i in raw if (i.isdigit() or i in " rRlL"))
rawCommands = s.split(" ")
commands = filter(lambda a: a != None and a != '' and a != ',', rawCommands)

distance = runMap(commands)
print "The shortest path is {}, going sideways {}, and vertically {}".format(distance, dist[0], dist[1])
