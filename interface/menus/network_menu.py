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
                    "[8] - (Network Diagnostics)",
                    "[9] - (Return to menu)"
                ]
            ).ask()

            if options == "[1] - (NMAP)":
                sleep(0.5)
                from interface.screens.network.nmap_screen import menu_nmap_model
                menu_nmap_model()

            elif options == "[2] - (NETCAT)":
                sleep(0.5)
                from interface.screens.network.netcat_screen import menu_netcat_model
                menu_netcat_model()

            elif options == "[3] - (Wireshark)":
                print("Em desenvolvimento.")

            elif options == "[4] - (TShark)":
                sleep(0.5)
                from interface.screens.network.tshark_screen import menu_tshark_model
                menu_tshark_model()

            elif options == "[5] - (Tracerout)":
                sleep(0.5)
                from interface.screens.network.traceroute_screen import menu_traceroute_model
                menu_traceroute_model()

            elif options == "[6] - (MRT)":
                print("Em desenvolvimento.")

            elif options == "[7] - (ARP-Scan)":
                sleep(0.5)
                from interface.screens.network.arp_scan_screen import menu_arpScan_model
                menu_arpScan_model()

            elif options == "[8] - (Network Diagnostics)":
                sleep(0.5)
                from interface.screens.network.network_diagnostics_screen import menu_network_diagnostics_model
                menu_network_diagnostics_model()
                
            else:
                return
        
    except Exception as error:
        console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU:{error}[/bold red]")
        return
    