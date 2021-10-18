import click
import subprocess
import pty
import psutil

def getCommandOutput(commandArray, suppressErrors=True):
    try:
        process = subprocess.Popen(commandArray, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        output = process.communicate()
        returnCode = process.returncode
        stdout = output[0].decode("UTF-8")
        stderr = output[1].decode("UTF-8")
        if suppressErrors:
            return stdout
        else:
            return stdout, stderr, returnCode

    except OSError as e:
        print(e.filename)
        if suppressErrors:
            return "-\n"
        else:
            return "-\n","-\n","-\”"

def runShellScript(commandArray):
    subprocess.call(commandArray)

def getUbuntuVersion():
    ubuntuRelease = ""
    for line in open("/etc/lsb-release"):
        line = line.strip()
        var, arg = line.split('=', 1)
        if var.startswith('DISTRIB_RELEASE'):
            ubuntuRelease = arg

    return ubuntuRelease

@click.group()
def cli():
    """Command line interface of the ELN Docker image"""
    pass

@click.command()
def init():
    """Initialization of the DB and required configurations"""
    click.echo(f"Initialization...")
    runShellScript(["/etc/scripts/initScript.sh"])

@click.group()
def landscape():
    """Manage configuration landscapes for the ELN"""
    pass

@landscape.command()
@click.option("--name", default="default", help="Name of an existing landscape in /share/landscapes/")
@click.option("--nodefault/--default", help="Should the deployed landscape be based on the default")
def deploy(name, nodefault):
    """Establish a configuration landscape for the ELN"""
    click.echo(f"Deploy landscape: {name}")
    if nodefault:
        runShellScript(["/etc/scripts/landscapeScript.sh", name, "nodefault"])
    else:
        runShellScript(["/etc/scripts/landscapeScript.sh", name, "default"])

@click.command()
@click.option("--destination", help="Destination path for the backup.")
def backup(destination):
    """Backup the existing DB, data and configurations to a given DESTINATION"""
    click.echo(f"Backup to {destination}")
    runShellScript(["/etc/scripts/backupScript.sh"])

@click.command()
@click.option("--version", default="1.0", help="Target version for the upgrade.")
def upgrade(version):
    """Upgrade an existing ELN installation to a desired VERSION"""
    click.echo(f"Upgrading to version {version}")
    runShellScript(["/etc/scripts/upgradeScript.sh"])
    
@click.command()
def startEln():
    """Start ELN"""
    click.echo(f"Start ELN...")
    runShellScript(["/etc/scripts/startELNscript.sh"])
    
@click.command()
def startWorker():
    """Start worker"""
    click.echo(f"Start worker...")
    runShellScript(["/etc/scripts/startWorkerScript.sh"])
    
@click.command()
def shell():
    """Open a root shell"""
    click.echo(f"Root shell...")
    pty.spawn("/bin/bash")
    
@click.command()
def userShell():
    """Open a user shell"""
    click.echo(f"User shell...")
 #   pty.spawn("sudo -E -H -u ${PROD} bash -c '. $HOME/.profile; ' /bin/bash")
    
@click.command()
def info():
    """Display information about the existing installation"""
    uname = getCommandOutput(['uname', '-a'])
    ubuntuRelease = getUbuntuVersion()
    click.echo(f"System: {uname}")
    click.echo(f"Ubuntu {ubuntuRelease}")
 
    click.echo(f"Number CPU cores: {psutil.cpu_count()}")
 
    memory = psutil.virtual_memory()
    click.echo(f"Memory:")
    click.echo(f"    total: {psutil._common.bytes2human(memory.total)}")
    click.echo(f"    available: {psutil._common.bytes2human(memory.available)}")
    click.echo(f"Storage:")
 
    storageRoot = psutil.disk_usage("/")
    click.echo(f"    /:")
    click.echo(f"        total: {psutil._common.bytes2human(storageRoot.total)}")
    click.echo(f"        available: {psutil._common.bytes2human(storageRoot.free)}")
    storageShared = psutil.disk_usage("/shared")
    click.echo(f"    /shared:")
    click.echo(f"        total: {psutil._common.bytes2human(storageShared.total)}")
    click.echo(f"        available: {psutil._common.bytes2human(storageShared.free)}")

    click.echo(f"Used program versions:")
    rubyVersion = getCommandOutput(['ruby','--version'])
    click.echo(f"    Ruby version: {rubyVersion}")
    passengerVersion = getCommandOutput(['passenger','--version'])
    click.echo(f"    Passenger version: {passengerVersion}")
    nodeVersion = getCommandOutput(['node','--version'])
    click.echo(f"    Node version: {nodeVersion}")
    npmVersion = getCommandOutput(['npm','-v'])
    click.echo(f"    NPM version: {npmVersion}")
    chemotionVersion = "-"
    bundlerVersion = getCommandOutput(['bundler','--version'])
    click.echo(f"    Bundler version: {bundlerVersion}")
    pandocVersion = getCommandOutput(['pandoc','--version']).partition('\n')[0]
    click.echo(f"    Pandoc version: {pandocVersion} \n")
    click.echo(f"    Chemotion version: {chemotionVersion} \n")


cli.add_command(init)
cli.add_command(landscape)
cli.add_command(backup)
cli.add_command(upgrade)
cli.add_command(startEln)
cli.add_command(startWorker)
cli.add_command(shell)
cli.add_command(userShell)
cli.add_command(info)

if __name__ == '__main__':
    cli()
