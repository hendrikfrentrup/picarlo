# calculating pi with modern tooling

We need a few things:
1. a CLI tool to specify the number of iterations and the number of cores it runs on:
`picarlo --cores 4 --iterations 10000`


## basic tooling setup (runs on each commit) 
1. `uv self update` & `uv sync`
2. linting/format checking: `uv run ruff check`
3. auto-formatting: `uv run ruff format`
4. type checking: `uv run pyright`
5. testing: `uv run pytest`
6. integrate into pre-commit

## required 
1. split between dev and prod dependencies: `uv add --dev`
2. add a build system, hatchling in [pyproject.toml](pyproject.toml)
3. run a build `uv build`
4. try maturing build backend

## useful stuff
1. create docstrings via LLM
2. create docs from docstrings
3. calculate test coverage

## release preparation
1. generate changelog from commit messages
2. update version indicator
3. build package/wheel
4. publish assets

# [vscode extensions](.vscode/extensions.json)
1. Ruff