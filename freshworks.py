import json
import CRD as x

print("..........................Select one chioce.......................")
print("")
print("To create key-value pairs  -->  create")
print("To read the data in file   -->  read")
print("To delete the data in file -->  delete")
print("To show data in file       -->  file")
print("To qiut this programm      -->  Exit")
while(True):
    print("")
    ch=input("Enter your choice:")
    if ch not in ["create","read","delete","file","Exit"]:
        print("Select above choice only.")
    elif ch=="create":
        print("Enter key and value: ",end="")
        k,v=input().split()
        print("Do U want TimeToLive",end="")
        c=input("Yes or No:")
        if (c=='Yes'):
            t=int(input("Enter time in seconds"))
            x.create(k,int(v),t)
        else:
            x.create(k,int(v))
    elif ch=="read":
        print("Enter key to read data: ",end="")
        x.read(input())
    elif ch=="delete":
        print("Enter key to delete: ",end="")
        x.delete(input())
    elif ch=="file":
        print("It shows the all content of file")
        x.show()
    elif ch=='Exit':
        x.Exit()
        break
    


    
    






    

    

