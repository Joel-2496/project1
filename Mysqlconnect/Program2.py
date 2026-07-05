

# Single company trend (over time)
def Program2():
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
        print("1.Honda")
        print("2.Nissan")
        print("3.Return")

        userinput = input("Enter choice:")

        if userinput == "1":
            brand_id = 1
            brand_name = "Honda"
            break
        elif userinput == "2":
            brand_id = 2
            brand_name = "Nissan"
            break
        elif userinput == "3":
            return
        else:
            print("Invalid input")

    years = []
    sales = []


    mycursor.execute(f"SELECT Sales_Year, SUM(Sales) FROM sales WHERE BrandID={brand_id} group by sales_year ORDER BY Sales_Year")

    for year, value in mycursor.fetchall():
        years.append(year)
        sales.append(value)


    pt.figure(figsize=(8, 5))

    pt.plot(years, sales, marker="o", label=brand_name)

    pt.xticks(years)
    pt.title(f"{brand_name} Sales Over Time")
    pt.xlabel("Year")
    pt.ylabel("Sales")
    pt.legend()
    pt.grid(True)

    pt.show()
