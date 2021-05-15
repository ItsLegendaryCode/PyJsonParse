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
    Union: Fore, Back
           1. green, white
           2. white, green
           3. red, cyan
           4. yellow, magenta
           5. black, white
           6. white, black
           7. yellow, white
           8. black, red
           9. black, green

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
        for style in styles:
            for cont in container:
                for keys, values in cont.items():
                    for value in values:
                        process_values.append(value)
                        for prc in process_values:
                            if prc == style:
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
                            break
                        break
                    break

