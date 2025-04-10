import time

class Garden:
    def __init__(self, soil_moisture=50, water_level=100):
        self.soil_moisture = soil_moisture         
    def check_soil_moisture(self):
        """A talaj nedvességének ellenőrzése"""
        if self.soil_moisture < 30:
            print("A talaj túl száraz, szükséges az öntözés!")
            return False
        else:
            print("A talaj megfelelően nedves.")
            return True

    def water_plants(self):
        """Öntözés elindítása"""
        if self.water_level > 0:
            print("Öntözés folyamatban...")
            self.soil_moisture += 30  
            self.water_level -= 10  
            print(f"Az öntözés befejeződött. Talaj nedvessége: {self.soil_moisture}%")
            print(f"Vízszint: {self.water_level}%")
        else:
            print("Nincs elég víz az öntözéshez!")

    def simulate_day(self):
        """A nap szimulációja: a talaj nedvessége csökkenhet, és a vízszint is"""
        self.soil_moisture -= 10 
        self.water_level -= 5 

        print("\nMa:")
        print(f"Talaj nedvessége: {self.soil_moisture}%")
        print(f"Vízszint: {self.water_level}%")

        if not self.check_soil_moisture():
            self.water_plants()



def main():
    garden = Garden() 
    days = 5 

    for day in range(1, days + 1):
        print(f"\nNap {day}")
        garden.simulate_day()
        time.sleep(1)  

    print
