import functools
import multiprocessing
import random
import time
from dataclasses import dataclass

from loguru import logger


def monte_carlo_pi_python(num_samples: int) -> float:
    """
    Estimate the value of Pi using the Monte Carlo method (Python implementation).

    This function generates random points within a unit square and counts how many fall within the unit circle.
    The ratio of points inside the circle to the total number of points is used to estimate Pi.

    Args:
        num_samples (int): The number of random points to generate.

    Returns:
        float: The estimated value of Pi.

    Logs:
        The runtime of the function in seconds.
    """  # noqa: E501
    in_circle_count = 0
    in_square_count = 0

    for _ in range(num_samples):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            in_circle_count += 1
        in_square_count += 1

    return 4 * in_circle_count / in_square_count


try:
    from picarlo._picarlo_rust import monte_carlo_pi as _monte_carlo_pi_rust
except ImportError:
    logger.warning("Falling back to Python implementation.")
    _monte_carlo_pi_rust = None


# 2. Define the public function explicitly (picklable)
def monte_carlo_pi(num_samples: int, force_python: bool = False) -> float:
    """
    Estimate Pi using the available backend (Rust or Python).
    """
    start = time.time()

    # Use Rust if available AND not forced to use Python
    if _monte_carlo_pi_rust and not force_python:
        result = _monte_carlo_pi_rust(num_samples)
    else:
        result = monte_carlo_pi_python(num_samples)

    end = time.time()
    logger.info(f"Runtime: {end - start:.2f} seconds")
    return result


def monte_carlo_pi_parallel(
    num_samples: int, num_proc: int, force_python: bool = False
) -> float:
    """
    Estimate the value of Pi using the Monte Carlo method in parallel.

    This function divides the task of estimating Pi into multiple processes
    to take advantage of multiple CPU cores, thereby speeding up the computation.

    Args:
        num_samples (int): The number of random samples to generate in each process.
        num_proc (int): The number of processes to use for parallel computation.
        worker (callable, optional): The function to use for estimation.
                                     Defaults to monte_carlo_pi.

    Returns:
        float: The estimated value of Pi.
    """
    # TODO: get # of core and other info about mutliprocessing
    num_cores = multiprocessing.cpu_count()

    logger.info(
        f"# of avail. cores: {num_cores} | {num_proc} procs spawned.",
    )

    # Prepare the worker with the frozen argument
    worker = functools.partial(monte_carlo_pi, force_python=force_python)

    pool = multiprocessing.Pool(processes=num_proc)
    # map passes the iterable items as the first argument to 'worker'
    results = pool.map(worker, [num_samples] * num_proc)
    pool.close()
    pool.join()

    return sum(results) / num_proc


@dataclass
class Config:
    """
    Configuration class for simulation parameters.

    Attributes:
        num_samples (int): The number of samples to be used in the simulation.
        Default is 10,000,000.
    """

    num_samples: int = 10000000


def hello() -> str:
    print("inside hello!")
    return "hello"


def goodbye() -> str:
    print("inside goodbye!")
    return "goodbye"


def stringify_the_float(value: float) -> str:
    return f"{int(value):d} dot {int((value-int(value))*100):d}"
