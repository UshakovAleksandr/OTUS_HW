"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine


class Car(Vehicle):
    engine = False

    def __init__(self, weight=1000, fuel=100, fuel_consumption=10):
        super().__init__(weight, fuel, fuel_consumption)

    def __repr__(self):
        return f"{self.weight}, {self.started}, {self.fuel}, {self.fuel_consumption}, {self.engine}"

    def set_engine(self, engine):
        self.engine = engine


car1 = Car()
print(car1)
car1.set_engine(engine=Engine(3.2, 6))
print(car1)
print(isinstance(car1, Vehicle))
