"""Command-line interface."""
import click


@click.command()
@click.version_option()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def main(count: int, name: str) -> str:
    """Python Test Project."""
    for x in range(count):
        click.echo(f"Hello {name}")
    return f"{count*name}"


if __name__ == "__main__":
    main(prog_name="python-test-project")  # pragma: no cover
