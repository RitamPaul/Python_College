def add(num1, num2):
    return num1+num2

#_main_
while(True):
    num1 = float(input("\nEnter your 1st number = "))
    num2 = float(input("Enter your 2nd number = "))
    ans = add(num1+num2)
    print("The sum of {} + {} = {}".format(num1, num2, ans))
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue