cardinals = ["north", "east", "south", "west"]
facing = 0
dist = [0,0]
logger = []
dest = None


def goDirection(direction, steps):
    global dist, logger, dest
    xd = 0
    yd = 0
    if direction == "north":
        yd = 1
    elif direction == "south":
        yd = -1
    elif direction == "east":
        xd = 1
    elif direction == "west":
        xd = -1

    for i in range(0,steps) :
        dist[0] += xd
        dist[1] += yd
        here = "{},{}".format(dist[0],dist[1])
        print here
        if haveIBeenHere(here):
            if dest == None:
                dest = [dist[0],dist[1]]


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
    global dist
    for command in commands:
        if command[0].upper() == 'R' :
            if(turnRight(int(command[1:]))):
                print "==>{}".format(abs(dist[0]) + abs(dist[1]))
        elif command[0].upper() == 'L':
            if(turnLeft(int(command[1:]))):
                print "==>{}".format(abs(dist[0]) + abs(dist[1]))
        else:
            print "ERROR: something is wrong with command: " + command

    return abs(dist[0]) + abs(dist[1])

def haveIBeenHere(here):
    global logger
    for log in logger:
        if log == here:
            return True

    logger.append(here)
    return False

raw = raw_input("Enter the directions in the form of <turn><steps>*space*|<enter> (R1 L3)\n")
s="".join(i for i in raw if (i.isdigit() or i in " rRlL"))
rawCommands = s.split(" ")
commands = filter(lambda a: a != None and a != '' and a != ',', rawCommands)

distance = runMap(commands)
print "The shortest path is {}, going sideways {}, and vertically {}".format(distance, dist[0], dist[1])

print dest
print "==>{}".format(abs(dest[0]) + abs(dest[1]))
