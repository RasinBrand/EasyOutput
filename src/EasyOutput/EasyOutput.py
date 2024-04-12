from colorama import Fore, Style, Back as bg
from typing import Optional

import colorama

reset = Style.RESET_ALL
brighten = Style.BRIGHT
dim_message = Style.DIM

class Colors:
    
    def Show():
        """
        Shows all available colors 
        """
        Title_Print("All Colors", color=Colors.Cyan)
        Colored_Message("Red", color=Colors.Red)
        Colored_Message("Light Red", color=Colors.Light_Red)
        Colored_Message("Green", color=Colors.Green)
        Colored_Message("Light Green", color=Colors.Light_Green)
        Colored_Message("Blue", color=Colors.Blue)
        Colored_Message("Light Blue", color=Colors.Light_Blue)
        Colored_Message("Black", color=Colors.Black)
        Colored_Message("Light Black", color=Colors.Light_Black)
        Colored_Message("Yellow", color=Colors.Yellow)
        Colored_Message("Light Yellow", color=Colors.Light_Yellow)
        Colored_Message("Cyan", color=Colors.Cyan)
        Colored_Message("Light Cyan", color=Colors.Light_Cyan)
        Colored_Message("White", color=Colors.White)
        Colored_Message("Light White", color=Colors.Light_White)
        Colored_Message("Magenta", color=Colors.Magenta)
        Colored_Message("Light Magenta", color=Colors.Light_Magenta)
        
    Red = Fore.RED
    Green = Fore.GREEN
    Blue = Fore.BLUE
    Black = Fore.BLACK
    Yellow = Fore.YELLOW
    Cyan = Fore.CYAN
    White = Fore.WHITE
    Magenta = Fore.MAGENTA
    Light_Red = Fore.LIGHTRED_EX
    Light_Green = Fore.LIGHTGREEN_EX
    Light_Blue = Fore.LIGHTBLUE_EX
    Light_Black = Fore.LIGHTBLACK_EX
    Light_Yellow = Fore.LIGHTYELLOW_EX
    Light_Cyan = Fore.LIGHTCYAN_EX
    Light_White = Fore.LIGHTWHITE_EX
    Light_Magenta = Fore.LIGHTMAGENTA_EX


class Highlights:
    none = ""
    Red = bg.RED
    Green = bg.GREEN
    Blue = bg.BLUE
    Black = bg.BLACK
    Yellow = bg.YELLOW
    Cyan = bg.CYAN
    White = bg.WHITE
    Magenta = bg.MAGENTA
    Light_Red = bg.LIGHTRED_EX
    Light_Green = bg.LIGHTGREEN_EX
    Light_Blue = bg.LIGHTBLUE_EX
    Light_Black = bg.LIGHTBLACK_EX
    Light_Yellow = bg.LIGHTYELLOW_EX
    Light_Cyan = bg.LIGHTCYAN_EX
    Light_White = bg.LIGHTWHITE_EX
    Light_Magenta = bg.LIGHTMAGENTA_EX


def Info_Message(message, color: Colors = Colors.White, highlight: Highlights = '', title_color: Colors = Colors.Blue):  
    """
    Prints a message notifying the user of specific need to know information.
    
    color
        Color your message! The standard is set to white.
    
    highlight
        Blue
    """
    print(f"{title_color + brighten}Info{reset}: {highlight + color + message + reset}")
    
def Error_Message(message, color: Colors = Colors.White, highlight: Highlights = '', title_color: Colors = Colors.Red):
    """
    Prints a message notifying the user of an error.
    
    colo
        Color your message! The standard is set to white.
    
    highlight
        Red
    """
    print(f"{title_color}Error{reset}: {highlight + color + message + reset}")

    
def Connection_Error_Message(message, color: Colors = Colors.White, highlight: Highlights = '', title_color: Colors = Colors.Red):
    """
    Prints a message notifying the user of a connection error.
    
    colo
        Color your message! The standard is set to white.
    
    highlight
        Red
    """
    print(f"{title_color}Connection Error{reset}: {highlight + color +  message + reset}")
    
def Success_Message(message, color: Colors = Colors.White, highlight: Highlights = '', title_color: Colors = Colors.Green):
    """
    Prints a message notifying the user of a success.
    
    color:
        Color your message! The standard is set to white.
    
    highlight
        Green
    """
    print(f"{title_color + brighten}Success{reset}: {highlight + color + message + reset}")
    
def Successful_Connection_Message(message, color: Colors = Colors.White, highlight: Highlights = '', title_color: Colors = Colors.Green):
    """
    Prints a message notifying the user of a successful connection.
    
    color:
        Color your message! The standard is set to white.
    
    highlight
        Green
    """
    print(f"{title_color + brighten}Successful Connection{reset}: {highlight + color + message + reset}")
    
def Note_Message(message, color: Colors = Colors.White, highlight: Highlights = '', title_color: Colors = Colors.Yellow):
    """
    Prints a note notifying the user of something they should be made aware of.
    
    color: 
        Color your message! The standard is set to white.
    
    highlight
        Yellow
    """
    print(f"{title_color}Note{reset}: {highlight + color +  message + reset}")
    
def Warning_Message(message, color: Colors = Colors.White, highlight: Highlights = '', title_color: Colors = Colors.Yellow):
    """
    Prints a warning message for the user indicating your code is running.
    
    color: 
        Color your message! The standard is set to white.
    
    highlight
        Yellow
    """
    print(f"{title_color}Warning{reset}: {highlight + color +  message + reset}")    

    
def Title_Print(title, color: Colors = Colors.Green, highlight: Highlights = ''):
    """
    Prints a title for grouping lists and anything else you can think of.
    
    color:
        Color your message! The standard is set to green.
    
    highlight
        Green
    """
    print(f"=== {highlight + color + brighten + title + reset} ===")    

     
def Redacted_Message(message, color: Colors = Colors.White, highlight: Highlights = '', title_color: Colors = Colors.Red):
    """
    Prints redacted message 
    
    color:
        Color your message! The standard is set to white.
    
    highlight
        Red
    """
    print(f"{title_color}REDACTED{reset}: {highlight + color + message + reset}")    


def Colored_Message(message, color: Colors = Colors.White, highlight: Highlights = ''):
    """
    Prints user written message!
    
    color:
        Color your message! The standard is set to white.

    """
    print(highlight + color + message + reset)