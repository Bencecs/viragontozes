import time
import random

class Ontozorendszer:
    def __init__(self, nedvesseg_kuszob=30):
        self.nedvesseg_kuszob = nedvesseg_kuszob  # százalékban
        self.nedvesseg = random.randint(20, 80)
        self.ontozo_bekapcsolva = False

    def mer_nedvesseg(self):
        # Véletlenszerűen csökken a nedvesség, mintha száradna a talaj
        self.nedvesseg -= random.uniform(0.5, 2.5)
        if self.nedvesseg < 0:
            self.nedvesseg = 0
        return round(self.nedvesseg, 2)

    def ontoz(self):
        print("💧 Öntözés elindítva...")
        self.ontozo_bekapcsolva = True
        for i in range(5):
            self.nedvesseg += random.uniform(3.0, 6.0)
            print(f"   ➤ Öntözés folyamatban... Nedvesség: {round(self.nedvesseg, 2)}%")
            time.sleep(1)
        self.ontozo_bekapcsolva = False
        print("✅ Öntözés leállítva.")

    def futtat(self, ciklusok=10):
        print("🌿 Automata öntözőrendszer elindítva...\n")
        for i in range(ciklusok):
            aktualis_nedvesseg = self.mer_nedvesseg()
            print(f"[{i+1}. ciklus] Talaj nedvessége: {aktualis_nedvesseg}%")
            if aktualis_nedvesseg < self.nedvesseg_kuszob:
                print("⚠️  Alacsony nedvességszint! Öntözés szükséges.")
                self.ontoz()
            else:
                print("✅ A talaj elég nedves, nincs szükség öntözésre.")
            print("-" * 40)
            time.sleep(2)
        print("\n🌱 Öntözőrendszer leállítva.")

# Fő program
if __name__ == "__main__":
    ontozorendszer = Ontozorendszer(nedvesseg_kuszob=35)
    ontozorendszer.futtat(ciklusok=8)
