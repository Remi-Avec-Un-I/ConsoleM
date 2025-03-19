from ConsoleM import Terminal

term = Terminal()
term.handle_key_input()

while True:
    try:
        key = term.get_key_from_queue()
        print(key)
    except KeyboardInterrupt:
        break

term.stop_handle_key_input()