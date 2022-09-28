import csv

class Item:

        uden_moms = 1.25 #hvad et beløb inkl mom skal ganges med for at finde prisen uden moms
        def __init__(self, navn:str, id:int, pris:float, beskrivelse:str, antal:int, hylde:int, plads:str, ):

            # bekræft at der er indtastet gyldige argumenter
            assert pris >= 0, f"Pris {pris} er ikke større en 0!"
            assert antal >= 0, f"Antal {antal} er ikke større en 0!"

            #Assign til self object
            self.navn = navn
            self.id = id
            self.pris = pris
            self.beskrivelse = beskrivelse
            self.antal = antal
            self.hylde = hylde
            self.plads = plads

        def udregn_pris(self):
            return self.pris * self.antal

        def pris_uden_moms(self):
            self.pris = self.pris / Item.uden_moms



item1 = Item("Laptop", 1, 799.99, "Arbejds bærbar", 7, 2, "Lagerrum 1")
#item1.pris_uden_moms()
item2 = Item("Desktop", 2, 1499.95, "i7 4790k, 32 gb 3600 mhz, gtx 1660 ", 4, 1, "Lagerrum 1")
item3 = Item("Headset", 3, 699.95, "SENNHEISER HD 350", 8, 4, "Lagerrum 1")
item4 = Item("Mouse", 4, 499.95, "Logitech G Pro wireless", 11, 4, "Lagerrum 1")
item5 = Item("Monitor", 5, 1995.95, "ASUS VG258QR", 6, 4, "Lagerrum 1")
item6 = Item("iPhone 6", 6, 399.95, "refurb iPhone 6 64gb carrier unlocked", 4, 1, "Lagerrum 2")
item7 = Item("iPhone 7", 7, 499.95, "refurb iPhone 7 64gb carrier unlocked", 9, 2, "Lagerrum 2")


