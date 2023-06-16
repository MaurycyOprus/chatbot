def get_help():
    print(" Czesc tu Stefan! Jestem asystentem twojego asystenta. \n Pokaze ci kilka mozliwych zapytan, z ktorych mozesz skorzystac. \n Wybierz kategorie: \n 1 - rezerwacja \n 2 - zamowienia \n 3 - platnosc \n 4 - rekomendacje  \n 5 - wyjdz ")
    while True:
        user = input(" Twoj wybor: ")
        if user.isdigit():
            if int(user) == 1:
                print(" Przykładowe zapytania: ")
                print("chcialbym zarezerwowac stolik na jutro na dziesiata trzydziesci dla trzech osob")
                print("chcialbym zarezerwowac stolik na srode na jedenasta na piec osob")
            elif int(user) == 2:
                print(" Przykładowe zapytania: ")
                print("chcialbym zamowic margharita")
                print("chcialabym zamowic lody")
                print("poprosze piwo jasne")
            elif int(user) == 3:
                print(" Przykładowe zapytania: ")
                print("czy moge zaplacic karta")
                print("chce zaplacic za zamowienie")
                print("mam zamiar uregulowac rachunek blikiem")
            elif int(user) == 4:
                print(" Przykładowe zapytania: ")
                print("jakie napoje polecasz")
                print("ktora pizza najlepsza")
                print("jaki sok polecasz")
            elif int(user) == 5:
                print(" Mam nadzieje, ze pomoglem! \n ~ Stefan - asystent asystenta")
                break
            else:
                print("Podałeś niepoprawną wartość!")
        else:
            print(" Wybierz wartosc 1, 2, 3, 4 lub 5 z podanej listy")

        print(" Wybierz kategorie: \n 1 - rezerwacja \n 2 - zamowienia \n 3 - platnosc \n 4 - rekomendacje  \n 5 - wyjdz ")
