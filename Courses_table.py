import mysql.connector,os
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='school')
cur=mydb.cursor()
while(True):
    os.system('cls')
    print("1. Create Courses Table")
    print("2. Show All Courses")
    print("3. Insert Course")
    print("4. Delete Course")
    print("5. Update Table")
    print("6. Delete All")
    print("7. Delete Table")
    print("8. Exit")
    x=int(input("Enter Your Choice"))
    if x==1:
        s="CREATE TABLE courses(course_id int PRIMARY KEY,course_name varchar(30))"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Already Exists")
        else:
            print("Table Created Successfully")
    if x==2:
        s="SELECT * from courses"
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
                print("Course ID:    ",row[0])
                print("Course Name:  ",row[1])
                print()
    if x==3:
        s="INSERT INTO courses VALUES(%s,%s)"
        a=input("Enter Course ID")
        b=input("Enter Course Name")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        except mysql.connector.errors.IntegrityError:
            print("Course ID cannot be same")
        else:
            mydb.commit()
            print("Insertion Successful")
        
    if x==4:
        s="DELETE from courses WHERE course_id=%s"
        d=input("Enter Course ID")
        try:
            cur.execute(s,(d,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Deletion Successful")
    if x==5:
        s="UPDATE courses SET course_name=%s WHERE course_id=%s"
        a=input("Enter new course name")
        b=input("Enter Course ID")
        b1=(a,b)
        try:
            cur.execute(s,b1)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Table Updated Successfully")
    if x==6:
        s="TRUNCATE table courses"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            mydb.commit()
            print("Deletion Successful")
    if x==7:
        s="DROP table courses"
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
        
        
        
    
