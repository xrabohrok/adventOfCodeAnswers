def CountOccurances(set):
    symbols = {}
    for s in set:
        if s in symbols:
            symbols[s] += 1
        else:
            symbols[s] = 1
    sortable = []
    for k in symbols.keys():
        sortable.append((k, symbols[k]))
    preSort = sorted(sortable, key= lambda y: y[0], reverse=False)
    sort = sorted(preSort, key=lambda x: x[1], reverse=True)
    return sort

def isLegitRoom(command):
    #print command
    frequency = CountOccurances(command[0])
    checksum = ""
    i = 0
    while (len(checksum) < 5):
        checksum += frequency[i][0]
        i += 1
    if checksum == command[1]:
        return command[2]
    else:
        return 0

def formatCommand(inputString):
    parts = inputString.split("[")
    a = filter(lambda a: a != None and a != '' and a not in "[]-\n" and not a.isdigit(), parts[0])
    b = filter(lambda a: a != None and a != '' and a not in "[]-\n", parts[1])
    c = filter(lambda a: a.isdigit(), parts[0])
    return (a,b,c)

def processUserInput(raw):
    f = open(raw, 'r')
    rawCommands = []
    for l in f:
        rawCommands.append(l)
    return rawCommands

raw = raw_input("What file do we need to open\n")
commandStrings = processUserInput(raw)

roomSum = 0
for cs in commandStrings:
    formattedCommand = formatCommand(cs)
    roomId = isLegitRoom(formattedCommand)
    #print "RoomId:{}".format(roomId)
    roomSum += int(roomId)

print "The sum of legit room ID's is {}".format(roomSum)
