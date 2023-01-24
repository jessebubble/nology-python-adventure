#Available formats
formats = {"Bold":'\033[1m', "Italic":'\033[3m',
    "Underline":'\033[4m', "Blinking": '\033[5m',
    "Reversed": "\033[7m", "Strikethrough": '\033[9m',
    "DoubleUnderline":'\033[21m'
}

#Reset code to end the 'decoration'
reset_code = "\033[0m"

def colored_print(text = "", fg_color = None, bg_color = None, format = None):
    """
    Prints a decorated version of a text string with customised color and style
    ``text`` str, the actual text you want to decorate\n
    ``fg_color`` int, the color you want to use (values are from 0 to 255)\n
    ``bg_color`` int, the color you want to use on background (values are from 0 to 255)\n
    ``format`` str, the style you want to apply\n
    Possible values are [Bold, Italic, Underline, Blinking, Reversed, Strikethrough and DoubleUnderline]\n
    Using bg_color parameter ignores the fg_color argument
    """
    if (not isinstance(text, str)): text = ""
    if (not isinstance(fg_color, int)): fg_color = None
    if (not isinstance(bg_color, int)): bg_color = None
    if (not isinstance(format, str)): format = None
    
    #If no color has being selected, just use the default one
    result = text

    #Resetting colors to a valid input
    if (fg_color != None): fg_color = fg_color % 256
    if (bg_color != None): bg_color = bg_color % 256

    #If color is a valid key and different from None then 
    if (fg_color != None): result = "\033[38;5;{}m".format(fg_color) + text + reset_code
    if (bg_color != None): result = "\033[48;5;{}m".format(bg_color) + text + reset_code

    if (format != None): 
        selected_formats = format.split(";")
        for selected_format in selected_formats:
            if (selected_format in formats.keys()): result = formats[selected_format] + result + reset_code

    print(result)

def colored_sprint(text = "", fg_color = None, bg_color = None, format = None):
    """
    Returns a decorated version of a text string with customised color and style
    ``text`` str, the actual text you want to decorate\n
    ``fg_color`` int, the color you want to use (values are from 0 to 255)\n
    ``bg_color`` int, the color you want to use on background (values are from 0 to 255)\n
    ``format`` str, the style you want to apply\n
    Possible values are [Bold, Italic, Underline, Blinking, Reversed, Strikethrough and DoubleUnderline]\n
    Using bg_color parameter ignores the fg_color argument
    """
    if (not isinstance(text, str)): text = ""
    if (not isinstance(fg_color, int)): fg_color = None
    if (not isinstance(bg_color, int)): bg_color = None
    if (not isinstance(format, str)): format = None
    
    #If no color has being selected, just use the default one
    result = text

    #Resetting colors to a valid input
    if (fg_color != None): fg_color = fg_color % 256
    if (bg_color != None): bg_color = bg_color % 256

    #If color is a valid key and different from None then 
    if (fg_color != None): result = "\033[38;5;{}m".format(fg_color) + text + reset_code
    if (bg_color != None): result = "\033[48;5;{}m".format(bg_color) + text + reset_code

    if (format != None): 
        selected_formats = format.split(";")
        for selected_format in selected_formats:
            if (selected_format in formats.keys()): result = formats[selected_format] + result + reset_code

    return result