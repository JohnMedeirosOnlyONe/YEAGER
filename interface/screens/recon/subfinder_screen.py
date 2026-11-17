from rich.console import Console
from time import sleep
import questionary
from interface.components.banners import banner_subfinder

def menu_subfinder_model():
    try:
        banner_subfinder()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    ""
                ]
            )
    except Exception as error:
        Console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")