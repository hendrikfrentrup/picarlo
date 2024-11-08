from picarlo.sim import Config


def test_config():
    config = Config()
    assert config.num_samples == 1000000
