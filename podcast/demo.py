

from pip import main
from colorama import init, Fore, Back, Style
import click

@click.command()
@click.argument("city")
@click.option("--language", help="Language Ex: ja, en.", default="en")
@click.option("--interval", help="Interval (daily or hourly). Default is daily.", default="daily")
def main(city: str, language: str, interval: str):
    init(autoreset=True)
    print(Fore.YELLOW + "Hello World From city: " + city)
    print(Fore.RED + 'some red text')
    print(Fore.BLUE + Back.RED + 'and with a green background')
    print(Style.DIM + 'and in dim text')

if __name__ == "__main__":
    main()