
import json
import pandas as pd
import csv
from datetime import date


while True:
    A = input("Hast du bereits ein Konto(Yes/No) ")

    if A == "No":
        NewUsername = input("Plaese enter your new Username: ")
        NewPassword = input("Please enter your new Passwort: ")
        

        daten = {
            "Username": NewUsername,
            "Password": NewPassword,
           
        }

        with open("daten.json", "w", encoding="utf-8") as f:
            json.dump(daten, f, ensure_ascii=False, indent=4)

        


    with open("daten.json", "r", encoding="utf-8") as f:
        daten = json.load(f)

    Username = daten["Username"]
    Password = daten["Password"]

    while True:
        EingabeUsername = input("Plaese enter your Username: ")
        EingabePassword = input("Please enter your Passwort: ")

        if EingabeUsername == Username and EingabePassword == Password:
            print("Login erfolgreich!")
            break
        else:
            print("Username or Password false, try again.")

    break 






while True:
    print("1. Add a new transaction")
    print("2. View transaction within a date range and summary")
    print("3. Exit")

    Frage = input("Enter your Choice: ")

    if Frage == "1":  
       
            transaction = input("Enter the date of the transaction (dd-mm-yyyy) or press Enter for today: ")
            if transaction == "":
                datum = date.today().strftime("%d-%m-%Y")
            else:
                datum = transaction

            amount = input("Enter the amount: ")
            category_input = input("Enter the category (I for income, E for Expense): ").strip().upper()
            category = "Income" if category_input == "I" else "Expense"
            description = input("Enter a description: ")

            toWrite = [[datum, amount, category, description]]

            with open('finance_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(toWrite)

    elif Frage == "2":
        df = pd.read_csv('finance_data.csv', index_col=False)
        df["datum"] = pd.to_datetime(df["datum"], format="%d-%m-%Y")   # NEU: Datum korrekt umwandeln

        Start = input("Enter the start date(dd-mm-yyyy)")
        End = input("Enter the end date (dd-mm-yyyy)")

        start_date = pd.to_datetime(Start, format="%d-%m-%Y")
        end_date = pd.to_datetime(End, format="%d-%m-%Y")

        filtered_df = df[(df["datum"] >= start_date) & (df["datum"] <= end_date)]

        filtered_df_display = filtered_df.copy()
        filtered_df_display['datum'] = filtered_df_display['datum'].dt.strftime('%d-%m-%Y')

        print("\n--- Filtered Transactions ---")
        print(filtered_df_display)

        # Zusammenfassung (Summary) berechnen
        total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].astype(float).sum()
        total_expense = filtered_df[filtered_df['category'] == 'Expense']['amount'].astype(float).sum()
        net_savings = total_income - total_expense

        print("\n--- Zusammenfassung ---")
        print(f"Total income: {total_income:.2f}")
        print(f"Total expense:  {total_expense:.2f}")
        print(f"Savings: {net_savings:.2f}\n")

    else:
        print("Program is getting closed")
        break

   
        


       






































   
           






            



             



    

            


    









































