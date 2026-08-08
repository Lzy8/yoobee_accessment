import optimaztion
class HumanMeasurements:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height ** 2)

def main():
    person2 = HumanMeasurements(1.823242, 80)  
    print("Person 2 BMI:{0},heigt:{1:.2f}".format(person2.bmi(), person2.height))
    print("__name__:", __name__)
    # optimaztion.main()  # Call the main function from test.py

if __name__ == "__main__":
    main()      