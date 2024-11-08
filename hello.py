from dataclasses import dataclass


@dataclass
class Config:
    num_samples: int = 1000


def main():
    config = Config()
    print(f"starting pi carlo with {config.num_samples} samples!")


if __name__ == "__main__":
    main()
