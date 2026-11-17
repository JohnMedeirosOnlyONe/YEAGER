import questionary
from time import sleep
from rich.console import Console

console = Console()

def menu_tools_web():
    try:
        while True:
            print("")
            console.print("[bold green]_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-[/bold green]")
            print("")
        
            console.print("[bold green]CHOOSE AN OPTION.[/bold green]")

            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (FFUF)",
                    "[2] - (Gobuster)",
                    "[3] - (HTTP Header Analysis)",
                    "[4] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (FFUF)":
                sleep(0.5)
                pass

            elif options == "[2] - (Gobuster)":
                sleep(0.5)
                pass

            elif options == "[3] - (HTTP Header Analysis)":
                sleep(0.5)
                pass

            else:
                sleep(0.5)
                return

    except Exception as error:
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")
        sleep(1)
        return