import copy
define =   [
           ["0",""],
           ["1","1"],
           ["2","11"],
           ["3","111"],
           ["4","1111"],
           ["5","11111"],
           ["6","111111"],
           ["7","1111111"],
           ["8","11111111"],
           ["9","111111111"],
           ["j","1111111111"]
           ]

def cremi(o,sym):
    define = copy.deepcopy(o)
    define[-1] =  [sym,define[-1][1]]
    define.append(["j",define[-1][1]+"1"])
    return define

def define(sym): #base define flatten
    for i in define_:
        if sym==i[0]:
            return i[1]
        if sym==i[1]:
            if i[0]=="j": return "10"
            return i[0]

def addOne(sym): #base add 1 (1 to n, like n=9)
    sym = define(sym)
    sym += "1"
    sym = define(sym)
    return sym

def scanAddOne(sym): #add 1 (any value).
    sym = sym[::-1]
    nsym = ""
    addjump = True
    for i in sym:
        if addjump:
            i = addOne(i)
            if i=="10":
                nsym += "0"
                addjump = True
            else:
                nsym += i
                addjump = False
        else:
            nsym += i
    if addjump:
        nsym += "1"
    nsym = nsym[::-1]
    return nsym

def scanjumpflatten(sym): #flatten: 3 to "111"
    sym = sym[::-1]
    nsym = ""
    base = define("1")
    jump = define("j")
    for i in sym:
        i = define(i)
        value = ""
        for o in i:
            value += base 
        nsym += value
        
        nbase = ""
        for o in jump:
            nbase += base
        base = nbase
    return nsym

def add(sym1,sym2):
    if len(sym1)>=len(sym2):
        max_ = sym1
        min_ = sym2
    else:
        max_ = sym2
        min_ = sym1
    min_ = scanjumpflatten(min_)
    for i in min_:
        max_ = scanAddOne(max_)
    return max_

def subtraction(sym1,sym2): #不支援負數
    sym1 = scanjumpflatten(sym1)
    sym2 = len(scanjumpflatten(sym2))
    sym1 = sym1[sym2:]
    sym3 = "0"
    for ik in sym1:
        sym3 = scanAddOne(sym3)
    return sym3

def mutiply(sym1,sym2):
    sym2 = scanjumpflatten(sym2)
    sym3 = "0"
    for ik in sym2:
        sym3 = add(sym3,sym1)
    return sym3

def mprint():
    i_ = ""
    ie_ = ""
    for i in define("j")[1:]:
        i_ += "1"
        ie_ = ""
        for ie in define("j")[1:]:
            ie_ += "1"
            print("%s × %s = %2s"%(define(ie_),define(i_),mutiply(define(i_),define(ie_))),end="  ")
        print()
    print()

symbols = ["1","2","3","4","5","6","7","8","9","┴","┬","┤","├","┌","┐","└","┘"]
define_ = [["0",""],["j","1"]]
size = ""
for i in symbols:
    size += "1"
    define_ = cremi(define_,i)
    mprint()