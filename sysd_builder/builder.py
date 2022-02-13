from dataclasses import dataclass
from getpass import getuser

from jinja2 import Environment, PackageLoader, select_autoescape
from plumbum import local


@dataclass
class SysdService:
    """Describes a single systemd service"""

    name: str
    cmd: str
    service_type: str
    jinja_env = Environment(
        loader=PackageLoader(__package__, "templates"),
        autoescape=select_autoescape(),
    )
    shell = local

    def __post_init__(self):
        """Post-init setup"""
        return

    def install(self, system: bool = False):
        """Install the service to the current host. Defaults to user-level install
        :param system: Flag to specify system-level install
        """
        system = True  # TODO remove, arg in the cli
        service_template = self.jinja_env.get_template("service.j2")
        service_raw = service_template.render(
            service_name=self.name,
            service_cmd=self.cmd,
            service_type=self.service_type,
        )
        install_path = (
            "/usr/lib/systemd/system/"
            if system
            else f"/home/{getuser()}/.config/systemd/user/"
        )
        with open(f"{install_path}{self.name}.service", "w") as sfile:
            for line in service_raw.splitlines():
                sfile.write(f"{line}\n")
        self.shell["systemctl"]["daemon-reload"]()
