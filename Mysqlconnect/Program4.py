#Country comparison (same brand)
def Program4():
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
        print("1. Honda")
        print("2. Nissan")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            brand_id = 1
            brand_name = "Honda"
            break
        elif choice == "2":
            brand_id = 2
            brand_name = "Nissan"
            break
        elif choice == "3":
            return
        else:
            print("Invalid input")

    countries = ["Japan", "USA", "India"]
    totals = []

    for c in countries:
        mycursor.execute(f"SELECT SUM(Sales) FROM sales WHERE BrandID={brand_id} AND Country='{c}'")
        totals.append(mycursor.fetchone()[0])

    pt.bar(countries, totals)
    pt.title(f"Country Comparison: {brand_name}")
    pt.xlabel("Country")
    pt.ylabel("Total Sales")
    pt.show()
