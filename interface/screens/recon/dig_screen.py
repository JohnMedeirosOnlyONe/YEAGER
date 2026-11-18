from rich.console import Console
from time import sleep
from interface.components.banners import banner_dig
import questionary

console = Console()

def menu_dig_model():
    try:
        banner_dig()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (A Record Lookup)",
                    "[2] - (AAAA Record Lookup)",
                    "[3] - (MX Record Lookup)",
                    "[4] - (NS Record Lookup)",
                    "[5] - (TXT Record Lookup)",
                    "[6] - (CNAME Record Lookup)",
                    "[7] - (SOA Record Lookup)",
                    "[8] - (PTR Reverse Lookup)",
                    "[9] - (DNS Trace)",
                    "[10] - (Query Specific DNS Server)",
                    "[11] - (Show Short Answer)",
                    "[12] - (Custom DNS Query)",
                    "[13] - (Save Query Results)",
                    "[14] - (Return to Recon Menu)"
                ]
            ).ask()

            if options == "[1] - (A Record Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (AAAA Record Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (MX Record Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (NS Record Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (TXT Record Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (CNAME Record Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (SOA Record Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (PTR Reverse Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (DNS Trace)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Query Specific DNS Server)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[11] - (Show Short Answer)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[12] - (Custom DNS Query)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[13] - (Save Query Results)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                return
            
    except Exception as error:
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")
        sleep(1)
        return