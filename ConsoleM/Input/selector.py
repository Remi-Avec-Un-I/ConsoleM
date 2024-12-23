from dataclasses import dataclass
from typing import Iterable

from ConsoleM import Text
from ConsoleM.Core import Terminal
from ConsoleM.Core.const import Keys


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
    :param indicator: The indicator to display above the selector.
    :param indicator_error: The indicator to display when the number of selected items is not between the minimum and maximum.
    :param arrow: The arrow to display when an item is selected.
    :param empty_arrow: The empty arrow to display when an item is not selected.
    :param selected_bullet: The bullet to display when an item is selected.
    :param unselected_bullet: The bullet to display when an item is not selected.
    :param key_down: The key(s) to go down.
    :param key_up: The key(s) to go up.
    :param key_select: The key(s) to select an item.
    :param key_validate: The key(s) to validate the selection
    """
    items: Iterable[Items | str | dict]
    message: str = ""
    minimum: int = 1
    maximum: int = 1
    indicator: str = "[gray] (Use arrow keys to navigate, Enter to select, tab to validate) [/]"
    indicator_error: str = "[red] (You must select between {minimum} and {maximum} items) [/]"
    arrow: str = ">"
    empty_arrow: str = " "
    selected_bullet: str = "•"
    unselected_bullet: str = "◦"
    key_down: list[str | Keys] | Keys | str = Keys.DOWN_ARROW
    key_up: list[str | Keys] | Keys | str = Keys.UP_ARROW
    key_select: list[str | Keys] | Keys | str = Keys.ENTER
    key_validate: list[str | Keys] | Keys | str = Keys.TAB

def _show_selector(
        items: Iterable[Items],
        selected: Iterable[Items],
        cursor: int,
        arrow: str, empty_arrow: str,
        selected_bullet: str, unselected_bullet: str,
):
    for i, item in enumerate(items):
        if item in selected:
            print(f"{arrow if cursor == i else empty_arrow} {selected_bullet} {item.representation}")
        else:
            print(f"{arrow if cursor == i else empty_arrow} {unselected_bullet} {item.representation}")

def get_key(*keys: str | Keys) -> list[Keys]:
    rst = []
    for key in keys:
        if isinstance(key, Keys):
            rst.append(key)
        rst.append(Keys[key.upper()])
    return rst

def lines_count(items_it: list[Items] | str, width: int) -> int:
    if isinstance(items_it, str):
        return 1 + len(items_it) // width
    total_lines = 0
    for item in items_it:
        total_lines += 1 + len(item.representation) // width
    return total_lines

def selector(
        items: Iterable[Items | str | dict] = None,
        message: str = "",
        minimum: int = 1,
        maximum: int = 1,
        indicator: str = "[gray] (Use {key_up} to go up, and {key_down} to go down, {key_select} to select, {key_validate} to validate) [/]",
        indicator_error: str = "[red] (You must select between {minimum} and {maximum} items) [/]",
        arrow: str = ">",
        empty_arrow: str = " ",
        selected_bullet: str = "•",
        unselected_bullet: str = "◦",
        key_down: list[str | Keys] | Keys | str = Keys.DOWN_ARROW,
        key_up: list[str | Keys] | Keys | str = Keys.UP_ARROW,
        key_select: list[str | Keys] | Keys | str = Keys.ENTER,
        key_validate: list[str | Keys] | Keys | str = Keys.TAB,
        config: SelectorConfig | dict = None,
) -> int | any:
    """
    Initialize the selector.
    :param items: The items to display in the selector.
    :param message: The message to display above the selector.
    :param minimum: The minimum number of items to select.
    :param maximum: The maximum number of items to select.
    :param indicator: The indicator to display above the selector.
    :param indicator_error: The indicator to display when the number of selected items is not between the minimum and maximum.
    :param arrow: The arrow to display when an item is selected.
    :param empty_arrow: The empty arrow to display when an item is not selected.
    :param selected_bullet: The bullet to display when an item is selected.
    :param unselected_bullet: The bullet to display when an item is not selected.
    :param key_down: The key(s) to go down.
    :param key_up: The key(s) to go up.
    :param key_select: The key(s) to select an item.
    :param key_validate: The key(s) to validate the selection.
    :param config: The configuration object/dict. If provided, the other arguments are ignored.
    :return: The value of the selected item(s). If no value are provided (ex: items are strings), the index of the selected item(s) is returned.
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
        indicator = config.indicator
        indicator_error = config.indicator_error
        key_down = config.key_down
        key_up = config.key_up
        key_select = config.key_select
        key_validate = config.key_validate

    if minimum < 1 or maximum < 1:
        raise ValueError("The minimum and maximum number of items to select must be at least 1.")
    if minimum > maximum:
        raise ValueError("The minimum number of items to select must be less than or equal to the maximum number of items to select.")
    if len(arrow) != len(empty_arrow):
        raise ValueError("The arrow and empty arrow must have the same length.")
    if len(selected_bullet) != len(unselected_bullet):
        raise ValueError("The selected bullet and unselected bullet must have the same length.")

    key_down = get_key(*key_down) \
        if isinstance(key_down, list) else [key_down] \
        if isinstance(key_down, Keys) else [Keys[key_down.upper()]]
    key_up = get_key(*key_up) \
        if isinstance(key_up, list) else [key_up] \
        if isinstance(key_up, Keys) else [Keys[key_up.upper()]]
    key_select = get_key(*key_select) \
        if isinstance(key_select, list) else [key_select] \
        if isinstance(key_select, Keys) else [Keys[key_select.upper()]]
    key_validate = get_key(*key_validate) \
        if isinstance(key_validate, list) else [key_validate] \
        if isinstance(key_validate, Keys) else [Keys[key_validate.upper()]]

    # Used for the indicator
    key_down_names = [k.get_name for k in key_down]
    key_up_names = [k.get_name for k in key_up]
    key_select_names = [k.get_name for k in key_select]
    key_validate_names = [k.get_name for k in key_validate]

    # Used for the key input
    key_down_input = [k.name for k in key_down]
    key_up_input = [k.name for k in key_up]
    key_select_input = [k.name for k in key_select]
    key_validate_input = [k.name for k in key_validate]

    terminal = Terminal()
    try:
        terminal.hide_cursor()
        terminal.handle_key_input()

        items_it = []
        total_lines = 0
        size = terminal.get_terminal_size()
        for i, item in enumerate(items):
            if isinstance(item, str):
                items_it.append(Items(item, i))
            elif isinstance(item, dict):
                items_it.append(Items(item["representation"], item["value"]))
            elif isinstance(item, Items):
                items_it.append(item)
            else:
                raise ValueError(f"Invalid item type: {type(item)}. Expected str, dict or Items.")
            total_lines += 1 + len(items_it[-1].representation) // size[0]

        selected = []
        cursor = 0
        indicator = indicator.format(
            key_up=", ".join(key_up_names),
            key_down=", ".join(key_down_names),
            key_select=", ".join(key_select_names),
            key_validate=", ".join(key_validate_names)
        )
        indicator_error = indicator_error.format(minimum=minimum, maximum=maximum)
        Text(message + indicator, True)
        _show_selector(items_it, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet)

        while True:
            key = terminal.get_key_from_queue()
            if key in key_up_input or key in key_down_input:
                size = terminal.get_terminal_size()

                cursor = (cursor - 1) if key in key_up_input else (cursor + 1)
                cursor %= len(items_it)

                terminal.move_cursor_relative(0, -(lines_count(items_it, size[0])))

                _show_selector(items_it, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet)
            if key in key_select_input:
                size = terminal.get_terminal_size()
                if items_it[cursor] in selected:
                    selected.remove(items_it[cursor])
                else:
                    selected.append(items_it[cursor])
                terminal.move_cursor_relative(0, -(lines_count(items_it, size[0])))
                _show_selector(items_it, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet)

            elif key in key_validate_input:
                if minimum <= len(selected) <= maximum:
                    break
                else:
                    terminal.move_cursor_relative(0,
                                                  -(lines_count(items_it, size[0]) + lines_count(indicator, size[0])))
                    terminal.clear_line()
                    Text(message + indicator_error).print()
                    _show_selector(items_it, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet)

            else:
                terminal.move_cursor_relative(0, -(lines_count(items_it, size[0]) + lines_count(indicator, size[0])))
                terminal.clear_line()
                Text(message + indicator).print()
                _show_selector(items_it, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet)

        terminal.stop_handle_key_input()
        return [item.value for item in selected] if maximum > 1 else selected[0].value
    finally:
        terminal.show_cursor()