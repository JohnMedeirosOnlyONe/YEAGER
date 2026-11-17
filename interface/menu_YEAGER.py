import questionary
from time import sleep
from rich.console import Console

console = Console()

def menu_eren():
    try:
        while True:
            print("")
            console.print("[bold green]_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-[/bold green]")
            print("")

            console.print("[bold green]CHOOSE AN OPTION.[/bold green]")
            opcao = questionary.select(
                "SELECT",
                choices=[
                    "[1] - (Reconnaissance)",
                    "[2] - (Network Analysis)",
                    "[3] - (Web Analysis)",
                    "[4] - (Vulnerability Assessment)",
                    "[5] - (Security Frameworks)",
                    "[6] - (Tool Manager)",
                    "[7] - (Close)"
                ]
            ).ask()

            if opcao == "[1] - (Reconnaissance)":
                console.print("[bold green]Preparing target reconnaissance, domains, and subdomains.[/bold green]")
                sleep(1)
                from interface.menus.recon_menu import menu_tools_recon
                menu_tools_recon()

            elif opcao == "[2] - (Network Analysis)":
                console.print("[bold green]Preparing the execution of networks, ports, and services.[/bold green]")
                sleep(1)
                from interface.menus.network_menu import menu_tolls_network
                menu_tolls_network()

            elif opcao == "[3] - (Web Analysis)":
                console.print("[bold green]Performing analysis and enumeration of the web application.[/bold green]")
                sleep(1)
                from interface.menus.web_menu import menu_tools_web
                menu_tools_web()

            elif opcao == "[4] - (Vulnerability Assessment)":
                console.print("[bold green]Identifying and analyzing vulnerabilities.[/bold green]")
                sleep(1)
                from interface.menus.vulnerability_menu import menu_tools_vulnerability
                menu_tools_vulnerability()

            elif opcao == "[5] - (Security Frameworks)":
                console.print("[bold green]Accessing integrated tools and frameworks.[/bold green]")
                sleep(1)
                from interface.menus.frameworks_menu import menu_frameworks_tools
                menu_frameworks_tools()

            elif opcao == "[6] - (Tool Manager)":
                console.print("[bold green][/bold green]")
                sleep(1)
                from interface.menus.utilities_menu import menu_utilities_tools
                menu_utilities_tools()

            else: 
                break

    except Exception as error:
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")
        sleep(1)
        return
