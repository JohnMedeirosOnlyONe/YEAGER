from time import sleep
from rich.console import Console
import questionary

console = Console()

def menu_utilities_tools():
    try:
        while True:
            print("")
            console.print("[bold green]_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-[/bold green]")
            print("")

            console.print("[bold green]CHOOSE AN OPTION.[/bold green]")

            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (Target Manager)",
                    "[2] - (Dependency Checker)",
                    "[3] - (Network Utilities)",
                    "[4] - (Tool Manager)",
                    "[7] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (Target Manager)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (Dependency Checker)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (Network Utilities)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (Tool Manager)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                sleep(0.5)
                return

    except Exception as error:
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")