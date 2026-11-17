import questionary
from time import sleep
from rich.console import Console
from rich.prompt import Prompt
from interface.components.banners import banner_nmap

console = Console()

def menu_nmap_model():
    try:
        banner_nmap()
        target = Prompt.ask("[red]Please enter the target IP address or hostname[/red]")

        if not target:
             console.print("[bold red]No target provided![/bold red]")

             while len(target) == 0:
                 target = Prompt.ask("[red]Please enter the target IP address or hostname[/red]")
        
        option = questionary.select(
            "Select",
            choices=[
                "[1] - (Host Discovery)",
                "[2] - (Port Scanning)",
                "[3] - (Service & Version Detection)",
                "[4] - (OS Detection)",
                "[5] - (NSE Script Scanning)",
                "[6] - (Advanced Scan Configuration)",
                "[7] - (Scan Reports)",
                "[8] - (Back to Network Menu)"
            ]
        ).ask()

        if option == "[1] - (Host Discovery)":
            sleep(1)
            console.print(f"[orange1]Checking how many devices are active on the target:[/orange1] [blue]{target}[/blue]")
            # from exemplo.exmplo import exemplo
        
        elif option == "[2] - (Port Scanning)":
            sleep(1)
            console.print(f"[orange1]Checking whether the target's TCP or UDP ports are open, closed, or filtered:[/orange1] [blue]{target}[/blue]")
            # from exemplo.exmplo import exemplo

        elif option == "[3] - (Service & Version Detection)":
            sleep(1)
            console.print(f"[orange1]Checking the target's services and versions:[/orange1] [blue]{target}[/blue]")
            # from exemplo.exmplo import exemplo

        elif option == "[4] - (OS Detection)":
            sleep(1)
            console.print(f"[orange1]Identifying the target's operating system:[/orange1] [blue]{target}[/blue]")
            # from exemplo.exmplo import exemplo

        elif option == "[5] - (NSE Script Scanning)":
            sleep(1)
            console.print(f"[orange1]Running Nmap scripts to obtain information or perform specific checks on the target:[/orange1] [blue]{target}[/blue]")
            # from exemplo.exmplo import exemplo

        elif option == "[6] - (Advanced Scan Configuration)":
            sleep(1)
            console.print(f"[orange1]Entering Nmap advanced scanning:[/orange1] [blue]{target}[/blue]")
            # from exemplo.exmplo import exemplo

        elif option == "[7] - (Scan Reports)":
            sleep(1)
            console.print(f"[orange1]Entering the area to save the results:[/orange1] [blue]{target}[/blue]")
            # from exemplo.exmplo import exemplo

        else:
            sleep(1)
            console.print("[bold red]Returning to the menu.[/bold red]")
            return

    except Exception as error:
        console.print("[bold red]AN ERROR OCCURRED IN THE MENU:[/bold red]")
        print(error)
