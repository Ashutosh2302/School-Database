import mysql.connector,os
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='school')
cur=mydb.cursor()
while(True):
    os.system('cls')
    print("1. Create Department Table")
    print("2. Show All Departments")
    print("3. Insert Department")
    print("4. Delete Department")
    print("5. Update Department")
    print("6. Delete All")
    print("7. Delete Table")
    print("8. Exit")
    x=int(input("Enter Your Choice"))
    if x==1:
        s="CREATE TABLE department(department_id int PRIMARY KEY,department_name varchar(30))"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Already Exists")
        else:
            print("Table Created Successfully")
    if x==2:
        s="SELECT * from department"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            results=cur.fetchall()
            print()
            print("Total Enteries in Table: ",cur.rowcount)
            print()
            for row in results:
                print("Department ID:    ",row[0])
                print("Department Name:  ",row[1])
                print()
    if x==3:
        s="INSERT INTO department VALUES(%s,%s)"
        a=input("Enter Department ID")
        b=input("Enter Department Name")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        except mysql.connector.errors.IntegrityError:
            print("Department ID cannot be same")
        else:
            mydb.commit()
            print("Insertion Successful")
        
    if x==4:
        s="DELETE from department WHERE department_id=%s"
        d=input("Enter Course ID")
        try:
            cur.execute(s,(d,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Deletion Successful")
    if x==5:
        s="UPDATE department SET department_name=%s WHERE department_id=%s"
        a=input("Enter new Department name")
        b=input("Enter Department ID")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Table Updated Successfully")
    if x==6:
        s="TRUNCATE table department"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Deletion Successful")
    if x==7:
        s="DROP table department"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        except mysql.connector.errors.DatabaseError:
            print("Cannot Delete Table, referenced by foreign key constraint")
        else:
            mydb.commit()
            print("Deletion Successful")
    if x==8:
        break;
    input("Press any key to continue..")
print("Thankyou for using this application")        
        

