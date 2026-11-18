from rich.console import Console
from time import sleep
import questionary
from interface.components.banners import banner_netcat

console = Console()

def menu_netcat_model():
    try:
        banner_netcat()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (TCP Connection)",
                    "[2] - (UDP Connection)",
                    "[3] - (Port Scanning)",
                    "[4] - (Banner Grabbing)",
                    "[5] - (Start TCP Listener)",
                    "[6] - (Start UDP Listener)",
                    "[7] - (File Transfer - Send)",
                    "[8] - (File Transfer - Receive)",
                    "[9] - (Reverse Shell)",
                    "[10] - (Bind Shell)",
                    "[11] - (Custom Command)",
                    "[12] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (TCP Connection)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (UDP Connection)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (Port Scanning)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (Banner Grabbing)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (Start TCP Listener)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (Start UDP Listener)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (File Transfer - Send)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (File Transfer - Receive)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (Reverse Shell)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Bind Shell)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[11] - (Custom Command)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                return
            
    except Exception as error:
        sleep(0.5)
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU:{error}[/bold red]")
        return