import pyfiglet
from rich.console import Console
from time import sleep
Console = Console()

# YEAGER system initiated
def interface_yeager():
    try:
        eren_yeager = pyfiglet.figlet_format("YEAGER", font="slant")
        Console.print("[bold orange1]_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-[/bold orange1]")
        print("")
        Console.print("[bold red]ALERT:[/bold red] [bold orange1]YEAGER SYSTEM INITIATED.[/bold orange1]")
        sleep(1)
        Console.print(f"[bold orange1]STARTING TOOL![/bold orange1]")
        sleep(0.5)
        Console.print(f"[bold orange1]3...[/bold orange1]")
        sleep(1)
        Console.print(f"[bold orange1]2...[/bold orange1]")
        sleep(1)
        Console.print(f"[bold orange1]1...[/bold orange1]")
        sleep(1)
        Console.print("[green]TOOL STARTED SUCCESSFULLY.[/green]")
        print("")
        Console.print("[bold orange1]_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-[/bold orange1]")
        print("")
        sleep(2)

        Console.print(f"[bold orange1]{eren_yeager}[/bold orange1]")
        sleep(0.5)

        eren_olhar = """
                                                                                        
                                            [bold orange1]░░░▓[/] [bold orange1]░[/] [bold orange1]░░[/]  [bold orange1]░[/]                                
                                          [bold orange1]▓░▓▓▓▓░▓░▓▓▓░▓[/]                                
                                          [bold orange1]▓░░▓░░▓▓░▓▓░▓▓[/]          [bold orange1]░[/]           [bold orange1]░[/]         
                     [bold orange1]░[/]                    [bold orange1]░▓▓▓░▓░▓░▓░▓▓[/]          [bold orange1]░[/]                      
               [bold orange1]░░[/]                          [bold orange1]▓▓▓░▓[/] [bold orange1]░▓▓░░░[/]                                 
                                            [bold orange1]▓▓▓░░[/] [bold orange1]░▓░▓[/]                                  
                     [bold orange1]░░░[/]                    [bold orange1]░▓░[/] [bold orange1]░[/]  [bold orange1]▓░[/]                    [bold orange1]░░▓░[/]           
                     [bold orange1]░░░░▓░░[/]                [bold orange1]░░[/]  [bold orange1]▓[/]  [bold orange1]░[/] [bold orange1]░[/]               [bold orange1]░░░░▓▓▓░[/]           
                          [bold orange1]░░▓▓░░░[/]          [bold orange1]░▓░[/]  [bold orange1]▓▓[/] [bold orange1]░░▓[/]           [bold orange1]░░░▓▓░[/]                 
         [bold orange1]░[/] [bold orange1]░[/]  [bold orange1]░░░░[/]   [bold orange1]░[/]      [bold orange1]░▓▓▓▓▓▓░[/]      [bold orange1]▓▓░░▓▓▓▓▓▓▓█▓░[/]    [bold orange1]░▓░▓▓▓▓░░[/]      [bold orange1]░[/] [bold orange1]░[/] [bold orange1]░░░░[/]   [bold orange1]░[/] 
            [bold white]████[/] [bold orange1]░[/]  [bold green]▓▓[/] [bold green]▓▓[/] [bold green]▓▓▓[/] [bold orange1]░░░░▓░▓▓░▓▓░▓▓▓▓▓▓░░▓▓▓▓░▓▓▓▓▓▓▓▓▓░░░[/]  [bold green]▓▓[/]  [bold green]▓[/] [bold green]▓▓▓[/][bold white]██[/] [bold white]████[/]   
             [bold white]███████[/][bold green]▓████▓[/][bold white]████[/]  [bold orange1]░░░▓▓▓[/] [bold orange1]▓░░▓█▓░[/]       [bold orange1]▓▓██░░▓▓░░░░[/]  [bold white]███[/][bold green]▓████▓▓[/][bold white]███████[/]    
               [bold white]█████[/]           [bold orange1]░░░░▓▓[/] [bold orange1]▓[/] [bold orange1]▓▓░▓█░[/]       [bold orange1]░▓▓▓░▓░░▓░░[/]             [bold white]████[/]       
                      [bold orange1]░▓░░░░▓▓░░░▓▓░▓░▓░▓▓░▓▓░[/]         [bold orange1]▓▓▓▓░▓▓▓░░▓▓▓▓░░░░▓░[/] [bold orange1]░░░[/]         
                              [bold orange1]▓▓░░▓▓▓▓░[/] [bold orange1]▓▓░▓░▓░[/]             [bold orange1]▓▓▓░░░░[/]                     
                            [bold orange1]░░░░░░░[/]        [bold orange1]░░░░[/]                [bold orange1]░[/] [bold orange1]░░░░[/]                   
                                             [bold orange1]░░[/]                    [bold orange1]░[/]                    
                                              [bold orange1]░[/]                                         
                                                                                        
        """
        Console.print(eren_olhar)
        sleep(1.5)
        
    except Exception as error:
        Console.print("[bold red]AN ERROR OCCURRED DURING YEAGER INITIALIZATION:[/bold red]")
        print(error)