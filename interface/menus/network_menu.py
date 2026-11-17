from rich.console import Console
from time import sleep
import questionary

console = Console()

def menu_tolls_network():
    try:
        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (NMAP)",
                    "[2] - (NETCAT)",
                    "[3] - (Wireshark)",
                    "[4] - (TShark)",
                    "[5] - (Tracerout)",
                    "[6] - (MRT)",
                    "[7] - (ARP-Scan)",
                    "[8] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (NMAP)":
                sleep(0.5)
                from interface.screens.network.nmap_screen import menu_nmap_model
                menu_nmap_model()

            elif options == "[2] - (NETCAT)":
                print("Em desenvolvimento.")

            elif options == "[3] - (Wireshark)":
                print("Em desenvolvimento.")

            elif options == "[4] - (TShark)":
                print("Em desenvolvimento.")

            elif options == "[5] - (Tracerout)":
                print("Em desenvolvimento.")

            elif options == "[6] - (MRT)":
                print("Em desenvolvimento.")

            elif options == "[7] - (ARP-Scan)":
                print("Em desenvolvimento.")

            else:
                return
        
    except Exception as error:
        console.print("[bold red]AN ERROR OCCURRED IN THE MENU:[/bold red]")
        print(error)
        return
    