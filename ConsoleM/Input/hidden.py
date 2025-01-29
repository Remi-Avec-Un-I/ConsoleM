from ConsoleM.Core.terminal import Terminal, Keys


def hidden(prompt: str = '') -> str:
    """Prompt the user for a password, hiding the input by replacing user input by '*'."""
    rst = ''
    terminal = Terminal()
    print(prompt, end='', flush=True)
    try:
        terminal.hide_cursor()
        terminal.handle_key_input()
        while True:
            key = terminal.get_key_from_queue()
            if key == Keys.ENTER.name:
                print(flush=True)
                break
            if key == Keys.BACKSPACE.name:
                if not rst:
                    continue
                rst = rst[:-1]
                pos = terminal.get_cursor_position()
                size = terminal.get_terminal_size()
                if pos[0] == 1:
                    terminal.move_cursor(size[0] + 2, pos[1] - 1)
                    terminal.clear_end_of_line()
                else:
                    terminal.move_cursor_relative(-1, 0)
                    terminal.clear_end_of_line()
            if key not in [key.name for key in Keys.get_normal_chars()]:
                continue
            else:
                rst += key
                print('*', end='', flush=True)
    finally:
        terminal.stop_handle_key_input()
        terminal.show_cursor()
    return rst
