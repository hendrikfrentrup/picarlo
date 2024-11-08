from picarlo.sim import Config, stringify_the_float


def main() -> None:
    config = Config()

    stringify_the_float(config.num_samples)

    print(f"starting pi carlo with {config.num_samples} samples!")


if __name__ == "__main__":
    main()
