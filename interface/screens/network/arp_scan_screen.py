from rich.console import Console
from time import sleep
import questionary
from interface.components.banners import banner_arp_scan

console = Console()

def menu_arpScan_model():
    try:
        banner_arp_scan()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (List Network Interfaces)",
                    "[2] - (Basic ARP Scan)",
                    "[3] - (Scan Local Network)",
                    "[4] - (Scan Specific Subnet)",
                    "[5] - (Scan Specific Host)",
                    "[6] - (Discover Active Hosts)",
                    "[7] - (Scan with Specific Interface)",
                    "[8] - (Display MAC Addresses)",
                    "[9] - (Identify Device Vendors)",
                    "[10] - (Set Scan Timeout)",
                    "[11] - (Set Retry Count)",
                    "[12] - (Disable DNS Resolution)",
                    "[13] - (Save Scan Results)",
                    "[14] - (Custom Command)",
                    "[15] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (List Network Interfaces)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (Basic ARP Scan)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (Scan Local Network)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (Scan Specific Subnet)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (Scan Specific Host)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (Discover Active Hosts)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (Scan with Specific Interface)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (Display MAC Addresses)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (Identify Device Vendors)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Set Scan Timeout)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[11] - (Set Retry Count)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[12] - (Disable DNS Resolution)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[13] - (Save Scan Results)":
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