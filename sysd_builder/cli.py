import click
from sysd_builder.builder import SysdService


@click.command()
@click.option("--name", help="Service name")
@click.option("--cmd", help="Command to run - quote in strings w/ args")
@click.option("--service-type", help="Service type, simple|oneshot")
def sdb_cli(name: str, cmd: str, service_type: str):
    """SDB Cli"""
    sysd_service = SysdService(name=name, cmd=cmd, service_type=service_type)
    sysd_service.install()
