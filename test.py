from ConsoleM.Core import Terminal

terminal = Terminal()
terminal.handle_key_input()
while True:
    key = terminal.keys.get()
    if key == 'q':
        terminal.stop_handle_key_input()
        break
    print(f"\rPressed : {key!r}", end="", flush=True)