from time import sleep
from rich.console import Console
import questionary
from interface.components.banners import banner_whois

console = Console()

def menu_whois_model():
    try:
        banner_whois()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (Basic WHOIS Lookup)",
                    "[2] - (Domain Registration Details)",
                    "[3] - (Registrar Information)",
                    "[4] - (Domain Name Servers)",
                    "[5] - (Registration and Expiration Dates)",
                    "[6] - (WHOIS Contact Information)",
                    "[7] - (Raw WHOIS Response)",
                    "[8] - (Query Specific WHOIS Server)",
                    "[9] - (Save WHOIS Results)",
                    "[10] - (Custom WHOIS Query)",
                    "[11] - (Return to Recon Menu)"
                ]
            ).ask()

            if options == "[1] - (Basic WHOIS Lookup)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (Domain Registration Details)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (Registrar Information)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (Domain Name Servers)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (Registration and Expiration Dates)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (WHOIS Contact Information)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (Raw WHOIS Response)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (Query Specific WHOIS Server)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (Save WHOIS Results)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Custom WHOIS Query)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                return
                            
    except Exception as error:
        sleep(0.5)
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU:{error}[/bold red]")
        return