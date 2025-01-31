import time
from ConsoleM.Core import Terminal
from ConsoleM import Text
from ConsoleM.Core.const import Keys


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

def _show_page(terminal: Terminal, size: tuple[int, int], cursor_pos: list[int], text_pos: list[int], title: str = "", text: list[list[str]] = "") -> None:
    pass


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
    for _ in range(size[1] - (title_size - 1 if title_size else 0) - 4 - (0 if title else 1)):
        print(_get_middle_border(size, _get_border(inner_size)))
    print(_get_middle_border(size, _get_lower_border(inner_size)))
    terminal.write(_get_lower_border(size))
    terminal.write(str(Text("[gray] Press Ctrl+X to exit. [/]")))
    terminal.move_cursor(4, (title_size+1 if title_size else 3))
    cursor_pos = [4, (title_size+1 if title_size else 3)]
    terminal.show_cursor()
    terminal.handle_key_input()
    printable = [char for char in Keys.get_printable()]

    rst = [[]]
    text_pos = [0, 0]
    while True:
        key = terminal.get_key_from_queue()
        key = Keys.get(key)
        if not key:
            continue
        if key == Keys.CTRL_X:
            break

        if key == Keys.ENTER:
            cursor_pos = [4, cursor_pos[1] + 1]
            terminal.move_cursor(4, cursor_pos[1])
            rst.append([])
            text_pos[1] += 1

        elif key == Keys.BACKSPACE:
            if cursor_pos[0] == 4:
                if cursor_pos[1] == (title_size+1 if title_size else 3):
                    continue
                cursor_pos = [inner_size[0] + 2, cursor_pos[1] - 1]
                terminal.move_cursor(inner_size[0] + 2, cursor_pos[1])
                terminal.clear_end_of_line()
            else:
                cursor_pos[0] -= 1
                terminal.move_cursor_relative(-1, 0)
                terminal.clear_end_of_line()
                if text_pos[0] == len(rst[text_pos[1]]):
                    rst[text_pos[1]].pop()
                else:
                    rst[text_pos[1]].pop(text_pos[0])

        elif key in printable:
            if key == Keys.TAB:
                key = Keys.SPACE
            cursor_pos[0] += 1
            terminal.write(key.value)
            if cursor_pos[0] == size[0] - 2:
                cursor_pos = [4, cursor_pos[1] + 1]
                terminal.move_cursor(4, cursor_pos[1])
            if len(rst[text_pos[1]]) < cursor_pos[0] - 4:
                rst[text_pos[1]].append(key.value)
            else:
                rst[text_pos[1]].insert(text_pos[0], key.value)

    print(rst)
    time.sleep(5)
    terminal.stop_handle_key_input()
    terminal.restore_alternate_screen()