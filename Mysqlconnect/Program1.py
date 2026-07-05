#Company comparison (same country)
def Program1():
    import mysql.connector
    import matplotlib.pyplot as pt

    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database=""
    )

    mycursor = mydb.cursor()


    while True:
        print("1.Japan")
        print("2.India")
        print("3.UAE")
        print("4.Exit")

        userinput = input("Enter choice:")

        if userinput == "1":
            country = "Japan"
            break
        elif userinput == "2":
            country = "India"
            break
        elif userinput == "3":
            country = "USA"
            break
        elif userinput == "4":
            return
        else:
            print("Invalid Input")
            continue

    years = []
    honda = []
    nissan = []

    mycursor.execute(f"SELECT DISTINCT Sales_Year FROM sales WHERE Country='{country}' ORDER BY Sales_Year")
    sales1 = mycursor.fetchall()
    for ado in sales1:
        years.append(ado[0])

    mycursor.execute(f"SELECT Sales FROM sales WHERE Country='{country}' AND BrandID=1 ORDER BY Sales_Year")
    year = mycursor.fetchall()
    for zpd in year:
        honda.append(zpd[0])

    mycursor.execute(f"SELECT Sales FROM sales WHERE Country='{country}' AND BrandID=2 ORDER BY Sales_Year")
    sales2 = mycursor.fetchall()
    for ep in sales2:
        nissan.append(ep[0])

    pt.figure(figsize=(8, 5))

    pt.plot(years, honda, marker='o', color="red", label="Honda")
    pt.plot(years, nissan, marker='o', color="blue", label="Nissan")

    pt.xticks(years)
    pt.title(f"Comparison of Honda and Nissan in {country}")
    pt.xlabel("Year")
    pt.ylabel("Sales")
    pt.legend()
    pt.grid(True)

    pt.show()

