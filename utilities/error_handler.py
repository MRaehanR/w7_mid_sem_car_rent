from utilities.print_with_color import print_error

def error_handler_with_print_error(type, function, error_message: str):
    try:
        type(function)
    except ValueError:
        print_error(error_message)