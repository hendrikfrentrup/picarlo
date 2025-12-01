import multiprocessing

import typer

from picarlo.sim import monte_carlo_pi, monte_carlo_pi_parallel

app = typer.Typer(help="Monte Carlo π estimator")


@app.command()
def run(
    iterations: int = typer.Option(
        10_000, "--iterations", "-i", help="Samples per process"
    ),
    cores: int = typer.Option(
        None, "--cores", "-c", help="Number of processes (defaults to CPU count)"
    ),
    parallel: bool = typer.Option(
        True, "--parallel/--no-parallel", help="Use multiprocessing"
    ),
):
    if cores is None:
        cores = multiprocessing.cpu_count()

    if parallel and cores > 1:
        pi = monte_carlo_pi_parallel(iterations, cores)
    else:
        pi = monte_carlo_pi(iterations)

    typer.echo(f"π ≈ {pi}")


def main():
    app()


if __name__ == "__main__":
    main()
