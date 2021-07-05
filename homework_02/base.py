from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 1000
    started = False
    fuel = 100
    fuel_consumption = 10

    def __init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __repr__(self):
        return f"{self.weight}, {self.started}, {self.fuel}, {self.fuel_consumption}"

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        max_distance = self.fuel / self.fuel_consumption
        if distance <= max_distance:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel
