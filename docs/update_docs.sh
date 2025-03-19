#!/bin/bash

# Exit on error
set -e

echo "Updating documentation..."

# Clean old build
echo "Cleaning old build..."
make clean

# Build HTML documentation
echo "Building HTML documentation..."
make html

echo "Documentation updated successfully!"
echo "You can find the updated documentation in _build/html/"

# Optional: if you're using GitHub Pages, uncomment these lines:
# echo "Copying to docs directory for GitHub Pages..."
# cp -r _build/html/* . 