Cash = 5000
Cash2 = 3400
Cash3 = 6000
Cash4 = 7000
Cash5 = 162
adam = "Person 1"
adam2 = "Person 2"
adam3 = "Person 3"
adam4 = "Person 4"
adam5 = "Person 5"
adam6 = "Person 6"
adamlar = [adam, adam2, adam3, adam4, adam5]

while True:
    ad = input("Adinizi ve soy adinizi daxil edin: ")
    if adam == ad:
        print("Salam", ad, "sizin balansinizda", Cash, "qeder vasait var")

        secim = input("1 ve ya 2 duymesini sixin(1 - Balans artirmaq, 2 - Balans azaltmaq): ")

        if secim == "1":
            Art = int(input("Artirmaq isdediyiniz meblegi daxil edin: "))
            Yek = Cash + Art
            print("Balansinizda", Yek, "mebleg oldu.")
        elif secim == "2":
            Azl = int(input("Azaltmaq isdediyiniz meblegi daxil edin: "))
            Qal = Cash - Azl
            if Cash > Azl:
                print("Balansinizda qalan mebleg: ", Qal)
            else:
                print("Balansinda yeterli mebleg qoqqo")
        break

    elif adam2 == ad:
        print("Salam", ad, "sizin balansinizda", Cash2 , "qeder vasait var")

        secim2 = input("1 ve ya 2 duymesini sixin(1 - Balans artirmaq, 2 - Balans azaltmaq): ")

        if secim2 == "1":
            Art = int(input("Artirmaq isdediyiniz meblegi daxil edin: "))
            Yek = Cash2 + Art
            print("Balansinizda", Yek, "mebleg oldu.")
        elif secim2 == "2":
            Azl = int(input("Azaltmaq isdediyiniz meblegi daxil edin: "))
            Qal = Cash2 - Azl
            if Cash2 > Azl:
                print("Balansinizda qalan mebleg: ", Qal)
            else:
                print("Balansinda yeterli mebleg qoqqo")
        break

    elif adam3 == ad:
        print("Salam", ad, "sizin balansinizda", Cash3 , "qeder vasait var")
        secim3 = input("1 ve ya 2 duymesini sixin(1 - Balans artirmaq, 2 - Balans azaltmaq): ")

        if secim3 == "1":
            Art = int(input("Artirmaq isdediyiniz meblegi daxil edin: "))
            Yek = Cash3 + Art
            print("Balansinizda", Yek, "mebleg oldu.")
        elif secim3 == "2":
            Azl = int(input("Azaltmaq isdediyiniz meblegi daxil edin: "))
            Qal = Cash3 - Azl
            if Cash3 > Azl:
                print("Balansinizda qalan mebleg: ", Qal)
            else:
                print("Balansinda yeterli mebleg qoqqo")
        break

    elif adam4 == ad:
        print("Salam", ad, "sizin balansinizda", Cash4 , "qeder vasait var")
        secim4 = input("1 ve ya 2 duymesini sixin(1 - Balans artirmaq, 2 - Balans azaltmaq): ")

        if secim4 == "1":
            Art = int(input("Artirmaq isdediyiniz meblegi daxil edin: "))
            Yek = Cash4 + Art
            print("Balansinizda", Yek, "mebleg oldu.")
        elif secim4 == "2":
            Azl = int(input("Azaltmaq isdediyiniz meblegi daxil edin: "))
            Qal = Cash4 - Azl
            if Cash4 > Azl:
                print("Balansinizda qalan mebleg: ", Qal)
            else:
                print("Balansinda yeterli mebleg qoqqo")
        break



    elif adam5 == ad:
        print("Salam", ad, "sizin balansinizda", Cash5 , "qeder vasait var")
        secim5 = input("1 ve ya 2 duymesini sixin(1 - Balans artirmaq, 2 - Balans azaltmaq): ")

        if secim5 == "1":
            Art = int(input("Artirmaq isdediyiniz meblegi daxil edin: "))
            Yek = Cash5 + Art
            print("Balansinizda", Yek, "mebleg oldu.")
        elif secim5 == "2":
            Azl = int(input("Azaltmaq isdediyiniz meblegi daxil edin: "))
            Qal = Cash5 - Azl
            if Cash5 > Azl:
                print("Balansinizda qalan mebleg: ", Qal)
            else:
                print("Balansinda yeterli mebleg qoqqo")
        break

    elif adam6 == ad:
        print("Salam", ad, "sizin qeyydiyatiniz yeni oldugu ucun balansinizda", Cash5 , "qeder vasait var")
        break
    elif adamlar != ad:
        print("Bele bir qeydiyyat yoxtur, yeni qeyd yaratmaq isdeyirsinizse 's' sixin")
        sec = input("")
        if sec == "s":
            y_adam = input("Adinizi daxil edin: ")
            adam6 = y_adam
        else:
            print("bye...")
            break