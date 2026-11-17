from interface.interface_YEAGER import interface_yeager
from interface.menu_YEAGER import menu_eren

def main():
    try: 
        interface_yeager()
        menu_eren()

    except Exception as error:
        print(f"AN ERROR OCCURRED DURING YEAGER INITIALIZATION: {error}")

if __name__ == "__main__":
    main()