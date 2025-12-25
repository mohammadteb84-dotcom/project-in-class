import mysql.connector

users = []

# 1. show menu
def show_menu():
    print("\n1: new Register")
    print("2: Report")
    print("3: Sort by Grade")
    print("4: Exit")
    return int(input())


# 2. get user info
def get_user_info():
    name = input("name: ")
    lastname = input("lastname: ")
    ncode = input("ncode: ")
    grade = int(input("grade: "))
    return add_to_disct(name, lastname, ncode, grade)


# 3. add to disct
def add_to_disct(name, lastname, ncode, grade):
    user_dict = {
        "name": name,
        "lastname": lastname,
        "ncode": ncode,
        "grade": grade
    }
    return user_dict


# 4. add to list
def add_to_list(user_list, user_dict):
    user_list.append(user_dict)


# 5. sort list
def sort_list(users):
    if not users:
        print("No records to sort")
        return

    sorted_users = sorted(users, key=lambda x: x["grade"])
    for user in sorted_users:
        print(user)


# 6. database
def add_to_db(user_dict):
    mydb = mysql.connector.connect(
        host="localhost",
        user="classuser",
        password="Aa123456",
        database="classuser"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO students (name, lastname, ncode, grade) VALUES (%s, %s, %s, %s)"
    values = (
        user_dict["name"],
        user_dict["lastname"],
        user_dict["ncode"],
        user_dict["grade"]
    )

    mycursor.execute(sql, values)
    mydb.commit()

    mycursor.close()
    mydb.close()


# ---------------- main ----------------
while True:
    choice = show_menu()

    if choice == 1:
        user = get_user_info()
        add_to_list(users, user)
        add_to_db(user)
        print("Saved successfully")

    elif choice == 2:
        if not users:
            print("No users")
        else:
            for u in users:
                print(u)

    elif choice == 3:
        sort_list(users)

    elif choice == 4:
        break

    else:
        print("Wrong choice")
