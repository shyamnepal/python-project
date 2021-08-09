def reverse(revNumList):
            actualBinary=[]
            actualBinaryNum=""
            for i in range(len(revNumList)-1,-1,-1):
                        actualBinary.append(revNumList[i])
                        actualBinaryNum=actualBinaryNum+str(revNumList[i])
            return actualBinaryNum
