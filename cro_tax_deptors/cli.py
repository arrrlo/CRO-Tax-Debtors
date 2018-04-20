import click

from cro_tax_deptors.screen import Screen
from cro_tax_deptors.spiders import CroTaxDepartment
from cro_tax_deptors.save_handlers import RedisHandler
from cro_tax_deptors.deptors import Deptors, CategoryDone


@click.group()
def cli():
    pass


@cli.command()
@click.option('-p', '--print_in_terminal', default=False, is_flag=True, help='Print in terminal')
def parse(print_in_terminal):

    data = [
        {
            'title': 'Fizicke osobe',
            'namespace': 'FIZICKE-OSOBE',
            'item': 'ime i prezime',
            'dept_key': 'ukupni iznos duga',
            'toplist_limit': 20,
            'color': 'blue',
            'url': 'http://duznici.porezna-uprava.hr/fo/svi/{}.html',
            'spider': CroTaxDepartment,
            'save_handler': RedisHandler,
            'connection': {
                'host': 'localhost',
                'port': 6379,
                'db': 0
            },
            'parsed': 0
        },
        {
            'title': 'Pravne osobe',
            'namespace': 'PRAVNE-OSOBE',
            'item': 'naziv pravne osobe',
            'dept_key': 'ukupni iznos duga',
            'toplist_limit': 20,
            'color': 'red',
            'url': 'http://duznici.porezna-uprava.hr/po/svi/{}.html',
            'spider': CroTaxDepartment,
            'save_handler': RedisHandler,
            'connection': {
                'host': 'localhost',
                'port': 6379,
                'db': 0
            },
            'parsed': 0
        },
        {
            'title': 'Gradjani',
            'namespace': 'GRADJANI',
            'item': 'ime i prezime',
            'dept_key': 'ukupni iznos duga',
            'toplist_limit': 20,
            'color': 'green',
            'url': 'http://duznici.porezna-uprava.hr/gr/svi/{}.html',
            'spider': CroTaxDepartment,
            'save_handler': RedisHandler,
            'connection': {
                'host': 'localhost',
                'port': 6379,
                'db': 0
            },
            'parsed': 0
        }
    ]

    screen = Screen()

    for category in data:
        for page in range(1, 2000):
            try:
                spider = category['spider'](category['url'].format(page))
                save_handler = category['save_handler'](category)
                Deptors(spider, save_handler, screen, category).run(print_in_terminal)

            except CategoryDone:
                break
