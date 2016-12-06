

def processUserInput(raw):
    f = open(raw, 'r')
    rawCommands = []
    for l in f:
        rawCommands.append(l)

    commands = []
    #I could probably make this more condensed as an array, but this is easier
    #to follow
    slotA = []
    slotB = []
    slotC = []
    for a in rawCommands:
        s="".join(i for i in a if i.isdigit() or i == " ")
        singularCommands = s.split(" ")
        temp = filter(lambda a: a != None and a != '' and a != ',', singularCommands)
        slotA.append(temp[0])
        slotB.append(temp[1])
        slotC.append(temp[2])
        if(len(slotA) >= 3):
            commands.append([])
            for x in slotA:
                commands[-1].append(int(x))
            slotA = []

            commands.append([])
            for x in slotB:
                commands[-1].append(int(x))
            slotB = []

            commands.append([])
            for x in slotC:
                commands[-1].append(int(x))
            slotC = []

    return commands

def checkTrigLegitimacy(rawTris):
    legit = 0
    illegit = 0
    total = 0
    for tri in rawTris:
        total += 1
        #print "{} | {} | {}".format(tri[0], tri[1], tri[2])
        if tri[0] + tri[1] <= tri[2] :
            illegit += 1
            continue
        elif tri[0] + tri[2] <= tri[1] :
            illegit += 1
            continue
        elif tri[2] + tri[1] <= tri[0] :
            illegit += 1
            continue
        else:
            legit += 1
            #print "====Legit"
    return [legit, illegit, total]

raw = raw_input("What file do we need to open\n")
commands = processUserInput(raw)

result = checkTrigLegitimacy(commands)

print("In the set of {} edgelengths, there are {}legit triangles and\n {} illegitimate triangles".format(result[2], result[0], result[1]))
