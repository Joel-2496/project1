import mysql.connector
import programs


mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="2496",
    database="python_video"
)

mycursor = mydb.cursor()

while True:
    print("Main Menu")
    print("1.Table commands")
    print("2.Analysis")
    print("3.Exit")

    choice1=input("Enter your choice: ").strip()
    if choice1 == "1":
        programs.commands()

    elif choice1== "2":
        print("ANALYSIS OF SALES OF CARS")
        print("1.Company comparison (same country)")
        print("2.Single company trend (over time)")
        print("3.Country comparison (same brand)")
        print("4.Final combined visual")
        print("5.Exit")

        choice2 = input("Enter your choice: ").strip()

        if choice2 == "1":
            programs.Program1()
        elif choice2 == "2":
            programs.Program2()
        elif choice2 == "3":
            programs.Program3()
        elif choice2 == "4":
            programs.Program4()
        elif choice2 == "5":
            break
        else:
            print("Invalid choice")
            continue
    elif choice1 == "3":
        break

    else:
        print("Invalid choice")