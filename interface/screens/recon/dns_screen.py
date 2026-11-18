from rich.console import Console
from time import sleep
from interface.components.banners import banner_dns_enumaration
import questionary

console = Console()

def menu_dns_enumaration_model():
    try:
        banner_dns_enumaration()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (Enumerate DNS Records)",
                    "[2] - (Discover Subdomains)",
                    "[3] - (Reverse DNS Enumeration)",
                    "[4] - (Check DNS Zone Transfer)",
                    "[5] - (Query Name Servers)",
                    "[6] - (Inspect SPF and DMARC Records)",
                    "[7] - (Enumerate TXT Records)",
                    "[8] - (Resolve Hostname List)",
                    "[9] - (Set DNS Resolver)",
                    "[10] - (Save Enumeration Results)",
                    "[11] - (Custom DNS Operation)",
                    "[12] - (Return to Recon Menu)"
                ]
            ).ask()

            if options == "[1] - (Enumerate DNS Records)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (Discover Subdomains)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (Reverse DNS Enumeration)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (Check DNS Zone Transfer)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (Query Name Servers)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (Inspect SPF and DMARC Records)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (Enumerate TXT Records)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (Resolve Hostname List)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (Set DNS Resolver)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Save Enumeration Results)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[11] - (Custom DNS Operation)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                return
            
    except Exception as error:
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")
        sleep(1)
        return