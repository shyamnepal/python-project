import reverse
def andGate(x,y):
    if x==1 and y==1:
        return 1
    else:
        return 0

def orGate(x,y):
    if x==0 and y==0:
        return 0
    else:
        return 1

def xorGate(x,y):
    if (x==1 and y==1) or (x==0 and y==0):
        return 0
    else:
        return 1
        


def BinaryAddition(number1,number2):
            cin=0
            arrayList=[]
            for i in range(len(number1)-1,-1,-1):
                        x=int(number1[i])
                        y=int(number2[i])
                        bSum=xorGate(cin,(xorGate(x,y)))
                        cout_first=andGate(cin,(xorGate(x,y)))
                        cout_second=andGate(x,y)
                        cout_last=orGate(cout_first,cout_second)
                        cin=cout_last
                        arrayList.append(bSum)
            arrayList2=reverse.reverse(arrayList)
            return arrayList2
            
            
            
