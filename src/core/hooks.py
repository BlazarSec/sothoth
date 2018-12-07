# run registered on_exit handle
def exit(sothoth, args):
    (sothoth.on_exit)()

exit.help = "exit sothoth"

# provide list of commands or help for specific commands
def help(sothoth, args):
    if len(args):
        for name in args:
            try:
                print(f"{name}: {sothoth.command_hooks[name].help}")
            
            except KeyError:
                raise RuntimeError(f"'{name}' not found.")
            
            except AttributeError:
                raise RuntimeError(f"The author of '{name}' has not provided helper info for the requested command.")

    else:
        print("Available commands:")

        for name in sothoth.command_hooks:
            print(f" * {name}")

help = "list available commands.\nif 1 or more commands is supplied as an argument, instead receive a summary of each."
