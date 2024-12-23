from ConsoleM.Core.terminal import Terminal

terminal = Terminal()
terminal.handle_key_input()

while True:
    key = terminal.keys.get()
    print(f"{key!r}")
    if key == 'q':
        break
terminal.stop_handle_key_input()