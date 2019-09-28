from tire import Tire, SnowTire


class Car:
    """
    Docstring describing the class
    """

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A car with an {self.engine} engine, and {self.tires} tires")

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return


tire = Tire('P', 205, 65, 15)
snowTire = SnowTire('P', 65, 3, 15, 15)
tires = [snowTire, snowTire, snowTire, snowTire]
civic = Car('4-cylinder', tires=tires)
print(civic.description())
