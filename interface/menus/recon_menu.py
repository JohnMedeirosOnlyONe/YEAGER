from rich.console import Console
from time import sleep
import questionary

console = Console()

def menu_tools_recon():
    try:
        while True:
            print("")
            console.print("[bold green]_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-[/bold green]")
            print("")

            console.print("[bold green]CHOOSE AN OPTION.[/bold green]")

            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (Whois)",
                    "[2] - (Dig)",
                    "[3] - (Dns Enumaration)",
                    "[4] - (Subfinder)",
                    "[5] - (WhatWeb)",
                    "[6] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (Whois)":
                sleep(0.5)
                from interface.screens.recon.whois_screen import menu_whois_model
                menu_whois_model()

            elif options == "[2] - (Dig)":
                sleep(0.5)
                from interface.screens.recon.dig_screen import menu_dig_model
                menu_dig_model()

            elif options == "[3] - (Dns Enumaration)":
                sleep(0.5)
                from interface.screens.recon.dns_screen import menu_dns_enumaration_model
                menu_dns_enumaration_model()

            elif options == "[4] - (Subfinder)":
                sleep(0.5)
                from interface.screens.recon.subfinder_screen import menu_subfinder_model
                menu_subfinder_model()

            elif options == "[5] - (WhatWeb)":
                sleep(0.5)
                from interface.screens.web.whatweb_screen import menu_whatweb_model
                menu_whatweb_model()

            else:
                sleep(0.5)
                return

    except Exception as error:
        sleep(0.5)
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")
        return