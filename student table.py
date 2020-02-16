import mysql.connector,os
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='school')
cur=mydb.cursor()
while(True):
    os.system('cls')
    print("1. Create Table Student")
    print("2. Show All students");
    print("3. Show students based on fee status");
    print("4. Show students based on class");
    print("5. Add student");
    print("6. Update Student name using student_id");
    print("7. Delete student");
    print("8. Delete All data");
    print("9. Delete Table")
    print("10. Enter Bus No")
    print("11. Exit");
    x=int(input("Enter your choice"))
    if x==1:
         s="CREATE table student(student_id int PRIMARY KEY,name varchar(50),class char(4), fee_status char, department_id int,Bus_no int DEFAULT NULL, FOREIGN KEY(department_id) REFERENCES department(department_id) ON DELETE CASCADE, FOREIGN KEY(Bus_no) REFERENCES transport(Bus_no) ON DELETE CASCADE)"
         try:
             cur.execute(s)
         except mysql.connector.errors.ProgrammingError:
            print("Table already exists")
         else:
            print("Table Created Successfully")
         mydb.commit()
    if x==2:
        s="SELECT * from student"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't exist")
        else:         
            result=cur.fetchall()
            print("Total Student Enteries: ",cur.rowcount)
            print()
            for row in result:
                print("Student Id:         ",row[0])
                print("Studen Name:        ",row[1])
                print("Student Class:      ",row[2])
                print("Student Fee Status: ",row[3])
                print("Department ID:      ",row[4])
                print("Bus No:             ",row[5])
                print()
    if x==3:
        s="SELECT * from student WHERE fee_status=%s"
        f=input("Enter fee status y or n")
        try:
            cur.execute(s,(f,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't exist")
        else:
            result=cur.fetchall()
            for row in result:
                print("Student Id:         ",row[0])
                print("Studen Name:        ",row[1])
                print("Student Class:      ",row[2])
                print("Student Fee Status: ",row[3])
                print("Student Bus No:     ",row[4])
                print()
    if x==4:
        s="SELECT * from student WHERE class=%s"
        c=input("Enter class")
        try:
            cur.execute(s,(c,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't exist")
        else:
            result=cur.fetchall()
            for row in result:
                print("Student Id:            ",row[0])
                print("Studen Name:           ",row[1])
                print("Student Class:         ",row[2])
                print("Student Fee Status:    ",row[3])
                print("Student Department ID: ",row[4])
                print("Student Bus No:        ",row[4])
                print()
    if x==5:
        s="INSERT INTO student(student_id,name,class,fee_status,department_id) VALUES(%s, %s, %s, %s, %s)"
        a=input("Enter Student ID")
        b=input("Enter Student name")
        c=input("Enter class")
        d=input("Enter Fee status")
        e=input("Enter Department ID")
        b1=(a,b,c,d,e)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.IntegrityError:
            print("Student ID cannot be same of foreign Key constraint")
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't exist")
        else:
            print("Data Inserted Successfully")
        mydb.commit()
    if x==6:
        s="UPDATE student set name=%s WHERE student_id=%s"
        a=input("Enter New Name")
        b=input("Enter student_id")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't exist")
        else:
            mydb.commit()
            print("Table Updated Successfully")
    if x==7:
        s="Delete from student WHERE student_id=%s"
        a=int(input("Enter student_id"))
        try:
            cur.execute(s,(a,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't exist")
        else:
            mydb.commit()

            print("Deletion Successfull")
    if x==8:
        s="TRUNCATE table student"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't exist")
        else:
            mydb.commit()
            print("Deletion Successfull")
    if x==9:
        s="DROP table student"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't exist")
        else:
            mydb.commit()
            print("Deletion Successfull")
    if x==10:
        s="UPDATE student SET Bus_no=%s WHERE student_id=%s"
        a=input("Enter Bus no")
        b=input("Enter Student ID")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't exist")
        else:
            mydb.commit()
            print("Table Updated Successfully")
    if x==11:
        break;
    input("Press any key to continue")
print("Thankyou for using this application")
        
    

    

