from picarlo.sim import Config


def main():
    config = Config()
    print(f"starting pi carlo with {config.num_samples} samples!")


if __name__ == "__main__":
    main()
