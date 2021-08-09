def DecimalInToBinary(decimalNo):
            bit=[]
            counter=0
            while counter!=8:
                        Remainder=decimalNo%2
                        bit.append(Remainder)
                        decimalNo=decimalNo//2
                        counter=counter+1
            return bit

