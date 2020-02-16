import mysql.connector,os
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='school')
cur=mydb.cursor()
while(True):
    os.system('cls')
    print("1. Create Teacher Table in Data Base")
    print("2. show all Teachers")
    print("3. Add Teacher")
    print("4. Update Teacher Class using Teacher ID")
    print("5. Delete Teacher using Teacher ID")
    print("6. Increment Salary")
    print("7. Decrement Salary")
    print("8. Delete All Data")
    print("9. Delete Table")
    print("10. Exit")
    x=int(input("Enter your Choice"))
    if x==1:
        s="CREATE table teacher(teacher_id int PRIMARY KEY, name varchar(50), salary int, class varchar(20),course_id int, department_id int, FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE, FOREIGN KEY (department_id) REFERENCES department(department_id) ON DELETE CASCADE)"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table already exist")
        else:
            print("Table Created Successfully")
 
    if x==2:
        s="SELECT * from teacher"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            result=cur.fetchall()
            print()
            print("Total Teacher Enteries: ",cur.rowcount)
            print()
            for row in result:
                print("Teacher ID:         ",row[0])
                print("Teacher Name:       ",row[1])
                print("Teacher Salary:     ",row[2])
                print("Teacher Class:      ",row[3])
                print("Teacher Course ID:  ",row[4])
                print("Teacher Department ID:  ",row[5])
                print()
    if x==3:
        s="INSERT into teacher VALUES(%s,%s,%s,%s,%s,%s)"
        a=input("Enter Teacher ID")
        b=input("Enter Teacher Name")
        c=input("Enter Teacher Salary")
        e=input("Enter Class")
        f=input("Enter Course ID")
        g=input("Enter Department ID")
        b1=(a,b,c,e,f,g)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.IntegrityError:
            print("Teacher ID cannot be same or Course Id doesn't Exist")
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            print("Data Inserted Successfully")
        mydb.commit()
    if x==4:
        s="UPDATE teacher SET class=%s WHERE teacher_id=%s"
        a=input("Enter New Class")
        b=input("Enter Teacher ID")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Table Updated Successfully")

    if x==5:
        s="DELETE from teacher WHERE teacher_id=%s"
        t=input("Enter Teacher ID")
        try:
            cur.execute(s,(t,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Deletion Successfull")
    if x==6:
        s="UPDATE teacher SET salary=salary+%s WHERE teacher_id=%s"
        a=int(input("Enter Increment"))
        b=input("Enter Teacher ID")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Table Updated Successfully")
    if x==7:
        s="UPDATE teacher SET salary=salary-%s WHERE teacher_id=%s"
        a=int(input("Enter Decrement"))
        b=input("Enter Teacher ID")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Table Updated Successfully")
    if x==8:
        s="TRUNCATE table teacher"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Deletion Successfull")
    if x==9:
        s="DROP table teacher"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Deletion Successfull")
    if x==10:
        break;
    input("Press any key to continue..")
print("Thankyou for using this application")
        
        
    
    
