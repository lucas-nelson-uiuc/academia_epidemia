import rich
from rich.table import Table
from datetime import datetime

def checkprint(msg, style='bold green'):
    rich.print(f'[{style}]:: {msg} ::[/{style}]')

def subcheckprint(msg, style='green'):
    rich.print(f'[{style}]\t> {msg}[/{style}]')

def dollarprint(dollar_amount, style):
    if '-' in str(dollar_amount):
        dollar_amount = str(dollar_amount)[1:]
        style = 'bold red'
    dollar_amount = round(float(dollar_amount), 2)
    return f'[{style}]${dollar_amount}[/{style}]'


def tableprint(df):
    
    date_info = datetime.today().strftime('%B %d, %Y')
    table = Table(
        title=f'[bold green]eBASS Data :: Newest Batch ({date_info})[/bold green]',
        style='bold magenta'
    )

    for col in df.columns:
        table.add_column(
            col.title(),
            justify='left',
            style='cyan'
        )

    for i in range(5):
        d1, d2, d3, d4 = tuple([elem for elem in df.iloc[df.shape[0] - 5 + i, :]])
        table.add_row(
            d1.strftime('%B %d, %Y'),
            d2,
            dollarprint(d3, style='bold green'),
            dollarprint(d4, style='bold green')
        )
    
    rich.print(table)