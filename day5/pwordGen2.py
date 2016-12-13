import hashlib

def FindHasPW(seed, pwSize):
    i = 0
    quintZero = 0
    pw = []
    f = open("output.txt","w")
    while len(pw) < pwSize:
        pw.append("-")
    while "-" in pw:
        h = hashlib.md5(str(seed)+str(i))
        hashed = h.hexdigest()
        print "{} : {} | {} // {}".format(i,hashed, "".join(pw), quintZero)
        if hashed[0:5] == "00000":
            quintZero += 1
            f.write(hashed)
            if(hashed[5].isdigit() and int(hashed[5])>= 0 and int(hashed[5]) < pwSize):
                position = int(hashed[5])
                letter = hashed[6]
                if(pw[position] == "-"):
                    pw[position] = letter
                    print "+++++++++++++++++++++++"
                    print "LETTER FOUND: {}".format(pw)
        i += 1
    final = "".join(pw)
    return (final,i)

size = 8
raw = raw_input("What pw are we decoding\n")

result = FindHasPW(raw, size)
print ("The PW is: {}\nFound over {} tries".format(result[0], result[1]))
