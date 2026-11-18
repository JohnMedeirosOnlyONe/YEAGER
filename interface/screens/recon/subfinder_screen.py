from rich.console import Console
from time import sleep
import questionary
from interface.components.banners import banner_subfinder

def menu_subfinder_model():
    try:
        banner_subfinder()

        while True:
            options = questionary.select(
                "Select",
                choices=[
                    "[1] - (Basic Subdomain Enumeration)",
                    "[2] - (Enumerate Multiple Domains)",
                    "[3] - (Use All Available Sources)",
                    "[4] - (Select Specific Sources)",
                    "[5] - (Exclude Specific Sources)",
                    "[6] - (Recursive Subdomain Enumeration)",
                    "[7] - (Use Active Resolution)",
                    "[8] - (Specify Custom Resolvers)",
                    "[9] - (Silent Output)",
                    "[10] - (Verbose Output)",
                    "[11] - (Save Results to File)",
                    "[12] - (Export Results as JSON)",
                    "[13] - (Custom Command)",
                    "[14] - (Return to Recon Menu)"
                ]
            ).ask()

            if options == "[1] - (Basic Subdomain Enumeration)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[2] - (Enumerate Multiple Domains)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[3] - (Use All Available Sources)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[4] - (Select Specific Sources)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[5] - (Exclude Specific Sources)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[6] - (Recursive Subdomain Enumeration)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[7] - (Use Active Resolution)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[8] - (Specify Custom Resolvers)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[9] - (Silent Output)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[10] - (Verbose Output)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[11] - (Save Results to File)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[12] - (Export Results as JSON)":
                sleep(0.5)
                print("Em desenvolvimento")

            elif options == "[13] - (Custom Command)":
                sleep(0.5)
                print("Em desenvolvimento")

            else:
                return

    except Exception as error:
        sleep(0.5)
        Console.print(f"[bold red]AN ERROR OCCURRED IN THE MENU: {error}[/bold red]")
        return