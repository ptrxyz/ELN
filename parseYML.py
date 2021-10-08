import click
import yaml

@click.group()
def cli():
    pass

@click.command()
@click.option("--prefix", default="DB_", help="string prefix for imported strings")
@click.argument("file", nargs=1)
def read(prefix, file):
    """Read entries from a YML file and add the given PREFIX"""
    click.echo(f"Reading file {file}")
    click.echo(f"Adding prefix {prefix}")
    stream = open(file, "r")
    fileContent = yaml.load(stream)
    click.echo(fileContent)

cli.add_command(read)

if __name__ == '__main__':
    cli()
