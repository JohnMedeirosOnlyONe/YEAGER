from rich.console import Console
from time import sleep
from interface.components.banners import banner_tshark
import questionary

console = Console()

def menu_tshark_model():
    try:
        banner_tshark()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (List Network Interfaces)",
                    "[2] - (Start Packet Capture)",
                    "[3] - (Capture TCP Traffic)",
                    "[4] - (Capture UDP Traffic)",
                    "[5] - (Capture HTTP Traffic)",
                    "[6] - (Capture DNS Traffic)",
                    "[7] - (Capture ICMP Traffic)",
                    "[8] - (Capture Specific Port)",
                    "[9] - (Capture Specific Host)",
                    "[10] - (Read PCAP File)",
                    "[11] - (Save Capture to PCAP)",
                    "[12] - (Apply Display Filter)",
                    "[13] - (Apply Capture Filter)",
                    "[14] - (Protocol Statistics)",
                    "[15] - (Follow TCP Stream)",
                    "[16] - (Extract Packet Fields)",
                    "[17] - (Custom Command)",
                    "[18] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (List Network Interfaces)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (Start Packet Capture)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (Capture TCP Traffic)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (Capture UDP Traffic)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (Capture HTTP Traffic)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (Capture DNS Traffic)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (Capture ICMP Traffic)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (Capture Specific Port)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (Capture Specific Host)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Read PCAP File)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[11] - (Save Capture to PCAP)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[12] - (Apply Display Filter)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[13] - (Apply Capture Filter)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[14] - (Protocol Statistics)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[15] - (Follow TCP Stream)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[16] - (Extract Packet Fields)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[17] - (Custom Command)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                return
            
    except Exception as error:
        sleep(0.5)
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU:{error}[/bold red]")
        return