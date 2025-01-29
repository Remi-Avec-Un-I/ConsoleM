from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Iterable, Union, overload

from ConsoleM import Text
from ConsoleM.Core import Terminal
from ConsoleM.Core.const import Keys
from ConsoleM.Style.const import Color, AsciiEscapeCode


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
    :param indicator_search: The indicator to display when searching.
    :param indicator_error: The indicator to display when the number of selected items is not between the minimum and maximum.
    :param arrow: The arrow to display when an item is selected.
    :param empty_arrow: The empty arrow to display when an item is not selected.
    :param selected_bullet: The bullet to display when an item is selected.
    :param unselected_bullet: The bullet to display when an item is not selected.
    :param current_ligne_color: The color of the current line. Default is green.
    :param key_down: The key(s) to go down.
    :param key_up: The key(s) to go up.
    :param key_select: The key(s) to select an item.
    :param key_validate: The key(s) to validate the selection
    :param key_search: The key(s) to search an item.
    :param key_select_all: The key(s) to select all items.
    :param key_deselect_all: The key(s) to deselect all items.
    """
    items: Iterable[Items | str | dict]
    message: str = ""
    minimum: int = 1
    maximum: int = 1
    indicator: str = "[gray] (Use arrow keys to navigate, Enter to select, tab to validate and space to search) [/]"
    indicator_search: str = "[gray] Search: {search} [/]"
    indicator_error: str = "[red] (You must select between {minimum} and {maximum} items) [/]"
    arrow: str = ">"
    empty_arrow: str = " "
    selected_bullet: str = "•"
    unselected_bullet: str = "◦"
    current_ligne_color: Color | int = Color.GREEN
    key_down: list[str | Keys] | Keys | str = Keys.DOWN_ARROW
    key_up: list[str | Keys] | Keys | str = Keys.UP_ARROW
    key_select: list[str | Keys] | Keys | str = Keys.ENTER
    key_validate: list[str | Keys] | Keys | str = Keys.TAB
    key_search: list[str | Keys] | Keys | str = Keys.SPACE
    key_select_all: list[str | Keys] | Keys | str = "a"
    key_deselect_all: list[str | Keys] | Keys | str = "d"

def _show_selector(
        items: Iterable[Items],
        selected: Iterable[Items],
        cursor: int,
        arrow: str, empty_arrow: str,
        selected_bullet: str, unselected_bullet: str,
        color: Color | int,
):
    for i, item in enumerate(items):
        if item in selected:
            print(f"{arrow if cursor == i else empty_arrow} {selected_bullet}{'' if (color == Color.NONE or cursor != i) else AsciiEscapeCode.OCTAL.build(color if isinstance(color, int) else color.value)} {item.representation}{AsciiEscapeCode.OCTAL.build(Color.RESET.value)}")
        else:
            print(f"{arrow if cursor == i else empty_arrow} {unselected_bullet}{'' if (color == Color.NONE or cursor != i) else AsciiEscapeCode.OCTAL.build(color if isinstance(color, int) else color.value)} {item.representation}{AsciiEscapeCode.OCTAL.build(Color.RESET.value)}")

def get_key(*keys: Union[str, Keys]) -> list[Keys]:
    rst = []
    for key in keys:
        if isinstance(key, Keys):
            rst.append(key)
        rst.append(Keys.get(key, Keys[key.upper()]))
    return rst

def lines_count(items_it: Union[list[Items], str], width: int) -> int:
    if isinstance(items_it, str):
        return 1 + len(items_it) // width
    total_lines = 0
    for item in items_it:
        total_lines += 1 + len(item.representation) // width
    return total_lines

def find_possibles_items(items_it: list[Items], search: str) -> list[Items]:
    return [item for item in items_it if all([s in item.representation.lower() for s in search.lower()])]

@overload
def selector(
    items: Optional[Iterable[Union[Items, str, dict]]] = None,
    message: str = "",
    minimum: int = 1,
    maximum: int = 1,
    indicator: str = "[gray] (Use {key_up} to go up, and {key_down} to go down, {key_select} to select, {key_validate} to validate and {key_search} to search) [/]",
    indicator_search: str = "[gray] Search: {search} [/]",
    indicator_error: str = "[red] (You must select between {minimum} and {maximum} items) [/]",
    arrow: str = ">",
    empty_arrow: str = " ",
    selected_bullet: str = "•",
    unselected_bullet: str = "◦",
    current_ligne_color : Color | int = Color.GREEN,
    key_down: list[str | Keys] | Keys | str = Keys.DOWN_ARROW,
    key_up: list[str | Keys] | Keys | str = Keys.UP_ARROW,
    key_select: list[str | Keys] | Keys | str = Keys.ENTER,
    key_validate: list[str | Keys] | Keys | str = Keys.TAB,
) -> Union[any, list[any]]:
    ...

@overload
def selector(
    config: Union[SelectorConfig, dict],
) -> Union[any, list[any]]:
    ...

def selector(
    items: Optional[Iterable[Union[Items, str, dict]]] = None,
    message: str = "",
    minimum: int = 1,
    maximum: int = 1,
    indicator: str = "[gray] (Use {key_up} to go up, and {key_down} to go down, {key_select} to select, {key_validate} to validate and {key_search} to search) [/]",
    indicator_search: str = "[blue] Search: {search} [/]",
    indicator_error: str = "[red] (You must select between {minimum} and {maximum} items) [/]",
    arrow: str = ">",
    empty_arrow: str = " ",
    selected_bullet: str = "•",
    unselected_bullet: str = "◦",
    current_ligne_color : Color | int = Color.GREEN,
    key_down: list[str | Keys] | Keys | str = Keys.DOWN_ARROW,
    key_up: list[str | Keys] | Keys | str = Keys.UP_ARROW,
    key_select: list[str | Keys] | Keys | str = Keys.ENTER,
    key_validate: list[str | Keys] | Keys | str = Keys.TAB,
    key_search: list[str | Keys] | Keys | str = Keys.SPACE,
    key_select_all: list[str | Keys] | Keys | str = Keys.a,
    key_deselect_all: list[str | Keys] | Keys | str = Keys.d,
    config: Optional[SelectorConfig | dict] = None,
) -> Union[any, list[any]]:
    # TODO: ajouter une option de recherche, de select all et de deselect all
    """
    Initialize the selector.
    :param items: The items to display in the selector.
    :param message: The message to display above the selector.
    :param minimum: The minimum number of items to select.
    :param maximum: The maximum number of items to select.
    :param indicator: The indicator to display above the selector.
    :param indicator_search: The indicator to display when searching.
    :param indicator_error: The indicator to display when the number of selected items is not between the minimum and maximum.
    :param arrow: The arrow to display when an item is selected.
    :param empty_arrow: The empty arrow to display when an item is not selected.
    :param selected_bullet: The bullet to display when an item is selected.
    :param unselected_bullet: The bullet to display when an item is not selected.
    :param current_ligne_color: The color of the current line. Default is green.
    :param key_down: The key(s) to go down.
    :param key_up: The key(s) to go up.
    :param key_select: The key(s) to select an item.
    :param key_validate: The key(s) to validate the selection.
    :param key_search: The key(s) to search an item.
    :param key_select_all: The key(s) to select all items.
    :param key_deselect_all: The key(s) to deselect all items.
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
        indicator_search = config.indicator_search
        indicator_error = config.indicator_error
        arrow = config.arrow
        empty_arrow = config.empty_arrow
        selected_bullet = config.selected_bullet
        unselected_bullet = config.unselected_bullet
        current_ligne_color = config.current_ligne_color
        key_down = config.key_down
        key_up = config.key_up
        key_select = config.key_select
        key_validate = config.key_validate
        key_search = config.key_search
        key_select_all = config.key_select_all
        key_deselect_all = config.key_deselect_all

    if minimum < 1 or maximum < 1:
        raise ValueError("The minimum and maximum number of items to select must be at least 1.")
    if minimum > maximum:
        raise ValueError("The minimum number of items to select must be less than or equal to the maximum number of items to select.")
    if len(arrow) != len(empty_arrow):
        raise ValueError("The arrow and empty arrow must have the same length.")
    if len(selected_bullet) != len(unselected_bullet):
        raise ValueError("The selected bullet and unselected bullet must have the same length.")

    def get_key_from_param(k):
        return get_key(*k) if isinstance(k, list) else [k] if isinstance(k, Keys) else [Keys[k.upper()]]

    key_down = get_key_from_param(key_down)
    key_up = get_key_from_param(key_up)
    key_select = get_key_from_param(key_select)
    key_validate = get_key_from_param(key_validate)
    key_search = get_key_from_param(key_search)
    key_select_all = get_key_from_param(key_select_all)
    key_deselect_all = get_key_from_param(key_deselect_all)

    # Used for the indicator
    key_down_names = [k.get_name for k in key_down]
    key_up_names = [k.get_name for k in key_up]
    key_select_names = [k.get_name for k in key_select]
    key_validate_names = [k.get_name for k in key_validate]
    key_search_names = [k.get_name for k in key_search]

    # Used for the key input
    key_down_input = [k.name for k in key_down]
    key_up_input = [k.name for k in key_up]
    key_select_input = [k.name for k in key_select]
    key_validate_input = [k.name for k in key_validate]
    key_search_input = [k.name for k in key_search]
    key_select_all_input = [k.name for k in key_select_all]
    key_deselect_all_input = [k.name for k in key_deselect_all]

    terminal = Terminal()

    def clear_lines(items_iterator: Union[list[Items], str], terminal_size: tuple[int, int]):
        lines = lines_count(items_iterator, terminal_size[0])
        terminal.move_cursor_relative(0, -lines)
        print(' ' * (terminal_size[0] * lines), end='', flush=True)
        terminal.move_cursor_relative(0, -lines)

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
            key_validate=", ".join(key_validate_names),
            key_search=", ".join(key_search_names),
        )
        indicator_error = indicator_error.format(minimum=minimum, maximum=maximum)
        Text(message + indicator, True)
        _show_selector(items_it, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet, current_ligne_color)

        search = ""
        to_show_items = items_it.copy()
        while True:
            key = terminal.get_key_from_queue()

            if search:
                to_show_items = find_possibles_items(items_it, search)

            if key in key_up_input or key in key_down_input:
                if len(to_show_items) == 0:
                    continue
                size = terminal.get_terminal_size()

                cursor = (cursor - 1) if key in key_up_input else (cursor + 1)
                cursor %= len(to_show_items)

                clear_lines(to_show_items, size)
                print(end=' ', flush=True)
                _show_selector(to_show_items, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet, current_ligne_color)

            elif key in key_select_input:
                size = terminal.get_terminal_size()
                if items_it[cursor] in selected:
                    selected.remove(items_it[cursor])
                else:
                    selected.append(items_it[cursor])
                terminal.move_cursor_relative(0, -(lines_count(to_show_items, size[0])))
                _show_selector(to_show_items, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet, current_ligne_color)

            elif key in key_validate_input:
                if minimum <= len(selected) <= maximum:
                    break
                terminal.move_cursor_relative(0,
                                              -(lines_count(to_show_items, size[0]) + lines_count(indicator, size[0])))
                terminal.clear_line()
                Text(message + indicator_error).print()
                _show_selector(to_show_items, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet, current_ligne_color)

            elif key in key_search_input:
                search = ""
                new_to_show_items = None
                terminal.clear_lines_above(lines_count(to_show_items, size[0]) + lines_count(indicator, size[0]))
                Text(message + indicator_search.format(search=search)).print()
                while True:
                    if cursor >= len(to_show_items):
                        cursor = 0

                    if new_to_show_items is not None:
                        to_show_items = new_to_show_items
                    _show_selector(to_show_items, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet, current_ligne_color)

                    key = terminal.get_key_from_queue()
                    if key == Keys.ENTER.name:
                        if search == "":
                            terminal.clear_lines_above(lines_count(to_show_items, size[0]) + lines_count(indicator_search.format(search=search), size[0]))
                            Text(message + indicator).print()
                        break
                    if key == Keys.BACKSPACE.name:
                        if search:
                            search = search[:-1]
                            new_to_show_items = find_possibles_items(items_it, search)
                    elif key in [k.name for k in Keys.get_normal_chars()]:
                        search += Keys[key].value
                        new_to_show_items = find_possibles_items(items_it, search)
                    size = terminal.get_terminal_size()
                    terminal.clear_lines_above(lines_count(to_show_items, size[0]) + lines_count(indicator_search.format(search=search), size[0]))
                    Text(message + indicator_search.format(search=search)).print()

            else:
                terminal.move_cursor_relative(0, -(lines_count(items_it, size[0]) + lines_count(indicator, size[0])))
                terminal.clear_line()
                Text(message + indicator).print()
                _show_selector(items_it, selected, cursor, arrow, empty_arrow, selected_bullet, unselected_bullet, current_ligne_color)

        terminal.stop_handle_key_input()
        return [item.value for item in selected] if maximum > 1 else selected[0].value
    finally:
        terminal.show_cursor()
