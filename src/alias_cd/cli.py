"""This module defines the CLI for alias_cd."""

import os

import typer

import alias_cd
from alias_cd import config

app = typer.Typer()
CONFIG = None
DEFAULT_LABEL = "<DEFAULT>"


@app.command()
def get(name: str):
    """Display the directory for the given directory."""

    if name in CONFIG.aliases:
        typer.echo(os.path.expanduser(CONFIG.aliases[name]))
    else:
        typer.secho(f"alias {name} not found", fg=typer.colors.RED, err=True)
        exit(-1)


@app.command()
def version():
    """Display the version of the CLI."""

    typer.echo(alias_cd.__version__)


@app.command()
def list():
    """Display all stored aliases."""

    typer.echo(CONFIG.aliases)
    padding_size = max(
        max(
            [
                len(alias) if alias is not None else len(DEFAULT_LABEL)
                for alias in CONFIG.aliases
            ]
        ),
        5,
    )
    typer.echo(f"{'Alias':{padding_size}} | Directory")
    for alias, directory in CONFIG.aliases.items():
        if alias is None:
            alias = DEFAULT_LABEL
        typer.echo(f"{alias:{padding_size}} | {directory}")


@app.command()
def validate():
    """Check that all aliases are valid."""

    exit_status = 0

    for alias, directory in CONFIG.aliases.items():
        if not os.path.exists(directory):
            exit_status = -1
            typer.secho(
                f"invalid {alias=} {directory=} does not exist.",
                fg=typer.colors.RED,
                err=True,
            )

    exit(exit_status)


@app.callback()
def _global_init(config_path: str = None):

    try:
        global CONFIG
        CONFIG = config._load_config(config_path)
    except ValueError as err:
        typer.secho(err, fg=typer.colors.RED, err=True)
        exit(-1)


if __name__ == "__main__":
    app()
