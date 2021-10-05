import click
import subprocess

def getCommandOutput(commandArray, suppressErrors=True):
    process = subprocess.Popen(commandArray, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.communicate()
    returnCode = process.returncode
    stdout = output[0].decode("UTF-8")
    stderr = output[1].decode("UTF-8")
    if suppressErrors:
        return stdout
    else:
        return stdout, stderr, returnCode

def runShellScript(commandArray):
    subprocess.Popen(commandArray)

@click.group()
def cli():
    pass

@click.command()
def init():
    """Initialization of the DB and required configurations"""
    click.echo(f"Initialization...")
    runShellScript(["./initScript.sh"])

@click.command()
@click.option("--destination", help="Destination path for the backup.")
def backup(destination):
    """Backup the existing DB, data and configurations to a given DESTINATION"""
    click.echo(f"Backup to {destination}")
    runShellScript(["./backupScript.sh"])

@click.command()
@click.option("--version", default="1.0", help="Target version for the upgrade.")
def upgrade(version):
    """Upgrade an existing ELN installation to a desired VERSION"""
    click.echo(f"Upgrading to version {version}")
    runShellScript(["./upgradeScript.sh"])
    
@click.command()
def startEln():
    """Start ELN"""
    click.echo(f"Start ELN...")
    runShellScript(["./startELNscript.sh"])
    
@click.command()
def startWorker():
    """Start worker"""
    click.echo(f"Start worker...")
    runShellScript(["./startWorkerScript.sh"])
    
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
    uname = getCommandOutput(['uname', '-a'])
    ubuntuRelease = getCommandOutput(['lsb_release', '-r'])
    numberCores, errorInfo, returnCode = getCommandOutput(['nproc', '--all'], False)
    click.echo(f"System: {uname}")
    click.echo(f"Ubuntu {ubuntuRelease}")
    click.echo(f"Number cores: {numberCores}")
    click.echo(f"Error info of nproc --all: {errorInfo}\n")
    click.echo(f"Return code of nproc --all: {returnCode}")

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
