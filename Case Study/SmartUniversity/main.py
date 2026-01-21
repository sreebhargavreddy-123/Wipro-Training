from models.student import Student
from models.faculty import Faculty
from models.course import Course
from utils.generators import student_generator
from utils.file_handler import save_students_json, generate_csv_report
from utils.display import title, section, success, error


students = []
faculty_list = []
courses = []

while True:
    title("SMART UNIVERSITY MANAGEMENT SYSTEM")

    print("""
    1️⃣  Add Student
    2️⃣  Add Faculty
    3️⃣  Add Course
    4️⃣  Calculate Student Performance
    5️⃣  Compare Two Students
    6️⃣  Generate Reports
    7️⃣  Show Students
    8️⃣  Exit
    """)

    choice = input("👉 Enter your choice: ")

    try:
        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Marks (5): ").split()))

            students.append(Student(sid, name, dept, sem, marks))
            print("Student Created Successfully")
            print("--------------------------------")
            print(f"ID        : {sid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")
            print(f"Semester  : {sem}")
            print("_" * 40)


        elif choice == "2":
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            salary = int(input("Salary: "))

            faculty_list.append(Faculty(fid, name, dept, salary))
            print("Faculty Created Successfully")
            print("--------------------------------")
            print(f"ID        : {fid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")
            print("_" * 40)



        elif choice == "3":
            code = input("Course Code : ")
            name = input("Course Name : ")
            credits = int(input("Credits     : "))
            fac_id = input("Faculty ID  : ")
            faculty_obj = None
            for f in faculty_list:
                if f.id == fac_id:
                    faculty_obj = f
                    break
            if faculty_obj is None:
                print("Error: Faculty ID not found")
            else:
                course = Course(code, name, credits, faculty_obj)
                courses.append(course)
                print("Course Added Successfully")
                print("--------------------------------")
                print(f"Course Code : {course.code}")
                print(f"Course Name : {course.name}")
                print(f"Credits     : {course.credits}")
                print(f"Faculty     : {course.faculty.name}")
                print("_" * 40)




        elif choice == "4":
            if not students:
                print("Error: No students found")
            else:
                print("Student Performance Report")
                print("--------------------------------")
                for student in students:
                    avg, grade = student.calculate_performance()
                    print(f"Student Name : {student.name}")
                    print(f"Marks        : {student.marks}")
                    print(f"Average      : {avg:.1f}")
                    print(f"Grade        : {grade}")
                    print("_" * 40)





        elif choice == "5":
            if len(students) < 2:
                print("Error: At least two students are required")
            else:
                print("Compare Two Students (> operator)")
                print("Comparing Students Performance")
                print("--------------------------------")
                for s in students:
                    print(f"{s.id} - {s.name}")
                id1 = input("Enter Student ID 1: ")
                id2 = input("Enter Student ID 2: ")
                s1 = s2 = None
                for s in students:
                    if s.id == id1:
                        s1 = s
                    if s.id == id2:
                        s2 = s
                if s1 is None or s2 is None:
                    print("Error: Invalid Student ID")
                else:
                    print(f"{s1.name} > {s2.name} : {s1 > s2}")
                    print("_" * 40)




        elif choice == "6":
            section("GENERATING REPORTS")
            generate_csv_report(students)
            save_students_json(students)
            success("All reports generated successfully")



        elif choice == "7":
            if not students:
                print("Error: No students found")
            else:
                print("Student Record Generator")
                print("Fetching Student Records...")
                print("--------------------------------")
                for record in student_generator(students):
                    print(record)
                print("_" * 40)




        elif choice == "8":
            print("Thank you for using Smart University Management System")
            print("_" * 40)
            break


    except Exception as e:
        print(str(e))
