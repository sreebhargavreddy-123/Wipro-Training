import mysql.connector

# ==========================================
# MYSQL CONNECTION
# ==========================================
try:
    mysql_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="wipro"
    )

    cursor = mysql_conn.cursor()
    print("Connected to MySQL successfully")

except Exception as e:
    print("MySQL connection failed:", e)
    exit()


# ==========================================
# 1. FETCH EMPLOYEES WITH SALARY > 50000
# ==========================================
try:
    fetch_query = "SELECT * FROM employee WHERE salary > 50000"
    cursor.execute(fetch_query)

    results = cursor.fetchall()

    print("\nEmployees earning more than 50,000:")
    for emp in results:
        print(emp)

except Exception as e:
    print("Error fetching data:", e)


# ==========================================
# 2. INSERT NEW EMPLOYEE RECORD
# ==========================================
try:
    insert_query = """
    INSERT INTO employee (employee_name, department, salary)
    VALUES (%s, %s, %s)
    """

    new_employee = ("Ganesh", "IT", 70000)
    cursor.execute(insert_query, new_employee)

    mysql_conn.commit()
    print("\nNew employee inserted successfully")

except Exception as e:
    print("Error inserting employee:", e)


# ==========================================
# 3. UPDATE SALARY BY 10% FOR SPECIFIC EMPLOYEE
# ==========================================
try:
    emp_id = 1

    update_query = """
    UPDATE employee
    SET salary = salary * 1.10
    WHERE employee_id = %s
    """

    cursor.execute(update_query, (emp_id,))
    mysql_conn.commit()

    print("\nEmployee salary updated by 10%")

except Exception as e:
    print("Error updating salary:", e)


# ==========================================
# CLOSE MYSQL CONNECTION
# ==========================================
cursor.close()
mysql_conn.close()
print("\nMySQL connection closed")


# ==========================================
# PART B: MONGODB
# ==========================================

from pymongo import MongoClient

print("\n==============================")
print("MongoDB Operations")
print("==============================")

try:
    # CONNECT TO MONGODB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["wipro"]
    collection = db["employees"]

    print("Connected to MongoDB successfully")

    # --------------------------------------
    # 1. INSERT NEW EMPLOYEE DOCUMENT
    # --------------------------------------
    new_employee_doc = {
        "name": "Ravi",
        "department": "IT",
        "salary": 65000
    }

    collection.insert_one(new_employee_doc)
    print("\nNew employee inserted into MongoDB")

    # --------------------------------------
    # 2. FIND ALL EMPLOYEES IN IT DEPARTMENT
    # --------------------------------------
    print("\nEmployees in IT department:")
    for emp in collection.find({"department": "IT"}):
        print(emp)

    # --------------------------------------
    # 3. UPDATE SALARY OF EMPLOYEE BY NAME
    # --------------------------------------
    employee_name = "Ravi"

    collection.update_one(
        {"name": employee_name},
        {"$set": {"salary": 75000}}
    )

    print("\nEmployee salary updated in MongoDB")

    client.close()
    print("\nMongoDB connection closed")

except Exception as e:
    print("MongoDB Error:", e)
