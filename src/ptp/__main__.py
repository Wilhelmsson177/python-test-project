"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Python Test Project."""


if __name__ == "__main__":
    main(prog_name="python-test-project")  # pragma: no cover
