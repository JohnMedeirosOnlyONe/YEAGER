from time import sleep
from rich.console import Console
import questionary

console = Console()

def menu_frameworks_tools():
    try:
        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (OWASP Top 10)",
                    "[2] - (MITRE ATT&CK)",
                    "[3] - (NIST cybersecurity Framework)",
                    "[4] - (CIS Controls)",
                    "[5] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (OWASP Top 10)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (MITRE ATT&CK)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (NIST cybersecurity Framework)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (CIS Controls)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                sleep(0.5)
                return
            
    except Exception as error:
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")