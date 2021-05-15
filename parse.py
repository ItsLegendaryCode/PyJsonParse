import json
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def LoadJsonScheme(path, application):
    '''
    path = Path to JSON based scheme
    application = An object for the scheme to be applied on -> Function (return value) ; String
    Note: It can be of any type, but will be converted to str()
    Usage: A JSON based application scheme parser
    AVAILIBLE COLORS:
    Union: Fore, Back, Style
           1. green, white
           2. white, green
           3. red, cyan
           4. yellow, magenta
           5. black, white
           6. white, black
           7. yellow, white
           8. black, red
           9. black, green
           10. cyan, black
           11. green, white, bright
           12. white, green, bright
           13. red, cyan, bright
           14. yellow, magenta, bright
           15. black, white, bright
           16. white, black, bright
           17. yellow, white, bright
           18. black, red, bright
           19. black, green, bright
           20. cyan, black, bright
           21. green, white, dim
           22. white, green, dim
           23. red, cyan, dim
           24. yellow, magenta, dim
           25. black, white, dim
           26. white, black, dim
           27. yellow, white, dim
           28. black, red, dim
           29. black, green, dim
           30. cyan, black, dim

    '''
    if type(application) is not str:
        application = str(application)
    with open(path, "r") as json_scheme:
        json_data = json_scheme.read()
        json_scheme.close()
    data = json.loads(json_data)
    container = [data]
    sections = ["$colors"]
    styles = ["fore", "back", "style"]
    process_values = []
    for section in sections:
        for st in styles:
            for cont in container:
                for keys, values in cont.items():
                    for value in values:
                        process_values.append(value)
                        for prc in process_values:
                            if prc == st:
                                if values['fore'] == "green" and values['back'] == "white":
                                    print(Fore.GREEN + Back.WHITE + application)

                                elif values['fore'] == "white" and values['back'] == "green":
                                    print(Fore.WHITE + Back.GREEN + application)
                                    
                                elif values['fore'] == "red" and values['back'] == "cyan":
                                    print(Fore.RED + Back.CYAN + application)

                                elif values['fore'] == "yellow" and values['back'] == "magenta":
                                    print(Fore.YELLOW + Back.MAGENTA + application)

                                elif values['fore'] == "black" and values['back'] == "white":
                                    print(Fore.BLACK + Back.WHITE + application)

                                elif values['fore'] == "white" and values['back'] == "black":
                                    print(Fore.WHITE + Back.BLACK + application)

                                elif values['fore'] == "yellow" and values['back'] == "white":
                                    print(Fore.YELLOW + Back.WHITE + application)

                                elif values['fore'] == "black" and values['back'] == "red":
                                    print(Fore.BLACK + Back.RED + application)

                                elif values['fore'] == "black" and values['back'] == "green":
                                    print(Fore.BLACK + Back.GREEN + application)
                                
                                elif values['fore'] == 'cyan' and values['back'] == "black":
                                    print(Fore.CYAN + Back.BLACK + application)

                                elif values['fore'] == "white" and values['back'] == "green" and values['style'] == "bright":
                                    print(Fore.WHITE + Back.GREEN + Style.BRIGHT + application)
                                    
                                elif values['fore'] == "red" and values['back'] == "cyan" and values['style'] == "bright":
                                    print(Fore.RED + Back.CYAN + Style.BRIGHT + application)

                                elif values['fore'] == "yellow" and values['back'] == "magenta" and values['style'] == "bright":
                                    print(Fore.YELLOW + Back.MAGENTA + Style.BRIGHT + application)

                                elif values['fore'] == "black" and values['back'] == "white" and values['style'] == "bright":
                                    print(Fore.BLACK + Back.WHITE + Style.BRIGHT + application)

                                elif values['fore'] == "white" and values['back'] == "black" and values['style'] == "bright":
                                    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + application)

                                elif values['fore'] == "yellow" and values['back'] == "white" and values['style'] == "bright":
                                    print(Fore.YELLOW + Back.WHITE + Style.BRIGHT + application)

                                elif values['fore'] == "black" and values['back'] == "red" and values['style'] == "bright":
                                    print(Fore.BLACK + Back.RED + Style.BRIGHT + application)

                                elif values['fore'] == "black" and values['back'] == "green" and values['style'] == "bright":
                                    print(Fore.BLACK + Back.GREEN + Style.BRIGHT + application)
                                
                                elif values['fore'] == 'cyan' and value['back'] == "black" and values['style'] == "bright":
                                    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + application)

                                elif values['fore'] == "white" and values['back'] == "green" and values['style'] == "dim":
                                    print(Fore.WHITE + Back.GREEN + Style.DIM + application)
                                    
                                elif values['fore'] == "red" and values['back'] == "cyan" and values['style'] == "dim":
                                    print(Fore.RED + Back.CYAN + Style.DIM + application)

                                elif values['fore'] == "yellow" and values['back'] == "magenta" and values['style'] == "dim":
                                    print(Fore.YELLOW + Back.MAGENTA + Style.DIM + application)

                                elif values['fore'] == "black" and values['back'] == "white" and values['style'] == "dim":
                                    print(Fore.BLACK + Back.WHITE + Style.DIM + application)

                                elif values['fore'] == "white" and values['back'] == "black" and values['style'] == "dim":
                                    print(Fore.WHITE + Back.BLACK + Style.DIM + application)

                                elif values['fore'] == "yellow" and values['back'] == "white" and values['style'] == "dim":
                                    print(Fore.YELLOW + Back.WHITE + Style.DIM + application)

                                elif values['fore'] == "black" and values['back'] == "red" and values['style'] == "dim":
                                    print(Fore.BLACK + Back.RED + Style.DIM + application)

                                elif values['fore'] == "black" and values['back'] == "green" and values['style'] == "dim":
                                    print(Fore.BLACK + Back.GREEN + Style.DIM + application)
                                
                                elif values['fore'] == 'cyan' and values['back'] == "black" and values['style'] == "dim":
                                    print(Fore.CYAN + Back.BLACK + Style.DIM + application)
                            break
                        break
                    break

