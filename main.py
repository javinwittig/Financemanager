
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
        transaction = input("Enter the date of the transachtion (dd-mm-yyyy) or press Enter for today")
        if transaction == "":
            datum = date.today()
            amount = input("Enter the amount: ")
            category = input ("Enter the category (I for income, E for Expense): ")
            description= input ("Enter a description:")


            toWrite = [
                ["datum","amount","category","description"],
                [datum,amount,category,description]
            ]  

            file = open('finance_data.csv', 'w') 

            with file:
                writer = csv.writer(file)

            for row in toWrite:
                writer.writerow(row)

        else:
            datum = transaction
            amount = input("Enter the amount: ")
            category = input ("Enter the category (I for income, E for Expense): ")
            description= input ("Enter a description:")


            toWrite = [
                ["datum","amount","category","description"],
                [datum,amount,category,description]
            ]  
            
            file = open('finance_data.csv', 'w') 
            
            with file:
                writer = csv.writer(file)
            
            for row in toWrite:
                writer.writerow(row)








            



             



    

            


    









































