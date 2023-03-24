#_main_
while(True):
    num1 = float(input("\nEnter your 1st number = "))
    num2 = float(input("Enter your 2nd number = "))
    temp = num1
    num1 = num2
    num2 = temp
    print("Now 1st no. = {}, 2nd no. = {}".format(num1, num2))
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue