from ConsoleM import Terminal
from ConsoleM.Style.text import Text

def main():
    # Create terminal instance
    term = Terminal()
    
    # Create alternate screen
    term.create_alternate_screen()
    
    try:
        # Hide cursor
        term.hide_cursor()

        # Get terminal dimensions
        width, height = term.get_terminal_size()
        
        # Clear the screen
        term.clear()
        
        # Draw a box around the screen
        top = "┌" + "─" * (width - 2) + "┐"
        top = Text("[blue]" + top + "[/]").content
        middle = "\n".join(["│" + " " * (width - 2) + "│" for _ in range(height - 2)])
        middle = Text("[blue]" + middle + "[/]").content
        bottom = "└" + "─" * (width - 2) + "┘"
        bottom = Text("[blue]" + bottom + "[/]").content
        term.write(top + middle + bottom)
        
        # Add some text
        term.move_cursor(3, 3)
        Text("[bold cyan]Welcome to Full Screen Mode[/]").print()
        term.move_cursor(3, 4)
        Text("[yellow]Press 'q' to quit[/]").print()
        
        # Handle input
        term.handle_key_input()
        while True:
            key = term.get_key_from_queue()
            if key.lower() == 'q':
                break
            
    finally:
        # Cleanup
        term.stop_handle_key_input()
        term.show_cursor()
        term.restore_alternate_screen()

if __name__ == "__main__":
    main()
