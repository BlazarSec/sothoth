from . import hooks

def load_into(sothoth):
    # pylint really likes to complain about no such member on these, even though the members exist.
    #pylint: disable=no-member
    for key, func in [
        ("exit", hooks.exit),
        ("exit", hooks.help)
    ]:
        sothoth.load_hook(key, func)
