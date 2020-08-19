from project.medicine.medicine import Medicine


class Salve(Medicine):
    def __init__(self, health_increase=50):
        Medicine.__init__(self, health_increase)
