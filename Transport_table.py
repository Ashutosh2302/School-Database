import mysql.connector,os
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='school')
cur=mydb.cursor()
while(True):
    os.system('cls')
    print("1. Create Table Transport")
    print("2. Show all buses Operational")
    print("3. Add Bus")
    print("4. update Bus Route")
    print("5. Delete Bus")
    print("6. Delete All Data")
    print("7. Delete Table")
    print("8. Exit")
    x=int(input("Enter your choice"))
    if x==1:
        s="CREATE TABLE transport(Bus_no integer PRIMARY KEY, Route varchar(50))"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Table Created Successfully")
    if x==2:
        s="SELECT * FROM transport"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            result=cur.fetchall()
            print()
            print("Total Bus Enteries: ",cur.rowcount)
            print()
            for row in result:
                print("Bus No:    ",row[0])
                print("Bus route: ",row[1])
                print()
    if x==3:
        s="INSERT INTO transport VALUES(%s,%s)"
        a=input("Enter Bus No")
        b=input("Enter Bus Route")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        except mysql.connector.errors.IntegrityError:
            print("Bus no cannot be same")
        else:
            mydb.commit()
            print("Insertion Successful")
    if x==4:
        s="UPDATE transport SET route=%s WHERE Bus_no=%s"
        a=input("Enter New Route")
        b=input("Enter Bus No")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Table Updated Successfully")
    if x==5:
        s="DELETE from transport WHERE Bus_no=%s"
        a=input("Enter Bus No")
        try:
            cur.execute(s,(a,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Delection Successful")
    if x==6:
        s="TRUNCATE table transport"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Delection Successful")
    if x==7:
        s="DROP table transport"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Deletion Successfull")
    if x==8:
       break;
    print("Press any key to continue")
    input()
print("Thankyou for using this application")
