from time import sleep
from rich.console import Console
import questionary
from interface.components.banners import banner_tracerout

console = Console()

def menu_traceroute_model():
    try:
        banner_tracerout()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (Basic Traceroute)",
                    "[2] - (ICMP Traceroute)",
                    "[3] - (TCP Traceroute)",
                    "[4] - (UDP Traceroute)",
                    "[5] - (IPv4 Traceroute)",
                    "[6] - (IPv6 Traceroute)",
                    "[7] - (Set Max Hops)",
                    "[8] - (Set Timeout)",
                    "[9] - (Set Packet Size)",
                    "[10] - (Set Queries per Hop)",
                    "[11] - (Disable DNS Resolution)",
                    "[12] - (Set Network Interface)",
                    "[13] - (Custom Command)",
                    "[14] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (Basic Traceroute)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (ICMP Traceroute)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (TCP Traceroute)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (UDP Traceroute)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (IPv4 Traceroute)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (IPv6 Traceroute)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (Set Max Hops)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (Set Timeout)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (Set Packet Size)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Set Queries per Hop)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[11] - (Disable DNS Resolution)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[12] - (Set Network Interface)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[13] - (Custom Command)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                return
            
    except Exception as error:
        sleep(0.5)
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU:{error}[/bold red]")
        return