import multiprocessing

import typer

from picarlo.sim import (
    monte_carlo_pi,
    monte_carlo_pi_parallel,
    monte_carlo_pi_python,
)

app = typer.Typer(help="Monte Carlo π estimator")


@app.command()
def run(
    iterations: int = typer.Option(
        10_000, "--iterations", "-i", help="Samples per process"
    ),
    cores: int = typer.Option(
        1, "--cores", "-c", help="Number of processes (defaults to CPU count)"
    ),
    parallel: bool = typer.Option(
        False,
        "--parallel/--no-parallel",
        "-p",
        help="Use multiprocessing (defaults to CPU count)",
    ),
    use_python: bool = typer.Option(
        False, "--use-python", help="Force use of Python implementation"
    ),
):
    if parallel is True:
        cores = multiprocessing.cpu_count()

    worker = monte_carlo_pi_python if use_python else monte_carlo_pi

    if cores > 1:
        pi = monte_carlo_pi_parallel(iterations, cores, worker=worker)
    else:
        pi = worker(iterations)

    typer.echo(f"π ≈ {pi}")


def main():
    app()


if __name__ == "__main__":
    main()
