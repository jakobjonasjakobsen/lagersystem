class Item:

    def __init__(self, navn: str, id: int, pris: float, beskrivelse: str, antal: int, hylde: int, plads: str, ):
        # bekræft at der er indtastet gyldige argumenter
        assert pris >= 0, f"Pris {pris} er ikke større en 0!"
        assert antal >= 0, f"Antal {antal} er ikke større en 0!"

        # Assign til self object
        self.navn = navn
        self.id = id
        self.pris = pris
        self.beskrivelse = beskrivelse
        self.antal = antal
        self.hylde = hylde
        self.plads = plads

# definér funktioner
    def pris_pr_stk(self):
        print("Pris pr stk med moms: ")
        return self.pris

    def total_price(self):
        print("Samlet pris: ")
        return self.pris * self.antal

    def pris_uden_moms(self):
        print("Pris pr stk uden moms: ")
        return self.pris / 1.25

    def total_price_uden_moms(self):
        print("Samlet pris uden moms: ")
        return self.pris / 1.25 * self.antal

# assign parametre til __init__
item1 = Item("Laptop", 1, 799.99, "i5 16gb 3200 mHz gtx 1660", 7, 2, "Lagerrum 1")
item2 = Item("Desktop", 2, 1499.95, "i7 4790k, 32 gb 3600 mhz, gtx 1660 ", 4, 1, "Lagerrum 1")
item3 = Item("Headset", 3, 699.95, "SENNHEISER HD 350", 8, 4, "Lagerrum 1")
item4 = Item("Mouse", 4, 499.95, "Logitech G Pro wireless", 11, 4, "Lagerrum 1")
item5 = Item("Monitor", 5, 1995.95, "ASUS VG258QR", 6, 4, "Lagerrum 1")
item6 = Item("iPhone 6", 6, 399.95, "refurb iPhone 6 64gb carrier unlocked", 4, 1, "Lagerrum 2")
item7 = Item("iPhone 7", 7, 499.95, "refurb iPhone 7 64gb carrier unlocked", 3, 1, "Lagerrum 2")
item8 = Item("iPhone 8", 8, 599.95, "refurb iPhone 8 64gb carrier unlocked", 7, 1, "Lagerrum 2")
item9 = Item("iPhone X", 9, 699.95, "refurb iPhone X 64gb carrier unlocked", 2, 2, "Lagerrum 2")
item10 = Item("iPhone XR", 10, 799.95, "refurb iPhone XR 64gb carrier unlocked", 4, 2, "Lagerrum 2")
item11 = Item("iPhone XS", 11, 899.95, "refurb iPhone XS 64gb carrier unlocked", 1, 2, "Lagerrum 2")
item12 = Item("iPhone 11", 12, 999.95, "refurb iPhone 11 64gb carrier unlocked", 7, 3, "Lagerrum 2")
item13 = Item("iPhone 12", 13, 1199.95, "refurb iPhone 12 64gb carrier unlocked", 6, 3, "Lagerrum 2")
item14 = Item("iPhone 13", 14, 1299.95, "refurb iPhone 13 64gb carrier unlocked", 5, 3, "Lagerrum 2")
item15 = Item("iPhone 14", 15, 10999.95, "iPhone 14 64gb carrier unlocked", 5, 3, "Lagerrum 2")


# input menu og valg af output
print ("Hvad har vi på lager? ")
inp = "0"
print("KATEGORI: ")
print("1. iPhone")
print("2. PC:Windows")
print("3. Peripherals")
inp = input("Vælg kategori: ")

if inp == "1":
    print("-iPhones-")
    print("1. Print enkelt produkt")
    print("2. Print alle produkter")
    inp = input("Vælg valgmulighed")

    if inp == "1":
        print("iPhones:")
        print("1. iPhone 6")
        print("2. iPhone 7")
        print("3. iPhone 8")
        print("4. iPhone X")
        print("5. iPhone XR")
        print("6. iPhone XS")
        print("7. iPhone 11")
        print("8. Phone 12")
        print("9. Phone 13")
        print("10.Phone 14")
        inp = input("Vælg produkt: ")
        if inp == "1":
            print(item6.__dict__)
            print(item6.pris_pr_stk())
            print(item6.pris_uden_moms())
            print(item6.total_price())
            print(item6.total_price_uden_moms())
        elif inp == "2":
            print(item7.__dict__)
            print(item7.pris_pr_stk())
            print(item7.pris_uden_moms())
            print(item7.total_price())
            print(item7.total_price_uden_moms())
        elif inp == "3":
            print(item8.__dict__)
            print(item8.pris_pr_stk())
            print(item8.pris_uden_moms())
            print(item8.total_price())
            print(item8.total_price_uden_moms())
        elif inp == "4":
            print(item9.__dict__)
            print(item9.pris_pr_stk())
            print(item9.pris_uden_moms())
            print(item9.total_price())
            print(item9.total_price_uden_moms())
        elif inp == "5":
            print(item10.__dict__)
            print(item10.pris_pr_stk())
            print(item10.pris_uden_moms())
            print(item10.total_price())
            print(item10.total_price_uden_moms())
        elif inp == "6":
            print(item11.__dict__)
            print(item11.pris_pr_stk())
            print(item11.pris_uden_moms())
            print(item11.total_price())
            print(item11.total_price_uden_moms())
        elif inp == "7":
            print(item12.__dict__)
            print(item12.pris_pr_stk())
            print(item12.pris_uden_moms())
            print(item12.total_price())
            print(item12.total_price_uden_moms())
        elif inp == "8":
            print(item13.__dict__)
            print(item13.pris_pr_stk())
            print(item13.pris_uden_moms())
            print(item13.total_price())
            print(item13.total_price_uden_moms())
        elif inp == "9":
            print(item14.__dict__)
            print(item14.pris_pr_stk())
            print(item14.pris_uden_moms())
            print(item14.total_price())
            print(item14.total_price_uden_moms())
        elif inp == "10":
            print(item15.__dict__)
            print(item15.pris_pr_stk())
            print(item15.pris_uden_moms())
            print(item15.total_price())
            print(item15.total_price_uden_moms())
    else:
        print("--------------------------------------------------------------------------------------------------")
        print(item6.__dict__)
        print(item6.pris_pr_stk())
        print(item6.pris_uden_moms())
        print(item6.total_price())
        print(item6.total_price_uden_moms())
        print("--------------------------------------------------------------------------------------------------")
        print(item7.__dict__)
        print(item7.pris_pr_stk())
        print(item7.pris_uden_moms())
        print(item7.total_price())
        print(item7.total_price_uden_moms())
        print("--------------------------------------------------------------------------------------------------")
        print(item8.__dict__)
        print(item8.pris_pr_stk())
        print(item8.pris_uden_moms())
        print(item8.total_price())
        print(item8.total_price_uden_moms())
        print("--------------------------------------------------------------------------------------------------")
        print(item9.__dict__)
        print(item9.pris_pr_stk())
        print(item9.pris_uden_moms())
        print(item9.total_price())
        print(item9.total_price_uden_moms())
        print("--------------------------------------------------------------------------------------------------")
        print(item10.__dict__)
        print(item10.pris_pr_stk())
        print(item10.pris_uden_moms())
        print(item10.total_price())
        print(item10.total_price_uden_moms())
        print("--------------------------------------------------------------------------------------------------")
        print(item11.__dict__)
        print(item11.pris_pr_stk())
        print(item11.pris_uden_moms())
        print(item11.total_price())
        print(item11.total_price_uden_moms())
        print("--------------------------------------------------------------------------------------------------")
        print(item12.__dict__)
        print(item12.pris_pr_stk())
        print(item12.pris_uden_moms())
        print(item12.total_price())
        print(item12.total_price_uden_moms())
        print("--------------------------------------------------------------------------------------------------")
        print(item13.__dict__)
        print(item13.pris_pr_stk())
        print(item13.pris_uden_moms())
        print(item13.total_price())
        print(item13.total_price_uden_moms())
        print("--------------------------------------------------------------------------------------------------")
        print(item14.__dict__)
        print(item14.pris_pr_stk())
        print(item14.pris_uden_moms())
        print(item14.total_price())
        print(item14.total_price_uden_moms())
        print("--------------------------------------------------------------------------------------------------")
        print(item15.__dict__)
        print(item15.pris_pr_stk())
        print(item15.pris_uden_moms())
        print(item15.total_price())
        print(item15.total_price_uden_moms())


elif inp == "2":
    print("WINDOWS PC: ")
    print("1. Print enkelt produkt")
    print("2. Print alle produkter")
    inp = input("Vælg valgmulighed")
    if inp == "1":
        print("Windows PC'er: ")
        print("1. Laptop")
        print("2. Desktop")
        inp = input("Vælg produkt: ")
        if inp == "1":
            print(item1.__dict__)
            print(item1.pris_pr_stk())
            print(item1.pris_uden_moms())
            print(item1.total_price())
            print(item1.total_price_uden_moms())
        elif inp == "2":
            print(item2.__dict__)
            print(item2.pris_pr_stk())
            print(item2.pris_uden_moms())
            print(item2.total_price())
            print(item2.total_price_uden_moms())

elif inp == "3":
    print("PERIPHERALS: ")
    print("1. Print enkelt produkt")
    print("2. Print alle produkter")
    inp = input("Vælg valgmulighed")
    if inp == "1":
        print("PERIPHERALS: ")
        print("1. Headset")
        print("2. Monitor")
        print("3. Mouse")
        inp = input("Vælg valgmulighed: ")
        if inp == "1":
            print(item3.__dict__)
            print(item3.pris_pr_stk())
            print(item3.pris_uden_moms())
            print(item3.total_price())
            print(item3.total_price_uden_moms())
        elif inp == "2":
            print(item5.__dict__)
            print(item5.pris_pr_stk())
            print(item5.pris_uden_moms())
            print(item5.total_price())
            print(item5.total_price_uden_moms())
        elif inp == "3":
            print(item4.__dict__)
            print(item4.pris_pr_stk())
            print(item4.pris_uden_moms())
            print(item4.total_price())
            print(item4.total_price_uden_moms())

    elif inp == "2":
        print(item3.__dict__)
        print(item3.pris_pr_stk())
        print(item3.pris_uden_moms())
        print(item3.total_price())
        print(item3.total_price_uden_moms())

        print(item4.__dict__)
        print(item4.pris_pr_stk())
        print(item4.pris_uden_moms())
        print(item4.total_price())
        print(item4.total_price_uden_moms())

        print(item5.__dict__)
        print(item5.pris_pr_stk())
        print(item5.pris_uden_moms())
        print(item5.total_price())
        print(item5.total_price_uden_moms())



