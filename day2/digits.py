
def executeMove(pos, deltaX, deltaY):
    if deltaX > 0 and pos[0] + deltaX < 3:
        pos[0] += deltaX
    elif deltaX < 0 and pos[0] + deltaX >= 0:
        pos[0] += deltaX

    if deltaY > 0 and pos[1] + deltaY < 3:
        pos[1] += deltaY
    elif deltaY < 0 and pos[1] + deltaY >= 0:
        pos[1] += deltaY
    return pos

def processCommands(numPad, pos, commands):
    digits = []
    lineNum = 0
    for l in commands:
        lineNum += 1
        #print "line {}".format(lineNum)
        for d in l:
            c = d.upper()
            #print "char: {}, pos: {}".format(c, pos)
            if c == "U":
                executeMove(pos,0,1)
            elif c == "D":
                executeMove(pos,0,-1)
            elif c == "L":
                executeMove(pos,-1,0)
            elif c == "R":
                executeMove(pos,1,0)
        digits.append( numpad[pos[0]][pos[1]])
    return digits

def processUserInput(raw):
    f = open(raw, 'r')
    rawCommands = []
    for l in f:
        rawCommands.append(l)

    commands = []
    for a in rawCommands:
        commands.append( filter(lambda a: a != None and a != '' and a != ',', a))
    print ("There are {} commands".format(len(commands)))
    #for c in commands:
        #print("====================")
        #print (c)
    return commands


numpad = []
numpad.append([7,4,1])
numpad.append([8,5,2])
numpad.append([9,6,3])

pos = [1,1]
digits = ""


raw = raw_input("What file do we need to open\n")
commands = processUserInput(raw)

digits = processCommands(numpad, pos, commands)
final = ""
for c in digits:
    final += "{}".format(c)
print("Code so far: {}".format(final))
