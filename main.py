import greeting
import numValidation
import binaryConversion
import reverse
import addition


greeting.GreetingAtBeginning()
continueLoop=True
while continueLoop==True:
            continueNum1=False
            while continueNum1==False:
                        try:
                                    decimalNum1=int(input("Enter first decimal number: "))
                                    decimalNum1=numValidation.ValidationNum(decimalNum1)
                                    continueNum1=True
                        except:
                                    print("\n")
                                    print("Invalid Input")

            continueNum2=False
            while continueNum2==False:
                        try:
                                    decimalNum2=int(input("Enter second decimal number: "))
                                    decimalNum2=numValidation.ValidationNum(decimalNum2)
                                    continueNum2=True
                        except:
                                    print("\n")
                                    print("Invalid Input")

            num1=binaryConversion.DecimalInToBinary(decimalNum1)
            num2=binaryConversion.DecimalInToBinary(decimalNum2)

            binaryNumber1=reverse.reverse(num1)
            binaryNumber2=reverse.reverse(num2)
            
            binaryAddition=addition.BinaryAddition(binaryNumber1,binaryNumber2)

            print("Binary number of",decimalNum1," is: ",binaryNumber1)
            print("\n")
            print("Binary number of",decimalNum2," is: ",binaryNumber2)
            print("\n")
            print("Addition of binary number is: ",binaryAddition)
            print("\n")
            continuous=input("Do you want to continue this application?? (Type No to exit) ").lower()
            if continuous=="no":
                        break

greeting.GreetingAtEnd()
            
            

