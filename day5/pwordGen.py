import hashlib

def FindHasPW(seed, pwSize):
    i = 0
    pw = ""
    while len(pw) < pwSize:
        h = hashlib.md5(str(seed)+str(i))
        hashed = h.hexdigest()
        print "{} : {} | {}".format(i,hashed, pw)
        if hashed[0:5] == "00000":
            pw += hashed[5]
            print "+++++++++++++++++++++++"
            print "LETTER FOUND: {}".format(pw)
        i += 1
    return (pw,i)

size = 8
raw = raw_input("What pw are we decoding\n")

result = FindHasPW(raw, size)
print ("The PW is: {}\nFound over {} tries".format(result[0], result[1]))
