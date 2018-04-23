import click

from cro_tax_deptors.screen import Screen
from cro_tax_deptors.spiders import CroTaxDepartment
from cro_tax_deptors.save_handlers import RedisHandler
from cro_tax_deptors.deptors import Deptors, CategoryDone


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {
        'data': [
            {
                # website specific, don't change
                'title': 'Fizicke osobe',
                'item': 'ime i prezime',
                'dept_key': 'ukupni iznos duga',
                'url': 'http://duznici.porezna-uprava.hr/fo/svi/{}.html',

                # your database specific, change as you like
                'namespace': 'FIZICKE-OSOBE',
                'toplist_limit': 20,
                'color': 'blue',
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
                # website specific, don't change
                'title': 'Pravne osobe',
                'item': 'naziv pravne osobe',
                'dept_key': 'ukupni iznos duga',
                'url': 'http://duznici.porezna-uprava.hr/po/svi/{}.html',

                # your database specific, change as you like
                'namespace': 'PRAVNE-OSOBE',
                'toplist_limit': 20,
                'color': 'red',
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
                # website specific, don't change
                'title': 'Gradjani',
                'item': 'ime i prezime',
                'dept_key': 'ukupni iznos duga',
                'url': 'http://duznici.porezna-uprava.hr/gr/svi/{}.html',

                # your database specific, change as you like
                'namespace': 'GRADJANI',
                'toplist_limit': 20,
                'color': 'green',
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
    }


@cli.command()
@click.pass_context
@click.option('-p', '--print_in_terminal', default=False, is_flag=True, help='Print in terminal')
def parse(ctx, print_in_terminal):

    screen = Screen()

    for category in ctx.obj['data']:
        for page in range(1, 2000):
            try:
                spider = category['spider'](category['url'].format(page))
                save_handler = category['save_handler'](category)
                Deptors(spider, save_handler, screen, category).run(print_in_terminal)

            except CategoryDone:
                break


@cli.command()
@click.pass_context
@click.option('-n', '--name', help='Name of the deptor')
def find(ctx, name):

    screen = Screen()

    for category in ctx.obj['data']:
        save_handler = category['save_handler'](category)
        Deptors(save_handler=save_handler, screen=screen, category_data=category).find(name)


@cli.command()
@click.pass_context
def delete(ctx):

    for category in ctx.obj['data']:
        save_handler = category['save_handler'](category)
        res = Deptors(save_handler=save_handler, category_data=category).delete()

    click.echo()
