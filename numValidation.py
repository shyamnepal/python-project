def ValidationNum(number):
            while number<0 or number>255:
                        print("\n")
                        print("your input is invalid..")
                        number=int(input("please! enter valid number (from 0 to 255): "))
            return number
