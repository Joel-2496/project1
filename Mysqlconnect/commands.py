
def commands():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="python_video"
    )
    mycursor = mydb.cursor()
    while True:
        print("TABLE MENU")
        print("1. Insert")
        print("2. Update")
        print("3. Delete")
        print("4. Display")
        print("5. Back to Main Menu")

        table_choice = input("Enter choice: ").strip()

        if table_choice == "1":  # INSERT
            brand = input("Brand: ")
            country = input("Country: ")
            year = input("Year: ")
            sales = input("Sales: ")

            sql = "insert into sales (Brand, Country, Year, Sales) VALUES (%s, %s, %s, %s)"  # s is used as placeholder so no sql injection
            mycursor.execute(sql, (brand, country, year, sales))
            mydb.commit()  # commit is used to directly effect the table
            print("Inserted")

        elif table_choice == "2":  # UPDATE
            idd = input("SalesID to update: ")
            new_sales = input("New Sales Value: ")

            sql = "update sales set Sales=%s WHERE SalesID=%s"
            mycursor.execute(sql, (new_sales,idd))
            mydb.commit()
            print("Updated")

        elif table_choice == "3":  # DELETE
            idd = input("SalesID To Delete: ")

            sql = "delete FROM sales where SalesID=%s"
            mycursor.execute(sql, (idd,))  # comma is used here since it needs a tuple
            mydb.commit()
            print("Deleted")

        elif table_choice == "4":  # DISPLAY
            mycursor.execute("select * from sales")
            for row in mycursor.fetchall():  # gets the data from mycursor
                print(row)

        elif table_choice == "5":
            break

        else:
            print("Invalid choice")
