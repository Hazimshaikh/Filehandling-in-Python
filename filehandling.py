#add record        
def addrec(ids,name,course,location):
    file = open("mydata.txt")
    data = file.readlines()
    file.close()

    newdata=[]
    for d in data:
        x=d.strip().split()
        newdata.append(x)

    newdata.append([ids,name,course,location])

    file = open("mydata.txt","w")
    for i,n,c,l in newdata:
        file.write(f"{i:^3} {n:^8} {c:^8} {l:^8}\n")
    file.close()

#read record
def read():
    file = open("mydata.txt")
    data = file.readlines()
    file.close()
    table =[]
    for row in data:
        table.append(row.strip().split())

    for i,n,c,l in table:
        print(f"{i:^3} {n:^8} {c:^8} {l:^8}")

#Update record
def update(ids,name,course,location):
    file = open("mydata.txt")
    data = file.readlines()
    file.close()
    newdata=[]

    for d in data:
        x=d.strip().split()
        newdata.append(x)

    newdata.pop(ids-1)
    newdata.insert(ids-1,[ids,name,course,location])

    file=open("mydata.txt","w")
    for i,n,c,l in newdata:
        file.write(f"{i:^3} {n:^8} {c:^8} {l:^8}\n")
    file.close()

#Delete Record
def delete(ids,name,course,place):
    file = open("mydata.txt")
    data = file.readlines()
    file.close()
    newdata=[]

    for d in data:
        x=d.strip().split()
        newdata.append(x)

    newdata.pop(ids-1)
    
    file=open("mydata.txt","w")
    for i,n,c,l in newdata:
        file.write(f"{i:^3} {n:^8} {c:^8} {l:^8}\n")
    file.close()

#Console base
def takeinput():
    ids=int(input("Enter the id : "))
    name=str(input("Enter the name : "))
    course=str(input("Enter the course name : "))
    location=str(input("Enter the place : "))
    return ids,name,course,location

while(True):
    print("Welcome To File hanling\n ")
    print("Selcet choice To perfom different operations \n")
    print("1 : Read record")
    print("2 : Add record")
    print("3 : Update record")
    print("4 : Delete record")
    print("5 : exit\n")

    choice=input("Enter Your Choice : ")

    if (choice=="1"):
        print("Reading Records from file \n")
        read()

    elif(choice=="2"):
        ids,name,course,location =takeinput()
        print("Added Record in File ")
        addrec(ids,name,course,location)

    elif(choice=="3"):
        ids,name,course,location =takeinput()
        print("Updated the data in file")
        update(ids,name,course,location)

    elif(choice=="4"):
        ids,name,course,location =takeinput()
        print("Deleted the data from file")
        delete(ids,name,course,location)

    
    elif(choice=="5"):
        choice=input("You really want to Exit then press y :")
        if (choice=="y"):
            break
        else:
            continue
