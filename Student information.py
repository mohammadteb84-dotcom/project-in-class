import mysql.connector

users = []

def add_to_db(user):
    mydb = mysql.connector.connect(
        host="localhost",
        user="classuser",
        password="Aa123456",
        database="classuser"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO students (name, lastname, ncode, grade) VALUES (%s, %s, %s, %s)"
    values = (user["name"], user["lastname"], user["ncode"], user["grade"])

    mycursor.execute(sql, values)
    mydb.commit()

    mycursor.close()
    mydb.close()

def show_menu():
    print("\nPlease Enter a number 1 to 4")
    print("1: new Register")
    print("2: Report")
    print("3: Sort by Grade")
    print("4: Exit")
    return int(input())

def get_user_info():
    name = input("name: ")
    lastname = input("lastname: ")
    ncode = input("ncode: ")
    grade = int(input("grade: "))  # بهتره عددی باشه

    return {
        "name": name,
        "lastname": lastname,
        "ncode": ncode,
        "grade": grade
    }

def sort_list(users):
    if not users:
        print("No records to sort")
        return

    sorted_users = sorted(users, key=lambda x: x["grade"])
    for user in sorted_users:
        print(user)

# اجرای کد --------------------------------
while True:
    value = show_menu()

    if value == 1:
        user_dict = get_user_info()
        users.append(user_dict)

        # ذخیره در دیتابیس همزمان
        add_to_db(user_dict)

        print("Your Registration has done successfully (Saved in DB)")

    elif value == 2:
        if len(users) == 0:
            print("No users")
        else:
            for u in users:
                print(u)

    elif value == 3:
        sort_list(users)

    elif value == 4:
        break

    else:
        print("Wrong number")
