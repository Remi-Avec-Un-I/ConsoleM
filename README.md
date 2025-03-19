# ConsoleM

A powerful Python library for terminal manipulation and text styling. ConsoleM provides a simple and intuitive API for creating beautiful terminal applications with advanced features like cursor control, text styling, and keyboard input handling.

## Features

* **Terminal Manipulation**
  * Precise cursor movement (absolute and relative positioning)
  * Screen clearing and line management
  * Alternate screen support for full-screen applications
  * Terminal size detection and cursor position tracking
  * Cursor visibility control
  * Non-blocking keyboard input handling

* **Text Styling**
  * Rich text formatting with intuitive markup syntax
  * 256-color support (foreground and background)
  * Text styles (bold, underline, italic, etc.)
  * Emoji support with automatic conversion
  * Easy-to-use BBCode-like markup syntax
  * Automatic style reset and cleanup

* **Input Handling**
  * Non-blocking keyboard input capture
  * Key event queue management
  * Special key detection (arrows, function keys, etc.)
  * Thread-safe input processing
  * Clean shutdown handling

## Installation

```bash
pip install ConsoleM
```

## Quick Start



```python
from ConsoleM import Terminal
from ConsoleM.Style.text import Text

# Create a terminal instance
term = Terminal()

# Print styled text
Text("[blue bold]Welcome to ConsoleM![/]").print()

# Get terminal size
width, height = term.get_terminal_size()
Text(f"[green]Terminal size: {width}x{height}[/]").print()
```

## Documentation

For detailed documentation, visit: https://consolem.readthedocs.io/en/latest/index.html

## License

This project is licensed under the MIT License - see the LICENSE file for details. 