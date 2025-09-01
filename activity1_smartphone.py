# Base class Smartphone
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # private attribute

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery: {self.__battery}%")
    
    def charge_battery(self, amount):
        self.__battery += amount
        if self.__battery > 100:
            self.__battery = 100
        print(f"Battery charged to {self.__battery}%")

# Inheritance
class SmartphoneGaming(Smartphone):
    def __init__(self, brand, model, battery, gpu):
        super().__init__(brand, model, battery)
        self.gpu = gpu

    def show_info(self):
        super().show_info()
        print(f"GPU: {self.gpu}")

# Test classes
if __name__ == "__main__":
    s1 = Smartphone("Samsung", "Galaxy S23", 80)
    s1.show_info()
    s1.charge_battery(15)

    s2 = SmartphoneGaming("Asus", "ROG Phone 6", 50, "Adreno 730")
    s2.show_info()
