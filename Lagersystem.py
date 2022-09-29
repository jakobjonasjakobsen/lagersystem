import time





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
        print("Samlet pris af lager: ")
        return self.pris * self.antal

    def pris_uden_moms(self):
        print("Pris pr stk uden moms: ")
        return self.pris / 1.25

    def total_price_uden_moms(self):
        print("Samlet pris af lager uden moms: ")
        return self.pris / 1.25 * self.antal



# assign parametre til __init__

liste_af_varer = []
liste_af_varer.append(Item("Laptop", 1, 799.99, "i5 16gb 3200 mHz gtx 1660", 7, 2, "Lagerrum 1"))
liste_af_varer.append(Item("Desktop", 2, 1499.95, "i7 4790k, 32 gb 3600 mhz, gtx 1660 ", 4, 1, "Lagerrum 1"))
liste_af_varer.append(Item("Headset", 3, 699.95, "SENNHEISER HD 350", 8, 4, "Lagerrum 1"))
liste_af_varer.append(Item("Mouse", 4, 499.95, "Logitech G Pro wireless", 11, 4, "Lagerrum 1"))
liste_af_varer.append(Item("Monitor", 5, 1995.95, "ASUS VG258QR", 6, 4, "Lagerrum 1"))
liste_af_varer.append(Item("iPhone 6", 6, 399.95, "refurb iPhone 6 64gb carrier unlocked", 4, 1, "Lagerrum 2"))
liste_af_varer.append(Item("iPhone 7", 7, 499.95, "refurb iPhone 7 64gb carrier unlocked", 3, 1, "Lagerrum 2"))
liste_af_varer.append(Item("iPhone 8", 8, 599.95, "refurb iPhone 8 64gb carrier unlocked", 7, 1, "Lagerrum 2"))
liste_af_varer.append(Item("iPhone X", 9, 699.95, "refurb iPhone X 64gb carrier unlocked", 2, 2, "Lagerrum 2"))
liste_af_varer.append(Item("iPhone XR", 10, 799.95, "refurb iPhone XR 64gb carrier unlocked", 4, 2, "Lagerrum 2"))
liste_af_varer.append(Item("iPhone XS", 11, 899.95, "refurb iPhone XS 64gb carrier unlocked", 1, 2, "Lagerrum 2"))
liste_af_varer.append(Item("iPhone 11", 12, 999.95, "refurb iPhone 11 64gb carrier unlocked", 7, 3, "Lagerrum 2"))
liste_af_varer.append(Item("iPhone 12", 13, 1199.95, "refurb iPhone 12 64gb carrier unlocked", 6, 3, "Lagerrum 2"))
liste_af_varer.append(Item("iPhone 13", 14, 1299.95, "refurb iPhone 13 64gb carrier unlocked", 5, 3, "Lagerrum 2"))
liste_af_varer.append(Item("iPhone 14", 15, 10999.95, "iPhone 14 64gb carrier unlocked", 5, 3, "Lagerrum 2"))


def udskriv(index):
    print(liste_af_varer[int(index)].__dict__)
    print(liste_af_varer[int(index)].pris_pr_stk())
    print(liste_af_varer[int(index)].pris_uden_moms())
    print(liste_af_varer[int(index)].total_price())
    print(liste_af_varer[int(index)].total_price_uden_moms())


# input menu og valg af output
print("Hvad har vi på lager? ")
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
        inp = int(inp)
        index = 4 + inp

        udskriv(index)
    else:
        index = "5"
        index = int(index)
        for vare in liste_af_varer:
            udskriv(index)
            index = 1 + index


elif inp == "2":
    print("Windows PC'er: ")
    print("1. Laptop")
    print("2. Desktop")
    index = input("Vælg produkt: ")
    index = int(index)
    index = index - 1
    udskriv(index)



elif inp == "3":
    print("PERIPHERALS CATEGORY: ")
    print("1. Print enkelt produkt")
    print("2. Print alle produkter")
    inp = input("Vælg valgmulighed")
    if inp == "1":
        print("PERIPHERALS: ")
        print("1. Headset")
        print("2. Mouse")
        print("3. Monitor")
        index = input("Vælg valgmulighed: ")
        index = int(index)
        index = 1 + index
        udskriv(index)

    elif inp == "2":
        index = 2
        index = int(index)
        for vare in liste_af_varer:
            if index < 5:
                udskriv(index)
                index = 1 + index