class SothothInstance():
    def __init__(self):
        self.command_hooks = {} # string: func
        self.components = {} # string: component 
        self.on_exit = None

    def load_hook(self, key, func):
        if key in self.command_hooks:
            obj = self.command_hooks[key]
            raise ValueError(f"'{key}' already bound to <{type(obj).__name__} {obj.__module__}.{obj.__name__}>")

        self.command_hooks[key] = func

    def invoke(self, command_string):
        # split command_string into command key and args
        command_string = command_string.strip(" \n;")
        in_quote = False
        words = []

        # blocks of text wrapped in quotes should not be split
        for word in command_string.split(" "):
            if '"' in word and "\\\"" not in word:
                if in_quote:
                    in_quote = False
                    words[-1] += " " + word.replace('"', "")

                else:
                    in_quote = True
                    words.append(word.replace('"', ""))

                continue

            if in_quote:
                words[-1] += " " + word

            else:
                words.append(word)
        
        self.command_hooks[words[0]](self, words[1])

class Component():
    pass
