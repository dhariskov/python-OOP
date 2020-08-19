from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor

from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply

class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []
        
    @property
    def food(self):
        result = [each for each in self.supplies if each.__class__.__name__ == "FoodSupply"]
        if result:
            return result
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        result = [each for each in self.supplies if each.__class__.__name__ == "WaterSupply"]
        if result:
            return result
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        result = [each for each in self.medicine if each.__class__.__name__ == "Painkiller"]
        if result:
            return result
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        result = [each for each in self.medicine if each.__class__.__name__ == "Salve"]
        if result:
            return result
        raise IndexError("There are no salves left!")

    def add_survivor(self, survivor: Survivor):
        if [s for s in self.survivors if s.name == survivor.name]:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            medicines = [each for each in self.medicine if each.__class__.__name__ == medicine_type]
            if medicines:
                removed_medicine = medicines.pop()
                self.medicine.remove(removed_medicine)
                removed_medicine.apply(survivor)
                return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            sustenance = [each for each in self.supplies if each.__class__.__name__ == sustenance_type]
            if sustenance:
                removed_supply = sustenance.pop()
                self.supplies.remove(removed_supply)
                removed_supply.apply(survivor)
                return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for each in self.survivors:
            each.needs -= each.age*2

        for each in self.survivors:
            self.sustain(each, "FoodSupply")
            self.sustain(each, "WaterSupply")

# painkiller = Painkiller()
# salve = Salve()
# surv = Survivor("Test", 12)
# surv.health -= 10
# bunker = Bunker()
#
# bunker.add_medicine(painkiller)
# bunker.add_medicine(salve)
# bunker.add_survivor(surv)
# bunker.heal(surv, "Painkiller")