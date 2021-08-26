#/usr/bin/python3
# *_*coding:utf-8 *_*
import os
from pathlib import Path
from os.path import dirname, abspath, join

ROOT = dirname(abspath(__file__))
import click
from click_help_colors import HelpColorsGroup


@click.group(cls=HelpColorsGroup,
             help_headers_color='yellow',
             help_options_color='magenta',
             help_options_custom_colors={
                 'up': 'cyan',
                 'push': 'cyan',
                 'undo': 'red',
                 'unstage': 'red',
                 'revert': 'red',
                 'diff': 'green',
                 'branch': 'green',
                 'add': 'blue',
                 'commit': 'blue',
                 'save': 'blue',
             })
def cli():
    """\b
                .__   .__
  ______  ______|  |  |__|  ____     ____
 /  ___/ / ____/|  |  |  | /    \   / ___\
 \___ \ < <_|  ||  |__|  ||   |  \ / /_/  >
/____  > \__   ||____/|__||___|  / \___  /
     \/     |__|               \/ /_____/
    """


# http://patorjk.com/software/taag/#p=display&h=0&v=0&f=Graffiti&t=funlp
@cli.command(help='Print version.')
def version():
    here = Path(__file__).parent.absolute()
    package_conf = {}
    with open(os.path.join(here, "__version__.py")) as f:
        exec(f.read(), package_conf)
    print(package_conf['__version__'])


@cli.command(help='run clean')
def clean():
    FILE = join(ROOT, 'scripts', 'clean.sh')
    os.system(f'bash {FILE}')


@cli.command(help='run create')
def create():
    FILE = join(ROOT, 'scripts', 'create.sh')
    os.system(f'bash {FILE}')


@cli.command(help='git pull to remote')
def gitpull():
    FILE = join(ROOT, 'scripts', 'gitpull.sh')
    os.system(f'bash {FILE}')


@cli.command(help='run delete')
def delete():
    FILE = join(ROOT, 'scripts', 'delete.sh')
    os.system(f'bash {FILE}')


@cli.command(help='run install')
def install():
    FILE = join(ROOT, 'scripts', 'install.sh')
    os.system(f'bash {FILE}')


@cli.command(help='run publish')
def publish():
    FILE = join(ROOT, 'scripts', 'publish.sh')
    os.system(f'bash {FILE}')


@cli.command(help='run requirements')
def require():
    FILE = join(ROOT, 'scripts', 'requirements.sh')
    os.system(f'bash {FILE}')


@cli.command(help='run python script')
def run():
    FILE = join(ROOT, 'scripts', 'run.sh')
    os.system(f'bash {FILE}')


def execute():
    try:
        cli(prog_name='sufu')
    except Exception as e:
        pass


if __name__ == "__main__":
    execute()
