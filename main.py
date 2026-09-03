
import json




while True:
    A = input("Hast du bereits ein Konto(Yes/No) ")

    if A == "No":
        NewUsername = input("Plaese enter your new Username")
        
        NewPassword = input("Please enter your new Passwort ")

        daten = {
        "Username" : NewUsername,
        "Password" : NewPassword

        }

        with open("daten.json" , "w" ,encoding="utf-8" ) as f:
            json.dump(daten, f,ensure_ascii=False, indent=4 )

        break

    else:

        
        while True:

            with open("daten.json", "r", encoding="utf-8") as f:
                daten = json.load(f)

            Username = daten["Username"]
            Password = daten["Password"]




            EingabeUsername = input("Plaese enter your Username")

            EingabePassword = input("Please enter your Passwort ")

            if EingabeUsername == Username and EingabePassword == Password:
                print("Login erfolgreich!")
                break
            else:
             print("Username or Password false, try again.")

        




    








einzahlung = input("Möchtest du dein Kontostand anschauen (A) oder eine Ausgabe tätigen (B) oder eine einzahlung (C)")












































