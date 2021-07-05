"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    volume: float
    pistons: int


engine_1 = Engine(3.2, 6)
