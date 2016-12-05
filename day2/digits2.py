
def executeMove(numpad,pos, deltaX, deltaY):
    if  pos[0] + deltaX < 5 and pos[0] + deltaX >=0 and numpad[pos[0]+deltaX][pos[1]] != "x":
        pos[0] += deltaX

    if pos[1] + deltaY < 5 and pos[1] + deltaY >=0 and numpad[pos[0]][pos[1]+deltaY] != "x":
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
            #print "char: {}, pos: {}, char: {}".format(c, pos, numPad[pos[0]][pos[1]])
            if c == "U":
                executeMove(numPad,pos,0,1)
            elif c == "D":
                executeMove(numPad,pos,0,-1)
            elif c == "L":
                executeMove(numPad,pos,-1,0)
            elif c == "R":
                executeMove(numPad,pos,1,0)
        digits.append( numPad[pos[0]][pos[1]])
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
numpad.append(["x","x","5","x","x"])
numpad.append(["x","A","6","2","x"])
numpad.append(["D","B","7","3","1"])
numpad.append(["x","C","8","4","x"])
numpad.append(["x","x","9","x","x"])

pos = [2,2]
digits = ""


raw = raw_input("What file do we need to open\n")
commands = processUserInput(raw)

digits = processCommands(numpad, pos, commands)
final = ""
for c in digits:
    final += "{}".format(c)
print("Code so far: {}".format(final))
