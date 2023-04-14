#_main_
li=[]
while(True):
    item = eval(input("\nEnter any correct format item to insert = "))
    ind = int(input("Enter the index for insertion = "))
    if(ind>len(li) or ind<0):
        print("Array index is out of range. Try Again !")
        continue
    else:
        li.insert(ind, item)
        print("Now your array = ", li)
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue