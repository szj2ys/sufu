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


@cli.command(help='run test')
def test():
    FILE = join(ROOT, 'scripts', 'test.sh')
    os.system(f'bash {FILE}')


def run():
    try:
        cli(prog_name='do')
    except Exception as e:
        pass


if __name__ == "__main__":
    run()
