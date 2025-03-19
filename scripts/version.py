import re
import sys
from pathlib import Path

def update_version(version_type: str):
    """Update version in setup.py and __init__.py"""
    setup_path = Path("setup.py")
    init_path = Path("ConsoleM/__init__.py")
    
    # Read current version from setup.py
    setup_content = setup_path.read_text()
    version_match = re.search(r'version="([^"]+)"', setup_content)
    if not version_match:
        print("Error: Could not find version in setup.py")
        sys.exit(1)
    
    current_version = version_match.group(1)
    major, minor, patch = map(int, current_version.split('.'))
    
    # Update version based on type
    if version_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif version_type == 'minor':
        minor += 1
        patch = 0
    elif version_type == 'patch':
        patch += 1
    else:
        print(f"Error: Invalid version type '{version_type}'")
        sys.exit(1)
    
    new_version = f"{major}.{minor}.{patch}"
    
    # Update setup.py
    new_setup_content = re.sub(
        r'version="[^"]+"',
        f'version="{new_version}"',
        setup_content
    )
    setup_path.write_text(new_setup_content)
    
    # Update __init__.py
    if init_path.exists():
        init_content = init_path.read_text()
        new_init_content = re.sub(
            r'__version__\s*=\s*"[^"]+"',
            f'__version__ = "{new_version}"',
            init_content
        )
        init_path.write_text(new_init_content)
    
    print(f"Version updated to {new_version}")
    return new_version

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python version.py [major|minor|patch]")
        sys.exit(1)
    
    update_version(sys.argv[1]) 