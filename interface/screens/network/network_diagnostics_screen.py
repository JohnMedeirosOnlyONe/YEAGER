from time import sleep
from rich.console import Console
import questionary
from interface.components.banners import banner_network_diagnostics

console = Console()

def menu_network_diagnostics_model():
    try:
        banner_network_diagnostics()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (Ping Host)",
                    "[2] - (Continuous Ping)",
                    "[3] - (DNS Lookup)",
                    "[4] - (Reverse DNS Lookup)",
                    "[5] - (Check Network Interfaces)",
                    "[6] - (Display IP Addresses)",
                    "[7] - (Display Routing Table)",
                    "[8] - (Check Default Gateway)",
                    "[9] - (Check DNS Configuration)",
                    "[10] - (Test Internet Connectivity)",
                    "[11] - (Check Listening Ports)",
                    "[12] - (Display Active Connections)",
                    "[13] - (Network Statistics)",
                    "[14] - (Custom Command)",
                    "[15] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (Ping Host)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (Continuous Ping)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (DNS Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (Reverse DNS Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (Check Network Interfaces)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (Display IP Addresses)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (Display Routing Table)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (Check Default Gateway)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (Check DNS Configuration)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Test Internet Connectivity)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[11] - (Check Listening Ports)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[12] - (Display Active Connections)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[13] - (Network Statistics)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[14] - (Custom Command)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                return
            
    except Exception as error:
        sleep(0.5)
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU:{error}[/bold red]")
        return