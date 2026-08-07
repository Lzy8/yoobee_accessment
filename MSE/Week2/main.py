class HumanMeasurements:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height ** 2)

person1 = HumanMeasurements(1.75, 70) 
print("Person 1 BMI:", person1.bmi())  
