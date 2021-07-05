"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 2500

    def __init__(self, weight=Vehicle.weight, fuel=Vehicle.fuel, fuel_consumption=Vehicle.fuel_consumption,
                 max_cargo=max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def __repr__(self):
        return f"{self.weight}, {self.started}, {self.fuel}, {self.fuel_consumption}, {self.cargo}, {self.max_cargo}"

    def load_cargo(self, value):
        new_cargo = self.cargo + value
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
            print(self.cargo)
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
