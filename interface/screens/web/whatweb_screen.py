from time import sleep
from rich.console import Console
from interface.components.banners import banner_whatweb
import questionary

console = Console()

def menu_whatweb_model():
    try:
        banner_whatweb()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (Basic Technology Detection)",
                    "[2] - (Scan Multiple Websites)",
                    "[3] - (Set Aggression Level)",
                    "[4] - (Show Verbose Results)",
                    "[5] - (Use Custom User-Agent)",
                    "[6] - (Set Custom HTTP Headers)",
                    "[7] - (Use Authentication)",
                    "[8] - (Set Proxy)",
                    "[9] - (Save Results as JSON)",
                    "[10] - (Save Results as Text)",
                    "[11] - (Custom Command)",
                    "[12] - (Return to Recon Menu)"
                ]
            ).ask()

            if options == "[1] - (Basic Technology Detection)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (Scan Multiple Websites)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (Set Aggression Level)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (Show Verbose Results)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (Use Custom User-Agent)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (Set Custom HTTP Headers)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (Use Authentication)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (Set Proxy)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (Save Results as JSON)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Save Results as Text)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[11] - (Custom Command)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                return
            
    except Exception as error:
        sleep(1)
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")
        return