from dataclasses import dataclass


@dataclass
class Config:
    num_samples: int = 1000000


def hello() -> str:
    print("inside hello!")
    return "hello"


def stringify_the_float(value: float) -> str:
    return f"{int(value):d} dot {int((value-int(value))*100):d}"
