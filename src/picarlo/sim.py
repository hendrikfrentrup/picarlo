from dataclasses import dataclass


@dataclass
class Config:
    num_samples: int = 1000000


def hello() -> str:
    print("inside hello!")
    return "hello"
