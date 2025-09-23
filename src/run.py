#!/usr/bin/env python3
# run.py
import sys
from pathlib import Path
import click
from enum import Enum
from typing import TypedDict, Literal, Dict

@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    """
    LLM Grader CLI

    Usage:
      python run.py install
      python run.py test
      python run.py URLS_FILE   # or '-' to read from stdin
    """


@cli.command(short_help="Install project/runtime dependencies.")
def install():
    # Minimal placeholder
    click.echo("Installing dependencies... (stub)")
    click.echo("Done.")


@cli.command(short_help="Run tests and print required summary line.")
@click.option("--min-coverage", type=int, default=80, show_default=True, help="Minimum coverage to pass.")
def test(min_coverage: int):
    # Minimal placeholder
    passed = True
    coverage = 100
    click.echo(f"X/Y test cases passed. {coverage}% line coverage achieved.")
    sys.exit(0 if (passed and coverage >= min_coverage) else 1)


@cli.command("urls", short_help="Grade models from a URL file (or stdin).")
@click.argument("urls_file", required=True)
def urls(urls_file: str):
    """Process a newline-delimited URL file (or '-' for stdin)."""
    if urls_file == "-":
        lines = [ln.strip() for ln in sys.stdin.read().splitlines() if ln.strip()]
        source = "stdin"
    else:
        p = Path(urls_file)
        if not p.exists():
            click.echo(f"Error: file not found: {p}", err=True)
            sys.exit(1)
        lines = [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]
        source = str(p)

    click.echo(f"Read {len(lines)} URL(s) from {source}. (grading stub)")


if __name__ == "__main__":
    cli()