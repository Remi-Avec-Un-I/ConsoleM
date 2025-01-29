import time

from ConsoleM.Core import Terminal
from ConsoleM import Text

def _get_upper_border(size: tuple[int, int]) -> str:
    return f"┌{'─' * (size[0] - 2)}┐"

def _get_middle_border(size: tuple[int, int], text: str = "") -> str:
    if not text:
        return f"├{'─' * (size[0] - 2)}┤"
    rst = ""
    for line in text.split("\n"):
        if len(line) > size[0] - 4:
            for i in range(0, len(line), size[0] - 4):
                rst += f"│ {line[i:i + size[0] - 4]}{' ' * (size[0] - 4 - len(line[i:i + size[0] - 4]))} │\n"
            rst = rst[:-1]
        else:
            rst += f"│ {line}{' ' * (size[0] - 4 - len(line))} │"
    return rst

def _get_border(size: tuple[int, int]) -> str:
    return f"│{' ' * (size[0] - 2)}│"

def _get_lower_border(size: tuple[int, int]) -> str:
    return f"└{'─' * (size[0] - 2)}┘"

def page(
    title: str = "",
) -> str:
    # TODO: fix la souris qui met le bordel, en capturant les signaux de la souris
    terminal = Terminal()
    terminal.hide_cursor()
    terminal.create_alternate_screen()
    terminal.move_cursor(1, 1)
    size = terminal.get_terminal_size()
    if size[0] < 10 or size[1] < 10:
        raise ValueError("Terminal size too small")
    inner_size = (size[0] - 4, size[1])
    title_size = 0

    print(_get_upper_border(size))

    if title:
        print(_get_middle_border(size, _get_upper_border(inner_size)))
        middle = _get_middle_border(size, _get_middle_border(inner_size, title))
        if not "\n" in middle:
            title_size = 3
        else:
            title_size = middle.count("\n") + 1
        print(middle)
        print(_get_middle_border(size, _get_lower_border(inner_size)))
        title_size += 2

    print(_get_middle_border(size, _get_upper_border(inner_size)))
    for _ in range(size[1] - (title_size - 1 if title_size else 0) - 4 - 1):
        print(_get_middle_border(size, _get_border(inner_size)))
    print(_get_middle_border(size, _get_lower_border(inner_size)))
    terminal.write(_get_lower_border(size))
    terminal.write(str(Text("[gray] Press Ctrl+X to exit. [/]")))
    time.sleep(5)
    terminal.show_cursor()
    terminal.restore_alternate_screen()