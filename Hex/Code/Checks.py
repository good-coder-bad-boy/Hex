# from sys import argv # unneeded (https://github.com/good-coder-bad-boy/Hex/blob/d7aebca0c74d22ad479d3fc34c47682e33009bc9/Hex/Code/Checks.py#L36-L36)

# Hex Imports
from Errors import defaults as e


# Definitions
class check:
    def __init__(self, errs: dict[str, function] = e):
        self.errs = errs

        self.errs.update()

    def args(self, args: list):
        if not any(args): # file is supplied
            self.errs["Melon"]()
        else:
            try: # file is valid
                if args != None:
                    open(args[1], "r").close()
            except OSError:
                self.errs["Domain"]()

    def tty(self):
        try: # platform supports tty
            import tty, termios
        except ModuleNotFoundError:
            self.errs["TTY"]()


# Runtime
if __name__ == "__main__":
    c = check()

    c.tty()
    # c.args(argv) # improbable that user will run this file via commandline