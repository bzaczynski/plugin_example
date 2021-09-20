import builtins
import zipimport
from pathlib import Path

_plugins = []


def load_plugins(path=Path("plugins")):
    for archive in sorted(path.glob("*.zip")):
        importer = zipimport.zipimporter(archive)
        module = importer.load_module("plugin")
        _plugins.append(getattr(module, "main"))
    _print("Loaded plugins:", _plugins)


def wrapper(text, *args, **kwargs):
    for plugin in _plugins:
        plugin(text)
    _print(text, *args, **kwargs)


_print = builtins.print
builtins.print = wrapper
load_plugins()
