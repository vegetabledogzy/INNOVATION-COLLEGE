def increment(n):
    return n+1
def square(n):
    return n**2
def apply(opList,arg):
    if len(opList)==0:
        return arg
    else:
        return apply(opList[1:],opList[0](arg))    

def addLevel(opList,fctList):
    return [x+[y] for y in fctList for x in opList]
def findSequence(initial,goal):
    opList = [[]]
    for i in range(1,goal-initial+1):
        opList = addLevel(opList,[increment,square])
        print(opList )
        for seq in opList:
            if apply(seq,initial)==goal:
                return seq                
answer = findSequence(1,100)
print ('answer =',answer)
