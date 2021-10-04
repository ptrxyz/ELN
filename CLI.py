import click
import subprocess

@click.group()
def cli():
    pass

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")

def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

@click.command()
def init():
    """Initialization of the DB and required configurations"""
    click.echo(f"Initialization...")

@click.command()
@click.option("--destination", help="Destination path for the backup.")
def backup(destination):
    """Backup the existing DB, data and configurations to a given DESTINATION"""
    click.echo(f"Backup to {destination}")

@click.command()
@click.option("--version", default="1.0", help="Target version for the upgrade.")
def upgrade(version):
    """Upgrade an existing ELN installation to a desired VERSION"""
    click.echo(f"Upgrading to version {version}")
    
@click.command()
def startEln():
    """Start ELN"""
    click.echo(f"Start ELN...")
    
@click.command()
def startWorker():
    """Start worker"""
    click.echo(f"Start worker...")
    
@click.command()
def shell():
    """Open a root shell"""
    click.echo(f"Root shell...")
    
@click.command()
def userShell():
    """Open a user shell"""
    click.echo(f"User shell...")
    
@click.command()
def info():
    """Display information about the existing installation"""
    click.echo(f"Info...")
    subprocess.Popen(['uname', '-a'])

cli.add_command(hello)
cli.add_command(init)
cli.add_command(backup)
cli.add_command(upgrade)
cli.add_command(startEln)
cli.add_command(startWorker)
cli.add_command(shell)
cli.add_command(userShell)
cli.add_command(info)

if __name__ == '__main__':
    cli()
