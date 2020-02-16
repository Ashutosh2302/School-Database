import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='school')
cur=mydb.cursor()
while(True):
    print("1. Show all Students")
    print("2. Show all Teachers")
    print("3. Show all Transport")
    print("4. Show all Courses")
    print("5. Show all Departements")
    print("6. Show students in a department")
    print("7. Show Students in a Bus")
    print("8. Show Teacher in a course")
    print("9. Show Teachers in a deparment")
    print("10.Exit")
    x=int(input("Enter your choice"))
    if x==1:
        s="SELECT * FROM student"
        try:
            cur.execute(s)
        except mysql.connector.errors.ProgrammingError:
            print("Table Dosen't Exist")
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
                print("Teacher ID:             ",row[0])
                print("Teacher Name:           ",row[1])
                print("Teacher Salary:         ",row[2])
                print("Teacher Class:          ",row[3])
                print("Teacher Course ID:      ",row[4])
                print("Teacher Department ID:  ",row[5])
                print() 
    if x==3:
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
    if x==4:
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
    if x==5:
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
    if x==6:
        s="SELECT student_id,name,class,fee_status,Bus_no,department_name FROM student,department WHERE student.department_id=department.department_id AND student.department_id=%s"
        a=input("Enter Department ID")
        try:
            cur.execute(s,(a,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            results=cur.fetchall()
            print()
            print("Total Rows: ",cur.rowcount)
            print()
            for row in results:
                print("Student ID:          ",row[0])
                print("Student Name:        ",row[1])
                print("Student Class:       ",row[2])
                print("Fee Status:          ",row[3])
                print("Bus No:              ",row[4])
                print("Department Name:     ",row[5])
                print()
    if x==7:
        s="SELECT student_id,name,class,fee_status,student.Bus_no,Route FROM student,transport WHERE student.Bus_no=transport.Bus_no AND student.Bus_no=%s"
        a=input("Enter Bus No")
        try:
            cur.execute(s,(a,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            results=cur.fetchall()
            print()
            print("Total Rows: ",cur.rowcount)
            print()
            for row in results:
                print("Student ID:       ",row[0])
                print("Student Name:     ",row[1])
                print("Student Class:    ",row[2])
                print("Fee Status:       ",row[3])
                print("Bus No:           ",row[4])
                print("Bus Route         ",row[5])
                print()
    if x==8:
        s="SELECT teacher_id,name,salary,class,department_id,course_name FROM teacher,courses WHERE teacher.course_id=courses.course_id AND course_name=%s"
        a=input("Enter Course Name")
        try:
            cur.execute(s,(a,))
        except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
        else:
            results=cur.fetchall()
            print()
            print("Total Rows: ",cur.rowcount)
            print()
            for row in results:
                print("Teacher ID:       ",row[0])
                print("Teacher Name:     ",row[1])
                print("Salary:           ",row[2])
                print("Class:            ",row[3])
                print("Department ID:    ",row[4])
                print("Course Name       ",row[5])
                print()
    if x==9:
     s="SELECT teacher_id,name,class,department_name,course_name from teacher INNER JOIN courses ON teacher.course_id=courses.course_id INNER JOIN department ON teacher.department_id=department.department_id AND department_name=%s"
     a=input("Enter Department Name")
     try:
            cur.execute(s,(a,))
     except mysql.connector.errors.ProgrammingError:
            print("Table Doesn't Exist")
     else:
            results=cur.fetchall()
            print()
            print("Total Rows: ",cur.rowcount)
            print()
            for row in results:
                print("Teacher ID:       ",row[0])
                print("Teacher Name:     ",row[1])
                print("Class:            ",row[2])
                print("Department Name:  ",row[3])
                print("Course Name:      ",row[4])
                print()
    if x==10:
        break;
    input("Press any key to continue")
        
print("Thankyou for using this application")
