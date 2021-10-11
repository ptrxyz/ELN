import click
from click.utils import echo
import yaml

@click.group()
def cli():
    pass

@click.command()
@click.option("--prefix", default="", help="string prefix for imported strings")
@click.option("--upper", is_flag=True, default=False, help="returned keywords should be uppercase letters")
@click.argument("file", nargs=1)
@click.argument("keywords", nargs=1)
def read(prefix, upper, file, keywords):
    """Read entries from a YML file and add the given PREFIX"""
    stream = open(file, "r")
    fileContent = yaml.safe_load(stream)
    for keyword in keywords.split("."):
        if fileContent.get(keyword):
            fileContent = fileContent[keyword]

    if type(fileContent) is dict:
        for item in fileContent:
            if type(item) is str:
                if upper:
                    click.echo(prefix + item.upper())
                else:
                    click.echo(prefix + item)

    else:
        if upper:
            click.echo(prefix + fileContent.upper())
        else:
            click.echo(prefix + fileContent)

cli.add_command(read)

if __name__ == '__main__':
    cli()
