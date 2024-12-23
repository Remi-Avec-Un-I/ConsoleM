from dataclasses import dataclass
from typing import Iterable

from ConsoleM.Core import Terminal

@dataclass
class Items:
    """
    The items to display in the selector.
    :param representation: The string representation of the item.
    :param value: The value of the item to return.
    """
    representation: str
    value: any

    def __str__(self):
        return self.representation

@dataclass
class SelectorConfig:
    """
    The configuration for the selector function.
    :param items: The items to display in the selector.
    :param message: The message to display above the selector.
    :param minimum: The minimum number of items to select.
    :param maximum: The maximum number of items to select.
    """
    items: Iterable[Items | str | dict]
    message: str = ""
    minimum: int = 1
    maximum: int = 1

def _show_selector(items: Iterable[Items], selected: Iterable[Items], cursor: int, terminal: Terminal):
    for i, item in enumerate(items):
        if item in selected:
            print(f"{'>' if cursor == i else ' '} • {item.representation}")
        else:
            print(f"{'>' if cursor == i else ' '} ◦ {item.representation}")

def selector(
        items: Iterable[Items | str | dict] = None,
        message: str = "",
        minimum: int = 1,
        maximum: int = 1,
        config: SelectorConfig | dict = None,
):
    """
    Initialize the selector.
    :param items: The items to display in the selector.
    :param message: The message to display above the selector.
    :param minimum: The minimum number of items to select.
    :param maximum: The maximum number of items to select.
    :param config: The configuration object/dict. If provided, the other arguments are ignored.
    """
    if not items and not config :
        raise ValueError("You must provide either items and message or a config object.")

    if config:
        if isinstance(config, dict):
            config = SelectorConfig(**config)
        items = config.items
        message = config.message
        minimum = config.minimum
        maximum = config.maximum

    if minimum < 1:
        raise ValueError("The minimum number of items to select must be at least 1.")
    if maximum < 1:
        raise ValueError("The maximum number of items to select must be at least 1.")
    if minimum > maximum:
        raise ValueError("The minimum number of items to select must be less than or equal to the maximum number of items to select.")


    terminal = Terminal()
    terminal.handle_key_input()

    items_it = []
    for item in items:
        if isinstance(item, str):
            items_it.append(Items(item, item))
        elif isinstance(item, dict):
            items_it.append(Items(item["representation"], item["value"]))
        elif isinstance(item, Items):
            items_it.append(item)
        else:
            raise ValueError(f"Invalid item type: {type(item)}. Expected str, dict or Items.")

    selected = []
    cursor = 0
    print(message)
    _show_selector(items_it, selected, cursor, terminal)

    while True:
        key = terminal.keys.get()
        if key == "\x1b":
            key += terminal.keys.get() + terminal.keys.get()
            if key == "\x1b[A":
                cursor = (cursor - 1) % len(items_it)
            elif key == "\x1b[B":
                cursor = (cursor + 1) % len(items_it)
            terminal.move_cursor_relative(0, -len(items_it))
            _show_selector(items_it, selected, cursor, terminal)
        if key =="q":
            break
    terminal.stop_handle_key_input()