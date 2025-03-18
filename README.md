# ConsoleM

A Python library for terminal manipulation and styling.

## Installation

You can install ConsoleM using pip:

```bash
pip install ConsoleM
```

## Usage

```python
from ConsoleM import Terminal
from ConsoleM.Style import *

# Create a terminal instance
term = Terminal()

# Use styling
styled_text = Text("[red underline]Hello[reset], :aries: [blue bold]World[/]!")
style_text.print()
```

## Features

- Terminal manipulation
- Text styling and coloring
- Cross-platform compatibility

## License

This project is licensed under the MIT License - see the LICENSE file for details. 